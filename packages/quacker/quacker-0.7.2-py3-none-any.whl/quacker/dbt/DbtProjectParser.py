# Third Party Imports
import yaml

class ClassDbtProjectParser:
    '''
    This class is responsible for parsing the dbt_project.yml file

    '''
    def __init__(self, project_dir):
        '''
        Initializes the DbtProjectParser object. The dir is assumed accurate.

        '''
        self.project_dir = project_dir
        self.project_file_path = project_dir + '/dbt_project.yml'
        self.project_file_content = self._load_project_file()

    def _load_project_file(self):
        '''
        Loads the content of the dbt_project.yml file.

        Returns:
            dict: The content of the dbt_project.yml file.
        '''
        with open(self.project_file_path, 'r') as project_file:
            return yaml.safe_load(project_file)
        
    def get_profile_name(self):
        '''
        Returns the name of the profile specified in the dbt_project.yml file.

        Returns:
            str: The name of the profile specified in the dbt_project.yml file.
        '''
        return self.project_file_content['profile']