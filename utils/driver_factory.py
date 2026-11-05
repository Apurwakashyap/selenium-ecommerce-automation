from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def get_driver(browser, headless=False):
    """Create and return a configured Selenium WebDriver instance."""
    browser = browser.strip().lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        }
        options.add_experimental_option("prefs", prefs)
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")

        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options,
        )

    if browser == "edge":
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")

        return webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options,
        )

    raise ValueError(
        f"Unsupported browser: '{browser}'. Supported browsers: chrome, edge."
    )
