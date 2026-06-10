from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.waits import wait_for_element


class LoginPage(BasePage):

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "h3[data-test='error']"
    )

    def login(self, username, password):

        self.enter_text(
            self.USERNAME,
            username
        )

        self.enter_text(
            self.PASSWORD,
            password
        )

        self.click(
            self.LOGIN_BUTTON
        )

    def get_error_message(self):

        return wait_for_element(
            self.driver,
            self.ERROR_MESSAGE
        ).text