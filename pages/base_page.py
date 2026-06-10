from utils.waits import wait_for_element


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, locator, text):

        wait_for_element(
            self.driver,
            locator
        ).send_keys(text)

    def click(self, locator):

        wait_for_element(
            self.driver,
            locator
        ).click()