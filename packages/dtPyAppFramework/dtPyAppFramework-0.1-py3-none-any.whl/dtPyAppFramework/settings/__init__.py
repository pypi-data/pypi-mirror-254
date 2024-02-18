from ..paths import ApplicationPaths
from ..decorators import singleton
from .settings_reader import SettingsReader
from .secrets import SecretsManager

import os


@singleton()
class Settings(dict):
    """
    Singleton class for managing application settings.

    Attributes:
        application_paths (ApplicationPaths): Object managing application paths.
        app_short_name (str): Short name of the application.
        settings_readers (list): List of settings readers.
        persistent_settings_stores (list): List of persistent settings stores.
        secret_manager (SecretsManager): Manager for handling secrets.
    """

    def __init__(self, application_paths=None, app_short_name=None) -> None:
        """
        Initialize Settings.

        Args:
            application_paths (ApplicationPaths, optional): Object managing application paths.
            app_short_name (str, optional): Short name of the application.
        """
        self.application_paths = application_paths
        self.app_short_name = app_short_name
        if not self.application_paths:
            self.application_paths = ApplicationPaths()

        self.settings_readers = []
        self.persistent_settings_stores = []
        self.secret_manager = SecretsManager(application_paths=self.application_paths, application_settings=self)

        super().__init__()

    def init_settings_readers(self):
        """
        Initialize settings readers.
        """
        self.settings_readers.append(SettingsReader(os.path.join(os.getcwd(), "config"), 300))
        self.settings_readers.append(SettingsReader(self.application_paths.app_data_root_path, 200))
        self.settings_readers.append(SettingsReader(self.application_paths.usr_data_root_path, 100))
        self.settings_readers.sort(key=lambda x: x.priority)

    def get_requests_tor_proxy(self) -> dict:
        """
        Gets TOR Proxy configuration in a format compatible with Requests.

        Returns:
            dict: Dictionary of HTTP and HTTPS configuration for TOR Proxy.
        """
        proxy = self.get('settings.proxies.tor_proxy', '127.0.0.1:9150')
        return {"http": 'socks5h://' + proxy,
                "https": 'socks5h://' + proxy}

    def get_selenium_tor_proxy(self) -> str:
        """
        Gets TOR Proxy configuration in a format compatible with Selenium.

        Returns:
            str: String value for proxy configuration.
        """
        proxy = self.get('settings.proxies.tor_proxy', '127.0.0.1:9150')
        return '--proxy-server=socks5://' + proxy

    def get(self, key, default=None):
        """
        Get the value of a setting.

        Args:
            key (str): Key of the setting.
            default: Default value if the setting is not found.

        Returns:
            Value of the setting or the default value.
        """
        try:
            value = self.__getitem__(key)
            if isinstance(value, str) and str(value).startswith('ENV/'):
                return os.getenv(str(value).replace('ENV/', '').strip(), value)
            if isinstance(value, str) and str(value).startswith('SEC/'):
                return self.secret_manager.get_secret(str(value).replace('SEC/', '').strip(), default)
            if isinstance(value, str) and str(value).startswith('<USR>'):
                return str(value).replace('<USR>', self.application_paths.usr_data_root_path).strip()
            if isinstance(value, str) and str(value).startswith('<APP>'):
                return str(value).replace('<APP>', self.application_paths.app_data_root_path).strip()
            if isinstance(value, str) and str(value).startswith('AWS_Secret#'):
                return self.secret_manager.get_secret(str(value).strip(), default)
            if not value:
                return default
            return value
        except KeyError:
            return default

    def set(self, key, value, store_name=None):
        """
        Set the value of a setting.

        Args:
            key (str): Key of the setting.
            value: Value to set.
            store_name (str, optional): Name of the store for persistent settings.
        """
        self.secret_manager.set_secret(key, value, store_name)

    def __getattr__(self, key):
        """
        Get attribute based on key.

        Args:
            key (str): Key of the attribute.

        Returns:
            Value of the attribute.

        Raises:
            AttributeError: If the attribute is not found.
        """
        try:
            return self.__getitem__(key)
        except KeyError:
            raise AttributeError("object has no attribute '%s'" % key)

    def __setitem__(self, key, value):
        """
        Set item in the dictionary.

        Args:
            key (str): Key of the item.
            value: Value to set.
        """
        # If the value of a setting is changed or new setting added,
        # then it will add it to the persistent store and will override any settings in the config YAML.
        return self.set(key=key, value=value)

    def __getitem__(self, key):
        """
        Get item from the dictionary.

        Args:
            key (str): Key of the item.

        Returns:
            Value of the item.
        """
        persistent_value = self.secret_manager.get_secret(key)
        if persistent_value:
            return persistent_value

        value = None
        for reader in self.settings_readers:
            value = reader.__getitem__(key)
            if value:
                break

        return value
