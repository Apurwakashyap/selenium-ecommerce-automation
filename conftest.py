import pytest

from utils.driver_factory import get_driver
from utils.screenshot import take_screenshot


def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser name"
    )


@pytest.fixture
def driver(request):

    browser = request.config.getoption(
        "--browser"
    )

    driver = get_driver(browser)

    driver.get(
        "https://www.saucedemo.com/"
    )

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        if "driver" in item.funcargs:

            driver = item.funcargs["driver"]

            take_screenshot(
                driver,
                "failed_test"
            )