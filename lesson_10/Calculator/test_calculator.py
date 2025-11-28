import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from MainPage import MainPage

@allure.title("Тестирование калькулятора: 7 + 8 = 15")
@allure.description("Тест проверяет корректность работы калькулятора.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)

def test_calculator():
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    page = MainPage(driver)

    with allure.step("Открыть страницу калькулятора"):
      page.open()
    
    with allure.step("Установить задержку 45 секунд"):
      page.set_delay("45")

    with allure.step("Нажать на кнопки 7, +, 8, ="):
      page.click_button("7")
      page.click_button("+")
      page.click_button("8")
      page.click_button("=")

    with allure.step("Ожидание результата"):
      page.wait_for_result("15")

    driver.quit()