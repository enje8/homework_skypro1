from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_item(self, item_id):
        button_id = f"add-to-cart-{item_id}"
        self.driver.find_element(By.ID, button_id).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()