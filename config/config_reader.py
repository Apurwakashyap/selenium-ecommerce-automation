import configparser
import os


class ConfigReader:
    def __init__(self):
        config = configparser.ConfigParser()

        config_path = os.path.join(
            os.path.dirname(__file__),
            "config.ini"
        )

        config.read(config_path)

        self.config = config

    @property
    def base_url(self):
        return self.config.get(
            "application",
            "base_url"
        )

    @property
    def default_browser(self):
        return self.config.get(
            "browser",
            "default_browser"
        )

    @property
    def explicit_wait(self):
        return self.config.getint(
            "timeouts",
            "explicit_wait"
        )

    @property
    def username(self):
        return self.config.get(
            "test_data",
            "username"
        )

    @property
    def password(self):
        return self.config.get(
            "test_data",
            "password"
        )


config = ConfigReader()