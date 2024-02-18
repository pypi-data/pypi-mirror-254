# Native Python imports
import os

# Third party imports
import duckdb
import pandas as pd

class ClassDuckDBConnector:
    """
    A class to handle DuckDB database operations, including loading data
    from a Pandas DataFrame into a specified database, schema, and table.
    Each call to load_dataframe can specify a different database.
    """

    def __init__(self, db_path: str):
        """
        Initialize the DuckDBConnector with a base path for database files.
        If the path does not exist, it will be created.

        Args:
            db_path (str): Base path for the DuckDB database files.
        """
        self.db_path = db_path
        if not os.path.exists(db_path):
            os.makedirs(db_path)

    def connect(self, db_file: str) -> duckdb.DuckDBPyConnection:
        """
        Connect to a specific DuckDB database file.

        Args:
            db_file (str): The database file name to connect to.

        Returns:
            duckdb.DuckDBPyConnection: A connection object to the DuckDB database.
        """
        db_file_path = os.path.join(self.db_path, f"{db_file}.duckdb")
        return duckdb.connect(db_file_path)

    def load_dataframe(self, dataframe: pd.DataFrame, database_name: str, schema_name: str, table_name: str) -> None:
        """
        Load a DataFrame into the specified schema and table in DuckDB.
        If the schema or table does not exist, they will be created.

        Args:
            dataframe (pd.DataFrame): The DataFrame to load into DuckDB.
            database_name (str): The name of the database (used as the file name).
            schema_name (str): The name of the schema.
            table_name (str): The name of the table.
        """
        # Convert data types before loading
        dataframe = self._convert_dataframe_dtypes(dataframe)

        with self.connect(database_name) as conn:
            # create the schema if it does not exist
            print(f"Attempting to create schema {schema_name} in duckdb database {database_name}")
            conn.execute(f"create schema if not exists {schema_name}")
            print(f"Successfully created schema {schema_name} in duckdb database {database_name}")

            # prepare the full table name
            full_table_name = f"{schema_name}.\"{table_name}\""

            # Check if an object with the same name as the table exists and whether it's a view
            result = conn.execute(f"select table_type from information_schema.tables where table_schema = '{schema_name}' and table_name = '{table_name}'").fetchall()
            if result:
                # Use index 0 to access the first (and only) column in the result tuple
                object_type = result[0][0]
                if object_type.lower() == 'view':
                    # If it's a view, drop the view
                    conn.execute(f"drop view if exists {full_table_name}")

            # create or replace the table with the dataframe content
            print(f"Attempting to drop table {full_table_name} in duckdb database {database_name} with query:")
            print(f"drop table if exists {full_table_name}")
            conn.execute(f"drop table if exists {full_table_name}")
            print(f"Successfully dropped table {table_name} in duckdb database {database_name}")
            
            print(f"Attempting to register dataframe with table '{table_name}' in duckdb database {database_name}")
            conn.register(f"{table_name}", dataframe)
            print(f"Successfully registered dataframe with table '{table_name}' in duckdb database {database_name}")

            print(f"Attempting to create table {full_table_name} in duckdb database {database_name} with query:")
            print(f"create table {full_table_name} as select * from {table_name}")
            conn.execute(f"create table {full_table_name} as select * from \"{table_name}\"")
            print(f"Successfully created table {full_table_name} in duckdb database {database_name}")

    def _convert_dataframe_dtypes(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Convert incompatible data types in the DataFrame to types that are
        compatible with DuckDB.

        Args:
            dataframe (pd.DataFrame): The DataFrame to convert.

        Returns:
            pd.DataFrame: The DataFrame with converted data types.
        """
        # Convert 'dbdate' columns to 'date'
        for col, dtype in dataframe.dtypes.items():
            if dtype.name == 'dbdate':
                dataframe[col] = pd.to_datetime(dataframe[col]).dt.date
        return dataframe