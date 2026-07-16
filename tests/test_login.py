from pages.login_page import LoginPage
from config.config_reader import config

def test_login(driver):

    login_page = LoginPage(driver)

    login_page.login(
        config.username,
        config.password)

    assert "inventory" in driver.current_url
    