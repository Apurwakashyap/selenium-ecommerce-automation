from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def get_driver(browser):

    if browser.lower() == "chrome":

        driver = webdriver.Chrome(
            service=ChromeService(
                ChromeDriverManager().install()
            )
        )

    elif browser.lower() == "edge":

        driver = webdriver.Edge(
            service=EdgeService(
                EdgeChromiumDriverManager().install()
            )
        )

    else:

        raise ValueError(
            f"Browser {browser} not supported"
        )

    driver.maximize_window()

    return driver