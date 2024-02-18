"""
This is the main entry point for the Quacker CLI tool.
Run this file to start the command-line interface.
"""

# Native Python Imports
import argparse

# Local Imports
from .config import (
    QuackerConfigParser,
)
from .databases import (
    BigQueryConnector,
    DuckDBConnector,
    QueryGenerator,
    SnowflakeConnector,
)
from .dbt import (
    DbtProfilesParser,
    DbtProjectParser,
    DbtManifestParser,
)

def main():
    """
    Main entry point for the Quacker CLI tool.

    Orchestrates the different components of the tool.
    """
    # Create the parser
    parser = argparse.ArgumentParser(description='Quacker CLI tool. Start quacking!')

    # Add subparsers for different commands
    subparsers = parser.add_subparsers( dest='command', help='Available commands' )

    # Subparser for 'sync' command
    sync_subparser = subparsers.add_parser('sync',
                                           help="""Syncs data from all dbt sources into duckdb databases.
                                           Example use: quack sync --project-dir poc_duckdb_for_local_dev --manifest-dir poc_duckdb_for_local_dev/target
                                           Example shorthand use: quack sync -p poc_duckdb_for_local_dev -m poc_duckdb_for_local_dev/target""")

    # Optional flags
    sync_subparser.add_argument('-p', '--project-dir', type=str, default='.', 
                                help='Relative path to the folder where dbt_project.yml is located. Defaults to the current directory. Example use: --project-dir poc_duckdb_for_local_dev')
    sync_subparser.add_argument('-pf', '--profiles-dir', type=str, 
                                help='FULL path to the folder where profiles.yml is located. Defaults to None. Example use: --profiles-dir /Users/username/path/to/dbt/profiles')
    sync_subparser.add_argument('-m', '--manifest-dir', type=str, default='target', 
                            help='Relative path to the folder where manifest.json is located. Defaults to the "target" folder in the current directory. Example use: --manifest-dir poc_duckdb_for_local_dev/target')
    sync_subparser.add_argument('-c', '--compile-target', type=str,
                            help="The dbt target name to sync the data from. It's also the target Quacker uses when running 'dbt compile' before extracting identifiers. Defaults to your default dbt profile. Example use: --compile-target dev_snowflake")

    # Parse the CLI input
    args = parser.parse_args()

    argument_project_dir = args.project_dir
    argument_profiles_dir = args.profiles_dir
    argument_manifest_dir = args.manifest_dir
    argument_target_name_compile = args.compile_target

    print(f"project-dir passed in argument or default: {argument_project_dir}")
    print(f"profiles-dir passed in argument or default: {argument_profiles_dir}")
    print(f"manifest-dir passed in argument or default: {argument_manifest_dir}")
    print(f"compile-target passed in argument or default: {argument_target_name_compile}")

    # Parse dbt_project.yml to get project name
    dbt_project_parser = DbtProjectParser.ClassDbtProjectParser(project_dir=argument_project_dir)
    profile_name = dbt_project_parser.get_profile_name()
    print(f"dbt profile name to get connection details from: '{profile_name}'")
    
    # Get default target name from profiles.yml if compile_target is not passed in as an argument
    dbt_profiles_parser = DbtProfilesParser.ClassDbtProfilesParser(profiles_dir=argument_profiles_dir)
    if not argument_target_name_compile:
        target_name_compile = dbt_profiles_parser.get_default_target_name(profile_name=profile_name)
        print(f"since no --compile-target was passed in as an argument, using default target name found in profile '{profile_name}': '{target_name_compile}'")
    else:
        target_name_compile = argument_target_name_compile

    # Read quacker_config.yml and extract configurations
    class_config_parser = QuackerConfigParser.ClassQuackerConfigParser(argument_project_dir)
    list_models_to_ignore = class_config_parser.get_models_to_ignore()
    main_duckdb_database_name = class_config_parser.get_main_duckdb_database_name()
    row_limit_warehouse_query = class_config_parser.get_row_limit()
    duckdb_folder_name = class_config_parser.get_duckdb_folder_name()


    # Process based on the command
    if args.command == 'sync':

        # Parse profiles.yml to get database type
        database_type = dbt_profiles_parser.get_database_type(
            profile_name=profile_name,
            target_name=target_name_compile,
            )

        # Parse profiles.yml to get warehouse connection details
        warehouse_connection_details = dbt_profiles_parser.get_warehouse_connection(
            profile_name = profile_name,
            target_name = target_name_compile,
            database_type = database_type,
            )

        # Create instances of connectors to avoid doing this over and over again during the table loop below
        duckdb_connector = DuckDBConnector.ClassDuckDBConnector(duckdb_folder_name)
        if database_type == 'snowflake':
            warehouse_connector = SnowflakeConnector.ClassSnowflakeConnector(**warehouse_connection_details)
        elif database_type == 'bigquery':
            warehouse_connector = BigQueryConnector.ClassBigQueryConnector(**warehouse_connection_details)
        else:
            print(f"Unsupported database type: {database_type}")
            return
    
        if not warehouse_connection_details:
            print("Error fetching warehouse connection details. Please check your profiles.yml configuration.")
            return

        # Parse dbt tables to replicate from manifest.json
        dbt_manifest_parser = DbtManifestParser.ClassDbtManifestParser(
            project_dir = argument_project_dir,
            profiles_dir = argument_profiles_dir,
            manifest_dir = argument_manifest_dir,
            target_name_compile = target_name_compile,
            duckdb_folder_name = duckdb_folder_name,
            list_models_to_ignore = list_models_to_ignore,
            database_type = database_type,
        )
        list_identifiers_of_all_tables_to_replicate = dbt_manifest_parser.get_identifiers_of_all_tables_to_replicate()

        # Generate SQL queries
        query_generator = QueryGenerator.ClassQueryGenerator(
            list_identifiers_of_all_tables_to_replicate,
            database_type=database_type,
            )
        list_table_identifiers_with_sample_queries = query_generator.generate_queries(row_number_limit = row_limit_warehouse_query)
        print(f"Generated {len(list_table_identifiers_with_sample_queries)} queries to execute against warehouse:")
        for table in list_table_identifiers_with_sample_queries:
            print(table["query"])

        # Execute queries against warehouse and load into DuckDB
        for dict_table_identifier in list_table_identifiers_with_sample_queries:
            database_name = dict_table_identifier['database']
            schema_name = dict_table_identifier['schema']
            table_name = dict_table_identifier["identifier"]
            identifier_type = dict_table_identifier['identifier_type']
            query = dict_table_identifier['query']

            # Fetch data from the warehouse as a DataFrame
            dataframe = warehouse_connector.query_to_dataframe(query=query)

            # Determine database name to load data into
            # If the table is a model to ignore, load it into the main duckdb database instead of the database from the manifest
            if identifier_type == 'model_to_ignore':
                database_name_to_load_into = main_duckdb_database_name
            else:
                database_name_to_load_into = database_name

            # Load data into DuckDB
            duckdb_connector.load_dataframe(
                dataframe=dataframe, 
                database_name=database_name_to_load_into, 
                schema_name=schema_name, 
                table_name=table_name
            )
            print(f"Data for {schema_name}.{table_name} loaded into DuckDB file {database_name_to_load_into}")

    else:
        print( 'Invalid command' )


if __name__ == "__main__":
    main()