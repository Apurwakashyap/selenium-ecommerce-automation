from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_to_cart(driver):

    LoginPage(driver).login(
        "standard_user",
        "secret_sauce"
    )

    inventory = InventoryPage(driver)

    inventory.add_product(
        "add-to-cart-sauce-labs-backpack"
    )

    inventory.open_cart()

    cart = CartPage(driver)

    assert (
        cart.get_product_name()
        == "Sauce Labs Backpack"
    )