import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from MainPage import MainPage

def test_calculator():
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    page = MainPage(driver)

    page.open()
    page.set_delay("45")

    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    page.wait_for_result("15")

    driver.quit()