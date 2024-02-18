# Native Python Imports
from typing import List, Dict, Any

class ClassQueryGenerator:
    def __init__(self,
                 list_table_identifiers: List[Dict[str, Any]],
                 database_type: str = None,
                 ):
        """
        Initialize the QueryGenerator with a list of table identifiers.

        Example usage:
        query_generator = ClassQueryGenerator(list_table_identifiers)

        Example input (list_table_identifiers):
        [
            {
                'database': 'fivetran_database',
                'schema': 'fivetran_google_search_console',
                'identifier': 'keyword_page_report',
                ... (other dictionary keys which are ignored)
            },
            ... (other dictionaries of table identifiers)
        ]
        """
        self.list_table_identifiers = list_table_identifiers
        self.database_type = database_type

    def _cross_database_random_function(self) -> str:
        """
        Return the appropriate random function for the database type.
        """
        if self.database_type == 'snowflake':
            return 'random()'
        elif self.database_type == 'bigquery':
            return 'rand()'
        else:
            raise ValueError(f"Invalid database type: {self.database_type}")

    def _cross_database_identifier_wrapper(self) -> str:
        """
        Return the appropriate identifier wrapper for the database type.
        """
        if self.database_type == 'snowflake':
            return ''
        elif self.database_type == 'bigquery':
            return '`'
        else:
            raise ValueError(f"Invalid database type: {self.database_type}")
        
    def _cross_dataase_identifier_string_converter_for_query(self, input_string: str) -> str:
        """
        Converts the string of a table identifier into the appropriate format for the database type.

        * Converts the case of an input string (snowflake: uppercase, bigquery: no change)
        * Wraps the string in the appropriate identifier wrapper (snowflake: double quotes, bigquery: no change)

        Arguments: the string to convert

        Example usage:
        converted_string = query_generator._cross_dataase_case_converter('order')

        Example output (if database_type is snowflake)
        '"ORDER"'

        Example output (if database_type is bigquery)
        'order'
        """

        if self.database_type == 'snowflake':
            return f'"{input_string.upper()}"'
        elif self.database_type == 'bigquery':
            return input_string
        else:
            raise ValueError(f"Invalid database type: {self.database_type}")

    def generate_queries(self, row_number_limit: float = 10000) -> Dict[str, str]:
        """
        Generate SQL queries to select a random subset of each table and add to the list_table_identifiers dictionary.
        
        Arguments: the number of rows to limit the query to (default 10k)

        Example usage:
        sample_queries: Dict[str, str] = query_generator.generate_queries()

        Example output:
        [
            {
                'database': 'fivetran_database',
                'schema': 'fivetran_google_search_console',
                'identifier': 'keyword_page_report',
                'query': 'select * from fivetran_database.fivetran_google_search_console.keyword_page_report order by random() limit 10000;',
                ... (other dictionary keys which are ignored)
            },
            ... (other dictionaries of table identifiers)
        ]

        """
        for dict_table_identifier in self.list_table_identifiers:
            database = self._cross_dataase_identifier_string_converter_for_query(dict_table_identifier['database'])
            schema = self._cross_dataase_identifier_string_converter_for_query(dict_table_identifier['schema'])
            identifier = self._cross_dataase_identifier_string_converter_for_query(dict_table_identifier['identifier'])
            # Wrap table identifier in double quotes to avoid breaking they are reserved keywords e.g. 'order'
            query = f'select * from {self._cross_database_identifier_wrapper()}{database}.{schema}.{identifier}{self._cross_database_identifier_wrapper()} order by {self._cross_database_random_function()} limit {row_number_limit};'
            dict_table_identifier['query'] = query

        return self.list_table_identifiers