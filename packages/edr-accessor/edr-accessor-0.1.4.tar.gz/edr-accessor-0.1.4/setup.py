from setuptools import setup, find_packages

setup(
    name='edr-accessor',
    version='0.1.4',
    packages=find_packages(),
    description='A pandas DataFrame accessor for accessing Enterprise Data Repository (EDR) tables with Spark.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Peter Boyd',
    author_email='peter.g.boyd@gmail.com',
    license='MIT',
    install_requires=[
        'pandas',
        'pyspark',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
