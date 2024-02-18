# Native Python Imports
import os
import re
from pathlib import Path

# Third-Party Imports
import yaml

class ClassDbtProfilesParser:
    '''
    Find and parse the dbt profiles.yml file to extract connection details.

    dbt docs detailing where a profiles.yml file can be found:
    https://docs.getdbt.com/docs/core/connect-data-platform/connection-profiles#advanced-customizing-a-profile-directory
    '''

    def __init__(self, profiles_dir=None):
        '''
        Initializes the DbtProfilesParser instance.

        Searches for the profiles.yml file in the specified locations and sets
        the profiles_file_path attribute.

        Args:
            profiles_dir (str, optional): The directory path specified
            by the --profiles-dir option. Defaults to None.
        '''
        self.profiles_file_path = self._find_profiles_file(profiles_dir)

    def _find_profiles_file(self, profiles_dir):
        '''
        Searches for the profiles.yml file in the following order of precedence:
        1. --profiles-dir option
        2. DBT_PROFILES_DIR environment variable
        3. Current working directory
        4. ~/.dbt/ directory

        Args:
            profiles_dir (str): The directory path specified by the
            --profiles-dir option.

        Returns:
            Path: The path to the found profiles.yml file.

        Raises:
            FileNotFoundError: If profiles.yml is not found in any of the
            known locations.
        '''
        # Check for profiles.yml file in the specified locations
        if profiles_dir:
            profiles_path = Path(profiles_dir) / 'profiles.yml'
            if profiles_path.is_file():
                print(f"using argument --profiles-dir to find profile at: {profiles_path}")
                return profiles_path

        dbt_profiles_env = os.getenv('DBT_PROFILES_DIR')
        if dbt_profiles_env:
            profiles_path = Path(dbt_profiles_env) / 'profiles.yml'
            if profiles_path.is_file():
                print(f"using environment variable DBT_PROFILES_DIR to find profile at: {profiles_path}")
                return profiles_path

        cwd_profiles_path = Path.cwd() / 'profiles.yml'
        if cwd_profiles_path.is_file():
            print(f"using current working directory to find profile at: {cwd_profiles_path}")
            return cwd_profiles_path

        home_profiles_path = Path.home() / '.dbt' / 'profiles.yml'
        if home_profiles_path.is_file():
            print(f"using ~/.dbt/ directory to find profile at: {home_profiles_path}")
            return home_profiles_path

        raise FileNotFoundError("profiles.yml file not found in any known locations.")

    def _load_profiles(self):
        '''
        Loads the content of the profiles.yml file.

        Returns:
            dict: The content of the profiles.yml file, or None if the file
            cannot be found or loaded.
        '''
        try:
            with open(self.profiles_file_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print(f"Profiles file not found at {self.profiles_file_path}")
            return None

    def _extract_env_var_or_return_value(self, value):
        """
        Checks if the given value is a Jinja templated environment variable, and extracts it.
        If it's not an environment variable, returns the value as is. Raises an error
        if the environment variable is required but not set or empty.

        Args:
            value (str): A possible Jinja templated string containing an environment variable.

        Returns:
            str: The value of the environment variable or the original string.

        Raises:
            ValueError: If an environment variable is required but not provided.
        """

        if isinstance(value, str):
            match = re.search(r"\{\{ env_var\('(.+?)'\) \}\}", value)
            if match:
                env_var_name = match.group(1)
                env_var_value = os.getenv(env_var_name)
                if env_var_value is None or env_var_value == "":
                    raise ValueError(f"Environment variable '{env_var_name}' required but not provided.")
                return env_var_value
        return value
    
    def get_default_target_name(self, profile_name):
        """
        Extracts the name of the default target for a specified profile.

        Args:
            profile_name (str): The name of the profile to extract the default target for.

        Returns:
            str: The name of the default target, or None if the profile cannot be found.
        """
        print(f"Extracting default target name for profile '{profile_name}'")

        profiles = self._load_profiles()
        if profiles and profile_name in profiles:
            default_target_name = profiles[profile_name].get('target')
            print(f"default target name found: '{default_target_name}'")
            return default_target_name
        return None
    
    def _return_error_if_target_not_found(self, profile_name, target_name):
        """
        Raises an error if the specified target cannot be found in the specified profile.

        If error is raised, program execution will stop.

        Args:
            profile_name (str): The name of the profile to extract the target from.
            target_name (str): The name of the target to extract.
        
        Raises:
            ValueError: If the target cannot be found.
        """
        profiles = self._load_profiles()
        if profiles and profile_name in profiles:
            if target_name not in profiles[profile_name].get('outputs', {}):
                raise ValueError(f"Target '{target_name}' not found in profile '{profile_name}'. Please check your profiles.yml file.")
        else:
            raise ValueError(f"Profile '{profile_name}' not found. Please check your profiles.yml file.")
    
    def get_database_type(self, profile_name, target_name):
        """
        Extracts the type of the database for a specified profile and target.
        It handles both hardcoded values and values set via environment
        variables.

        Args:
            profile_name (str): The name of the profile to extract the database type for.
            target_name (str, optional): The target within the profile.

        Returns:
            str: The database type, or None if the profile or target cannot be found.

        Raises:
            ValueError: If the database type is required but not provided.
        """
        print(f"Extracting database type for profile '{profile_name}' and target '{target_name}'")

        self._return_error_if_target_not_found(profile_name, target_name)

        profiles = self._load_profiles()
        if profiles and profile_name in profiles:
            target = profiles[profile_name].get('outputs', {}).get(target_name, {})
            database_type = target.get('type')
            if database_type is None or database_type == "":
                raise ValueError(f"Database type required but not provided for profile '{profile_name}' and target '{target_name}'")
            return database_type
        return None


    def _get_snowflake_connection(self, profile_name, target_name):
        """
        Extracts the Snowflake connection details from the profiles.yml file
        for a specified profile and target. It handles both hardcoded values
        and values set via environment variables.

        Args:
            profile_name (str): The name of the profile to extract details for.
            target_name (str, optional): The target within the profile.

        Returns:
            dict: A dictionary containing the Snowflake connection details, or
            None if the profile or target cannot be found.

        Raises:
            ValueError: If any required connection details are missing or empty.
        """
        print(f"Extracting Snowflake connection details for profile '{profile_name}' and target '{target_name}'")

        profiles = self._load_profiles()
        if profiles and profile_name in profiles:
            target = profiles[profile_name].get('outputs', {}).get(target_name, {})
            if target.get('type') == 'snowflake':
                return {
                    'account': self._extract_env_var_or_return_value(target.get('account', '')),
                    'user': self._extract_env_var_or_return_value(target.get('user', '')),
                    'password': self._extract_env_var_or_return_value(target.get('password', '')),
                    'role': self._extract_env_var_or_return_value(target.get('role', '')),
                    'warehouse': self._extract_env_var_or_return_value(target.get('warehouse', '')),
                    'database': self._extract_env_var_or_return_value(target.get('database', '')),
                    'schema': self._extract_env_var_or_return_value(target.get('schema', '')),
                }
        return None
    
    def _get_bigquery_connection(self, profile_name, target_name):
        """
        Extracts the BigQuery connection details from the profiles.yml file
        for a specified profile and target. It handles both hardcoded values
        and values set via environment variables.

        Args:
            profile_name (str): The name of the profile to extract details for.
            target_name (str, optional): The target within the profile.

        Returns:
            dict: A dictionary containing the BigQuery connection details, or
            None if the profile or target cannot be found.

        Raises:
            ValueError: If any required connection details are missing or empty.
        """
        print(f"Extracting BigQuery connection details for profile '{profile_name}' and target '{target_name}'")

        profiles = self._load_profiles()
        if profiles and profile_name in profiles:
            target = profiles[profile_name].get('outputs', {}).get(target_name, {})
            if target.get('type') == 'bigquery':
                return {
                    'project_id': self._extract_env_var_or_return_value(target.get('project', '')),
                    'dataset': self._extract_env_var_or_return_value(target.get('dataset', '')),
                    'keyfile_path': self._extract_env_var_or_return_value(target.get('keyfile', '')),
                }
        return None
    
    def get_warehouse_connection(self, profile_name, target_name, database_type):
        """
        Dispatches to the appropriate method to extract the connection details
        for a specified profile and target.

        Args:
            profile_name (str): The name of the profile to extract details for.
            target_name (str, optional): The target within the profile.
            database_type (str): The type of the database.

        """
        if database_type == 'snowflake':
            return self._get_snowflake_connection(profile_name, target_name)
        elif database_type == 'bigquery':
            return self._get_bigquery_connection(profile_name, target_name)
        else:
            return None