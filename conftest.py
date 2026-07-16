import pytest
from config.config_reader import config
from utils.driver_factory import get_driver
from utils.logger import logger
from utils.screenshot import take_screenshot


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser name"
    )


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")

    logger.info(f"Launching {browser} browser")

    driver = get_driver(browser)

    driver.maximize_window()

    logger.info("Opening application")

    driver.get(config.base_url)

    yield driver

    logger.info("Closing browser")

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        if "driver" in item.funcargs:
            driver = item.funcargs["driver"]

            logger.error(f"Test Failed: {item.name}")

            take_screenshot(driver, item.name)