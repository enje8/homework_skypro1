from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_user_info(self, first: str, last: str, postal: str) -> None:
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(first)
        self.driver.find_element(By.ID, "last-name").send_keys(last)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal)

    def continue_checkout(self) -> None:
        self.driver.find_element(By.ID, "continue").click()