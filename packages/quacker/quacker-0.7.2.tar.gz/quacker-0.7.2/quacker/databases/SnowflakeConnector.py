# Native Python Imports
import os

# Third-Party Imports
import pandas as pd
import snowflake.connector

class ClassSnowflakeConnector:
    """
    A class to connect to a Snowflake database, execute queries, and export data.
    """

    def __init__(self, **kwargs):
        """
        Initialize the SnowflakeConnector with provided credentials.
        """
        required_keys = ['account', 'user', 'password', 'warehouse', 'role', 'database', 'schema']
        missing_or_empty_credentials = [key for key in required_keys if not kwargs.get(key)]

        if missing_or_empty_credentials:
            missing_str = ", ".join(missing_or_empty_credentials)
            raise ValueError(f"Missing or empty Snowflake credentials: {missing_str}. Please provide all required credentials and ensure they are not empty.")

        self.account = kwargs.get('account')
        self.user = kwargs.get('user')
        self.password = kwargs.get('password')
        self.warehouse = kwargs.get('warehouse')
        self.role = kwargs.get('role')
        self.database = kwargs.get('database')
        self.schema = kwargs.get('schema')


    def _connect(self):
        """
        Create and return a Snowflake connection object.
        """
        return snowflake.connector.connect(
            user=self.user,
            password=self.password,
            account=self.account,
            warehouse=self.warehouse,
            role=self.role,
            database=self.database,
            schema=self.schema,
        )

    def query_to_dataframe(self, query: str) -> pd.DataFrame:
        """
        Execute a query and return a pandas DataFrame.
        """
        with self._connect() as conn:
            try:
                print(f"Executing snowflake query: {query}")

                dataframe = pd.read_sql(query, conn)

                print(f"Successfully executed snowflake query: {query}")
                print("head:")
                print(dataframe.head())
                
                return dataframe
            except snowflake.connector.Error as e:
                print(f"An error occurred when attempting to execute snowflake query: {e}")
                raise