from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):

    CART_ICON = (
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    def add_product(self, product_id):

        product_locator = (
            By.ID,
            product_id
        )

        self.click(product_locator)

    def open_cart(self):

        self.click(
            self.CART_ICON
        )