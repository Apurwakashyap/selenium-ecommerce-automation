from selenium.webdriver.common.by import By

class CartPage:

    PRODUCT_NAME = (
        By.CLASS_NAME,
        "inventory_item_name"
    )

    def __init__(self, driver):
        self.driver = driver

    def get_product_name(self):

        return self.driver.find_element(
            *self.PRODUCT_NAME
        ).text