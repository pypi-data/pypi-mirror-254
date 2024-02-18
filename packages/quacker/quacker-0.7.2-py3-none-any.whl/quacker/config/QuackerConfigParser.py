import yaml
import os

class ClassQuackerConfigParser:
    """
    A class to parse a configuration YAML file and return a dictionary of its values.
    """
    def __init__(self, config_directory):
        """
        Initialize the parser with the directory where quacker_config.yml is located.
        """
        self.config_directory = config_directory
        self.config_file_path = os.path.join(config_directory, 'quacker_config.yml')

    def _read_config(self):
        """
        Read the YAML file and return a dictionary with all non-empty values.

        Example output:

        {
            'models_to_ignore': [
                'stg_shopify__customers',
                'int_core__customers'
            ],  
            'other_config': [
                'some_value',
            ]
        }
            """
        try:
            with open(self.config_file_path, 'r') as file:
                # Load the YAML content, ignoring empty values
                config_content = yaml.safe_load(file)
                # Filter out empty values if necessary
                config_content = {k: v for k, v in config_content.items() if v}
                return config_content
        except FileNotFoundError:
            print(f"The file {self.config_file_path} was not found.")
            return {}
        except yaml.YAMLError as e:
            print(f"Error parsing the YAML file: {e}")
            return {}
        
    def get_models_to_ignore(self):
        """
        Read the YAML file and return a list of models to ignore.

        Example output:

        [
            'stg_shopify__customers',
            'int_core__customers'
        ]
        """
        config_content = self._read_config()
        return config_content.get('models_to_ignore', [])
    
    def get_main_duckdb_database_name(self):
        """
        Read the YAML file and return the name of the main DuckDB database.
        """
        config_content = self._read_config()
        return config_content.get('main_duckdb_database_name', 'main_duckdb_database')
    
    def get_row_limit(self):
        """
        Read the YAML file and return the row limit which is used to limit the number of rows returned from the warehouse.

        Default value is 1000.
        """
        config_content = self._read_config()
        return config_content.get('row_limit', 1000)
    
    def get_duckdb_folder_name(self):
        """
        Read the YAML file and return the name of the folder where the DuckDB databases are stored.

        Default value is 'data_duckdb'.
        """
        config_content = self._read_config()
        return config_content.get('duckdb_folder_name', 'data_duckdb')