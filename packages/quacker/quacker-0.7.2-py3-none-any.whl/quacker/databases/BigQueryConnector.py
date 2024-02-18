# Native Python Imports
import os

# Third-Party Imports
import pandas as pd
from google.cloud import bigquery

class ClassBigQueryConnector:
    """
    A class to connect to a BigQuery database, execute queries, and export data.
    """

    def __init__(self, **kwargs):
        """
        Initialize the BigQueryConnector with provided credentials.
        """
        # BigQuery credentials are usually provided through a service account JSON file
        self.keyfile_path = kwargs.get('keyfile_path')
        if not self.keyfile_path or not os.path.exists(self.keyfile_path):
            raise ValueError("Invalid or missing credentials path for BigQuery. Please provide a valid service account JSON file.")

        self.project_id = kwargs.get('project_id')
        if not self.project_id:
            raise ValueError("Missing project ID for BigQuery. Please provide the project ID.")

        self.client = bigquery.Client.from_service_account_json(self.keyfile_path, project=self.project_id)

    def query_to_dataframe(self, query: str) -> pd.DataFrame:
        """
        Execute a query and return a pandas DataFrame.
        """
        try:
            print(f"Executing BigQuery query: {query}")
            query_job = self.client.query(query)
            dataframe = query_job.result().to_dataframe()
            print(f"Successfully executed BigQuery query: {query}")
            print("head:")
            print(dataframe.head())
            return dataframe
        except Exception as e:
            print(f"An error occurred when attempting to execute BigQuery query: {e}")
            raise