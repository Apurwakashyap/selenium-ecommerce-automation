import configparser
import os
from pathlib import Path


class ConfigReader:
    """Read framework settings, allowing environment variables to override config.ini."""

    def __init__(self):
        self.config = configparser.ConfigParser()
        config_path = Path(__file__).resolve().parent / "config.ini"

        loaded_files = self.config.read(config_path)
        if not loaded_files:
            raise FileNotFoundError(f"Configuration file not found: {config_path}")

    @property
    def base_url(self):
        return os.getenv(
            "BASE_URL",
            self.config.get("application", "base_url"),
        )

    @property
    def default_browser(self):
        return os.getenv(
            "BROWSER",
            self.config.get("browser", "default_browser", fallback="chrome"),
        )

    @property
    def explicit_wait(self):
        return self.config.getint("timeouts", "explicit_wait", fallback=10)

    @property
    def page_load_timeout(self):
        return self.config.getint("timeouts", "page_load_timeout", fallback=30)

    @property
    def username(self):
        return os.getenv(
            "APP_USERNAME",
            self.config.get("test_data", "username"),
        )

    @property
    def password(self):
        return os.getenv(
            "APP_PASSWORD",
            self.config.get("test_data", "password"),
        )


config = ConfigReader()
