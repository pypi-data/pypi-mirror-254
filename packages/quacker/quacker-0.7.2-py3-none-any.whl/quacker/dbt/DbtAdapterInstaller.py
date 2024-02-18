import subprocess

class ClassDbtAdapterInstaller:
    """
    A class to install dbt adapters using pip.

    Example usage:
    adapter_installer = ClassDbtAdapterInstaller('snowflake')
    adapter_installer.install_adapter()

    """

    def __init__(self, adapter_name):
        """
        Initialize the installer with the name of the dbt adapter.
        """
        self.adapter_name = adapter_name

    def install_adapter(self):
        """
        Install the specified dbt adapter.
        """
        try:
            print(f"Attempting to install dbt-{self.adapter_name}")
            subprocess.run(['pip3', 'install', f'dbt-{self.adapter_name}'], check=True)
            print(f"dbt-{self.adapter_name} installation completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred during installation: {e}")
            raise