from setuptools import setup, find_packages
import pathlib

# read the contents of your README file
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='quacker',
    version='0.7.2',
    description='Sync dbt sources and models from cloud warehouses to duckdb',  # Short description
    long_description=long_description,  # Long description read from the README.md
    long_description_content_type='text/markdown',  # This is important to specify the markdown format
    author='Amir Jaber',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.5.0, <3.0.0',
        'snowflake-connector-python>=2.1.0, <4.0.0',
        'pyarrow>=12.0.0, <15.0.0',
        'duckdb>=0.9.0, <0.10.0',
        'db-dtypes>=1.1.0, <2.0.0',
        'pyyaml>=6.0.0, <7.0.0',
        'google-cloud-bigquery>=3.5.0, <4.0.0',
    ],
    entry_points={
        'console_scripts': [
            'quack=quacker.cli:main',
        ],
    },
)