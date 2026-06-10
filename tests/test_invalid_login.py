import pytest

from pages.login_page import LoginPage


def test_valid_login(driver):

    login_page = LoginPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert "inventory" in driver.current_url


@pytest.mark.parametrize(
    "username,password,expected",
    [
        (
            "wrong_user",
            "secret_sauce",
            "Username and password"
        ),
        (
            "standard_user",
            "wrong_password",
            "Username and password"
        ),
        (
            "",
            "secret_sauce",
            "Username is required"
        ),
        (
            "standard_user",
            "",
            "Password is required"
        )
    ]
)
def test_negative_login(
        driver,
        username,
        password,
        expected):

    login_page = LoginPage(driver)

    login_page.login(
        username,
        password
    )

    assert expected in (
        login_page.get_error_message()
    )