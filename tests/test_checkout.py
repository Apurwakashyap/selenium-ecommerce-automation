import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.data_reader import read_checkout_data
@pytest.mark.parametrize(
    "first_name,last_name,zip_code",
    read_checkout_data()
)
def test_checkout_flow(
        driver: WebDriver,
        first_name,
        last_name,
        zip_code):

    LoginPage(driver).login(
        "standard_user",
        "secret_sauce"
    )

    inventory = InventoryPage(driver)

    inventory.add_product(
        "add-to-cart-sauce-labs-backpack"
    )

    inventory.open_cart()

    checkout = CheckoutPage(driver)

    checkout.start_checkout()

    checkout.enter_customer_details(
        first_name,
        last_name,
        zip_code
    )

    checkout.continue_checkout()

    checkout.finish_order()

    assert (
        checkout.get_success_message()
        == "Thank you for your order!"
    )