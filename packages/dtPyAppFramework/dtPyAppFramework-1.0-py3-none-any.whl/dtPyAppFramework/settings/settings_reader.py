import json
import yaml
import logging
import os

class SettingsReader(dict):
    """
    A class for reading settings from a YAML file and accessing them using dot notation.

    Attributes:
        path (str): Path to the directory containing the settings YAML file.
        priority (int): Priority of the settings reader.
        settings_file (str): Full path to the settings YAML file.
    """

    def __init__(self, path: str, priority: int) -> None:
        """
        Initialize the SettingsReader.

        Args:
            path (str): Path to the directory containing the settings YAML file.
            priority (int): Priority of the settings reader.
        """
        self.priority = priority
        self.settings_file = os.path.join(path, "config.yaml")

        if os.path.exists(self.settings_file):
            self.load_yaml_file()

        super().__init__()

    def load_yaml_file(self):
        """
        Load settings from the YAML file and update the dictionary.
        """
        with open(self.settings_file, 'r', encoding='UTF-8') as file:
            self.update(yaml.safe_load(file))

    def clear(self) -> None:
        """
        Clear method not implemented.
        """
        raise NotImplementedError

    def popitem(self):
        """
        popitem method not implemented.
        """
        raise NotImplementedError

    def __setitem__(self, k, v) -> None:
        """
        __setitem__ method not implemented.
        """
        raise NotImplementedError

    def pop(self, __key):
        """
        pop method not implemented.
        """
        raise NotImplementedError

    def __getitem__(self, key):
        """
        Get item from the dictionary using dot notation.

        Args:
            key (str): Key in dot notation.

        Returns:
            The value associated with the key.
        """
        keys = key.split('.')
        if len(keys) == 1:
            return dict.__getitem__(self, key)
        else:
            data = self.copy()
            for key in keys:
                if key in data:
                    data = data[key]
                else:
                    return None
            return data
