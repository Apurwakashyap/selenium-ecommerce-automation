from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.logger import logger


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def login(self, username, password):
        """Login using the provided credentials."""

        logger.info("Entering username")
        self.enter_text(self.USERNAME, username)

        logger.info("Entering password")
        self.enter_text(self.PASSWORD, password)

        logger.info("Clicking Login button")
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        """Return login error message."""
        return self.get_text(self.ERROR_MESSAGE)