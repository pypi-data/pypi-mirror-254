# Native Python Imports
import json
import os
import subprocess
import sys

class ClassDbtManifestParser:
    """
    A class for parsing dbt's manifest.json file to extract dbt source information.
    This class runs 'dbt compile' to ensure the manifest.json is up-to-date.

    Example usage:
    dbt_manifest_parser = ClassDbtManifestParser()
    # or (non-defailt paths): dbt_manifest_parser = ClassDbtManifestParser(project_dir='path/to/dbt/project', manifest_path='path/to/manifest.json')
    """

    def __init__(self,
                 project_dir: str = None,
                 profiles_dir: str = None,
                 manifest_dir: str = None,
                 target_name_compile: str = None,
                 duckdb_folder_name: str = None,
                 list_models_to_ignore: list = None,
                 database_type: str = None,
                 ):
        """
        Initialize the DbtManifestParser with the dbt project directory and the path to manifest.json.
        Uses default paths relative to this script's location if none provided.
        """
        print("preparing to compile dbt project and parse manifest.json")

        script_dir = os.getcwd()
        self.project_dir = project_dir or os.path.join(script_dir)
        self.profiles_dir = profiles_dir
        self.manifest_dir = manifest_dir or os.path.join(self.project_dir, 'target')
        self.manifest_path = os.path.join(self.manifest_dir, 'manifest.json')
        self.target_name_compile = target_name_compile
        self.duckdb_folder_name = duckdb_folder_name
        self.list_models_to_ignore = list_models_to_ignore or []
        self.database_type = database_type
        self._ensure_duckdb_folder_exists()
        self._run_dbt_compile()
        self.dict_manifest = self._load_manifest()

        print(f"project_dir: {self.project_dir}")
        print(f"manifest_path: {self.manifest_path}")

    def _ensure_duckdb_folder_exists(self):
        """
        TODO move this to DuckDBConnector.py?
        Ensure that the duckdb folder exists. If it doesn't, create it.
        """
        if not os.path.exists(self.duckdb_folder_name):
            print(f"DuckDB folder '{self.duckdb_folder_name}' not found. Creating it.")
            os.makedirs(self.duckdb_folder_name)
        else:
            print(f"DuckDB folder '{self.duckdb_folder_name}' already exists.")

    def _run_dbt_compile(self):
        """
        Run 'dbt compile' command in the dbt project directory.
        """

        try:
            command = ['dbt', 'compile']

            # Add the target name to the command if specified
            if self.target_name_compile:
                command += ['--target', self.target_name_compile]

            # Add the profiles dir to the command if specified
            if self.profiles_dir:
                command += ['--profiles-dir', self.profiles_dir]

            print(f"Running {' '.join(command)} in location of {self.project_dir}/dbt_project.yml")
            subprocess.run(command, cwd=self.project_dir, check=True)
            print("dbt compile completed successfully")

        except subprocess.CalledProcessError as e:
            print(f"Error running dbt compile: {e}")
            print(f"This can occur if you don't have dbt-{self.database_type} installed. Try running 'pip install dbt-{self.database_type}', then run your Quacker command again")
            sys.exit(1)  # Exit the program with a non-zero exit code to indicate an error

        except FileNotFoundError as e:
            print(f"Error running dbt compile: {e}")
            print(f"This can occur if you don't have dbt-{self.database_type} installed. Try running 'pip install dbt-{self.database_type}', then run your Quacker command again")
            sys.exit(1)  # Exit the program with a non-zero exit code to indicate an error

    def _load_manifest(self) -> dict:
        """
        Load and return the dbt manifest.json file as a dictionary.
        """
        try:
            print(f"Loading dbt manifest file from {self.manifest_path}")
            with open(self.manifest_path, 'r') as file:
                manifest_json = json.load(file)
                print("Manifest file loaded and parsed successfully")
                return manifest_json
        except FileNotFoundError as e:
            print(f"Manifest file not found: {e}")
            raise
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            raise
    
    def _get_sources(self) -> list:
        """
        Extract identifiers of a list of dbt sources from the manifest.

        example output:
        [
            {
                'identifier_type': 'source',
                'source_name': 'google_search_console',
                'database': 'fivetran_database',
                'schema': 'fivetran_google_search_console',
                'identifier': 'keyword_page_report'
            }
        ]
        """
        sources = []
        
        # Extract sources from the top-level 'sources' key in the manifest
        for _, source_node in self.dict_manifest.get('sources', {}).items():
            # We are assuming that 'source_node' is a dictionary containing the source information
            source = {
                'identifier_type': 'source',
                'source_name': source_node.get('source_name', ''),
                'database': source_node.get('database', ''),
                'schema': source_node.get('schema', ''),
                'identifier': source_node.get('identifier', '')
            }
            sources.append(source)

        return sources
    
    def _get_models_to_ignore(self) -> list:
        """
        Extract identifiers of a list of dbt models to ignore from the manifest.

        example output:
        [
            {
                'identifier_type': 'model_to_ignore',
                'database': 'AMIR_DEMO',
                'schema': 'amir_analytics_demo_integration',
                'identifier': 'int_core__customers'
            }
        ]
        """
        list_tables_to_ignore_identifiers = []

        # Extract models from the 'nodes' key in the manifest
        for key, model_node in self.dict_manifest.get('nodes', {}).items():
            # Check if any suffix from self.list_models_to_ignore matches the end of the key
            if any(key.endswith(suffix) for suffix in self.list_models_to_ignore):
                model_info = {
                    'identifier_type': 'model_to_ignore',
                    'database': model_node.get('database', ''),
                    'schema': model_node.get('schema', ''),
                    'identifier': model_node.get('name', ''),
                }
                list_tables_to_ignore_identifiers.append(model_info)

        return list_tables_to_ignore_identifiers
    
    def get_identifiers_of_all_tables_to_replicate(self) -> list:
        """
        Return a list of all table identifiers in the dbt project.

        """
        list_identifiers_of_all_tables_to_replicate = []
        list_identifiers_of_all_tables_to_replicate += self._get_sources()
        list_identifiers_of_all_tables_to_replicate += self._get_models_to_ignore()

        return list_identifiers_of_all_tables_to_replicate