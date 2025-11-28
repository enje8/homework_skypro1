from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OverviewPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_total(self) -> None:
        total_element = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        text = total_element.text  # "Total: $58.29"
        return text.replace("Total: $", "")