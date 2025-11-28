from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    delay_field = (By.ID, "delay")
    screen = (By.CLASS_NAME, "screen")

    def button(self, value: str) -> tuple:
        return (By.XPATH, f"//span[text()='{value}']")

    def open(self) -> None:
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds: str) -> None:
        delay_input = self.wait.until(EC.presence_of_element_located(self.delay_field))
        delay_input.clear()
        delay_input.send_keys(seconds)

    def click_button(self, value: str) -> None:
        self.wait.until(EC.element_to_be_clickable(self.button(value))).click()

    def wait_for_result(self, expected: str) -> None:
        self.wait.until(EC.text_to_be_present_in_element(self.screen, expected))