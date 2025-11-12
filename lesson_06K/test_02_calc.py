import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 60)

def test_calculator():

  try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = wait.until(EC.presence_of_element_located((By.ID, "delay")))
    delay_input.clear()
    delay_input.send_keys("45")


    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='7']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='+']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='8']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='=']"))).click()

    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

  finally:
    driver.quit()


if __name__ == "__main__":
    test_calculator()