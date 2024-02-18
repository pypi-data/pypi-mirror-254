# edr-accessor/edr-accessor/__init__.py

import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from typing import Optional

from pyspark.sql import SparkSession
import pandas as pd


@pd.api.extensions.register_dataframe_accessor("edr")
class EDRAccessor:
    def __init__(self, pandas_obj: pd.DataFrame):
        """Initialize the custom DataFrame accessor.

        Args:
            panda_obj (pd.DataFrame): The DataFrame to which the accessor is attached.
        """
        self._obj = pandas_obj


    @staticmethod
    def mount_storage(self, storage_account: str, container: str, mount_point: str, client_secret: str, storage_key: str) -> None:
        """Mount an Azure storage container to DBFS.

        Args:
            storage_account (str): The name of the Azure storage account.
            container (str): The name of the Azure storage container.
            mount_point (str): The DBFS path to mount the storage container to.
            client_secret (str): The Azure Active Directory application secret.
            storage_key (str): name of the key to access client secret.

        Raises:
            RuntimeError: If the mount operation fails or if dbutils are not available.

        Returns:
            None: The function does not return any value. It prints a confirmation message after mounting the storage.
        """
        try:
            # Access dbutils when running inside Databricks
            from pyspark.dbutils import DBUtils
            dbutils = DBUtils(self._get_spark_session())

            configs = {
                    f"fs.azure.account.key.{storage_account}.blob.core.windows.net":
                    dbutils.secrets.get(scope=client_secret, key=storage_key),

            }

            # Check if the mount point already exists
            if any(mount.mountPoint == mount_point for mount in dbutils.fs.mounts()):
                print(f"Mount point {mount_point} already exists")
            else:
                # Mount the storage
                dbutils.fs.mount(
                    source=f"wasbs://{container}@{storage_account}.blob.core.windows.net/",
                    mount_point=mount_point,
                    extra_configs=configs
                )
                print(f"Mounted {container} to {mount_point}")
        except ImportError as e:
            raise RuntimeError("This function should only be used within a Databricks notebook or job environment.") from e
        except Exception as e:
            raise RuntimeError(f"Error mounting storage: {e}") from e

    @staticmethod
    def _get_spark_session() -> SparkSession:
        """Get or create a Spark session. Currently only within a databricks session.

        Returns:
            SparkSession: An active Spark session.
        """
        spark = SparkSession.builder \
            .appName("EDR Accessor App") \
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
            .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
            .getOrCreate()
        spark.conf.set("spark.databricks.delta.preview.enabled", "true")
        return spark

    def list_databases(self) -> pd.Series:
        """List all databases as a pandas Series.

        Returns:
            pd.Series: A pandas Series object containing names of all the currently available databases.
        """
        spark_session = self._get_spark_session()
        databases = spark_session.catalog.listDatabases()
        return pd.Series([db.name for db in databases])
    
    def list_tables(self, db_name: str) -> pd.Series:
        """List all tables in a given database as a pandas Series.

        Args:
            db_name (str): The name of the database whose tables are to be listed.

        Returns:
            pd.Series: A pandas Series object containing table names available in a given database (db_name).
        """
        spark_session = self._get_spark_session()
        table_info = spark_session.catalog.listTables(f"{db_name}")
        return pd.Series([table.name for table in table_info])
    
    def import_table(self, tablename: str, database: Optional[str] = None) -> None:
        """Retrieve a table from Spark and insert its data into the original DataFrame.

        Args:
            tablename (str): The name of the table to retrieve.
            database (Optional[str], optional): The database in which the table resides. Default is None, the default database.
        
        Raises:
            ValueError: If the original DataFrame is not empty.
        """
        if not self._obj.empty:
            raise ValueError(f"The DataFrame is not empty. Please instantiate a new DataFrame to populate it with the table {tablename}")
        spark_session = self._get_spark_session()
        # grab the table and convert to a pandas DataFrame.
        pandas_df = spark_session.table(f"{database}.{tablename}").toPandas()

        # insert column names and data into the existing empty DataFrame.
        self._obj[pandas_df.columns] = pandas_df

    def table_rowcounts(self, database: Optional[str] = None) -> pd.DataFrame:
        """
        Retrieve row counts for tables in a specified database, or for all tables in all databases
        if no database is specified.

        Args:
            database (Optional[str]): Name of the database from which to retrieve row counts for each table.
                                    If None, retrieves row counts for all tables across all databases.

        Returns:
            pd.DataFrame: A pandas DataFrame containing the database name, table name, and row count for each table.
        """
        spark_session = self._get_spark_session()

        if database:
            databases = [database]
        else:
            databases = [db.name for db in spark_session.catalog.listDatabases()]

        row_counts_data = []
        for db in databases:
            tables = spark_session.catalog.listTables(db)
            for table in tables:
                query = f"SELECT COUNT(*) as count FROM {db}.{table.name}"
                count = spark_session.sql(query).first()[0]
                row_counts_data.append({'database': db, 'table': table.name, 'row_count': count})

        return pd.DataFrame(row_counts_data)
    
    def to_delta_table(self, table_name: str, container: str, storage_account: str, db: str = 'edr', mode: str = 'overwrite', overwrite_schema: bool = True) -> None:
        """Write the pandas DataFrame to a Delta Lake table in Azure Data Lake Storage Gen2.

        This function writes the contents of the pandas DataFrame associated with the EDRAccessor to a specified Delta Lake table.
        The Delta table is identified by the combination of the container, storage account, database, and table name.
        If the table already exists, the write operation will behave according to the specified mode.
        If overwrite_schema is set to True, the schema of the existing Delta table will be overwritten with the DataFrame's schema.
        
        This method replaces the create_overwrite_table function from dsai_databricks_helpers.

        Args:
            table_name (str): The name of the Delta table to write to.
            container (str): The name of the Azure storage container where the Delta table is located.
            storage_account (str): The name of the Azure storage account that contains the container.
            db (str, optional): The name of the database within the Delta Lake. Defaults to 'edr'.
            mode (str, optional): The mode for saving the DataFrame. Defaults to 'overwrite'.
                Options:
                    'append' - Add new rows to the existing Delta table.
                    'overwrite' - Replace the existing Delta table with the new DataFrame.
                    'ignore' - If the Delta table already exists, the write operation is ignored.
                    'error' or 'errorifexists' - If the Delta table already exists, an error is raised.
            overwrite_schema (bool, optional): Whether to overwrite the Delta table schema with the DataFrame's schema.
                Defaults to True.

        Raises:
            ValueError: If the DataFrame associated with the EDRAccessor is empty.

        Returns:
            None: The function does not return any value. It prints a confirmation message after writing the table.
        """
        if self._obj.empty:
            raise ValueError("The DataFrame is empty. Cannot write to Delta table.")

        # check if storage container exists, is a delta lake?
        # there are a lot of assumptions here, like the user has write permissions to the datalake.
        save_path = f"abfss://{container}@{storage_account}.dfs.core.windows.net/{db}/{table_name.lower()}/"
    
        full_table_name = f'{db}.{table_name}'
        spark_session = self._get_spark_session()
        spark_df = spark_session.createDataFrame(self._obj)

        # ugh. Run sql command to ensure db exists.
        spark_session.sql(f"CREATE DATABASE IF NOT EXISTS {db}")

        # Write the Spark DataFrame to a Delta table
        writer = spark_df.write.format("delta").mode(mode)
        if overwrite_schema:
            writer.option("overwriteSchema", "true")
        writer.save(save_path)
        print(f"Table {full_table_name} written.")
        return

from . import EDRAccessor
