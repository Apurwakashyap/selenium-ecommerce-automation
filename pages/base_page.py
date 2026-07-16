import os

from utils.logger import logger  
from utils.waits import WaitUtils
from config.config_reader import config

class BasePage:
    """
    Base class for all page objects.
    Provides reusable browser interaction methods.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver,config.explicit_wait)

    def click(self, locator):
        logger.info(f"Clicking element: {locator}")

        element = self.wait.presence(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        element = self.wait.clickable(locator)

        element.click()



    def enter_text(self, locator, text):
        """Clear the field and enter text."""
        element = self.wait.visibility(locator)
        element.clear()
        element.send_keys(text)
        logger.info(f"Entered text into: {locator}")

    def clear(self, locator):
        """Clear an input field."""
        self.wait.visibility(locator).clear()

    def get_text(self, locator):
        """Return element text."""
        return self.wait.visibility(locator).text

    def is_displayed(self, locator):
        """Return True if element is visible."""
        try:
            return self.wait.visibility(locator).is_displayed()
        except Exception:
            return False

    def scroll_into_view(self, locator):
        """Scroll element into view."""
        element = self.wait.presence(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
            element
        )

    def js_click(self, locator):
        """Click an element using JavaScript."""
        element = self.wait.presence(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def take_screenshot(self, filename):
        """Capture screenshot."""

        os.makedirs("screenshots", exist_ok=True)

        filepath = f"screenshots/{filename}.png"

        self.driver.save_screenshot(filepath)

        logger.info(f"Screenshot saved: {filepath}")

    def get_title(self):
        """Return page title."""
        return self.driver.title

    def get_current_url(self):
        """Return current URL."""
        return self.driver.current_url