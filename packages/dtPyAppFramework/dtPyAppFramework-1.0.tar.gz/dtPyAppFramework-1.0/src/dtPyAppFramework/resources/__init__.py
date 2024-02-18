from ..paths import ApplicationPaths
from ..decorators import singleton

import os
import logging


@singleton()
class ResourceManager(object):
    """
    Singleton class for managing resources within the application.

    Attributes:
        application_paths (ApplicationPaths): Object managing application paths.
        resource_paths (list): List of paths where resources can be located.
    """

    def __init__(self, application_paths=None) -> None:
        """
        Initialize ResourceManager.

        Args:
            application_paths (ApplicationPaths, optional): Object managing application paths.
        """
        super().__init__()
        self.application_paths = application_paths
        if not self.application_paths:
            self.application_paths = ApplicationPaths()
        self.resource_paths = self.__load_default_paths__()

    def __load_default_paths__(self):
        """
        Load default resource paths.

        Returns:
            list: List of default resource paths.
        """
        return [os.path.join(self.application_paths.usr_data_root_path, "resources"),
                os.path.join(self.application_paths.app_data_root_path, "resources"),
                os.path.join(os.getcwd(), "resources")]

    def add_resource_path(self, path):
        """
        Add a custom resource path.

        Args:
            path (str): Path to be added to the resource paths.
        """
        self.resource_paths.append(path)

    def remove_resource_path(self, path):
        """
        Remove a custom resource path.

        Args:
            path (str): Path to be removed from the resource paths.
        """
        self.resource_paths.remove(path)

    def get_resource_path(self, resource):
        """
        Get the full path to a resource.

        Args:
            resource (str): Name of the resource.

        Returns:
            str: Full path to the resource, or None if not found.
        """
        for path in self.resource_paths:
            if os.path.exists(os.path.join(path, resource)):
                logging.info(f'Returning resource from: "{os.path.join(path, resource)}"')
                return os.path.join(path, resource)

        logging.error(f'Resource: "{resource}" could not be found')
        return None
