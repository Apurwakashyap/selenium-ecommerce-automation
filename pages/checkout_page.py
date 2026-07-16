from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.waits import WaitUtils

class CheckoutPage(BasePage):

    CHECKOUT_BUTTON = (
        By.ID,
        "checkout"
    )

    FIRST_NAME = (
        By.ID,
        "first-name"
    )

    LAST_NAME = (
        By.ID,
        "last-name"
    )

    ZIP_CODE = (
        By.ID,
        "postal-code"
    )

    CONTINUE_BUTTON = (
        By.ID,
        "continue"
    )

    FINISH_BUTTON = (
        By.ID,
        "finish"
    )

    SUCCESS_MESSAGE = (
        By.CLASS_NAME,
        "complete-header"
    )

    def start_checkout(self):

        self.click(
            self.CHECKOUT_BUTTON
        )

    def enter_customer_details(
            self,
            first_name,
            last_name,
            zip_code):

        self.enter_text(
            self.FIRST_NAME,
            first_name
        )

        self.enter_text(
            self.LAST_NAME,
            last_name
        )

        self.enter_text(
            self.ZIP_CODE,
            zip_code
        )

    def continue_checkout(self):
        self.click(self.CONTINUE_BUTTON)
        

    def finish_order(self):

        self.click(
            self.FINISH_BUTTON
        )

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)