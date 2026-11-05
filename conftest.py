import pytest

from config.config_reader import config
from utils.driver_factory import get_driver
from utils.logger import logger
from utils.screenshot import take_screenshot


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="Browser to use: chrome or edge (defaults to config.ini)",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run the browser in headless mode",
    )


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser") or config.default_browser
    headless = request.config.getoption("--headless")

    logger.info("Starting browser session: %s (headless=%s)", browser, headless)
    browser_driver = get_driver(browser, headless=headless)

    try:
        if not headless:
            browser_driver.maximize_window()

        browser_driver.set_page_load_timeout(config.page_load_timeout)

        logger.info("Opening application URL: %s", config.base_url)
        browser_driver.get(config.base_url)

        yield browser_driver
    finally:
        logger.info("Closing browser session")
        browser_driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        browser_driver = item.funcargs.get("driver")

        if browser_driver is not None:
            logger.error("Test failed: %s", item.nodeid)
            try:
                screenshot_path = take_screenshot(browser_driver, item.name)
                logger.info("Failure screenshot saved: %s", screenshot_path)
            except Exception:
                logger.exception("Could not capture failure screenshot")
