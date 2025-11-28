import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Pages.cart_page import CartPage
from Pages.checkout_page import CheckoutPage
from Pages.overview_page import OverviewPage

@allure.title("Оформления заказа и проверка итоговой суммы")
@allure.description("Тест проверяет добавление товаров в корзину, оформление заказа и корректность итоговой суммы.")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)

def test_shopping():

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    overview = OverviewPage(driver)

    with allure.step("Открыть страницу и выполнить вход"):
      login.open()
      login.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину и перейти в корзину"):
      inventory.add_item("sauce-labs-backpack")
      inventory.add_item("sauce-labs-bolt-t-shirt")
      inventory.add_item("sauce-labs-onesie")
      inventory.go_to_cart()

    with allure.step("Перейти к оформлению заказа"):
      cart.checkout()

    with allure.step("Заполнить данные пользователя"):
      checkout.fill_user_info("Enje", "Mazitova", "420064")
      checkout.continue_checkout()

    with allure.step("Проверить итоговую сумму заказа"):
      total_amount = overview.get_total()

      assert total_amount == "58.29", f"Ожидали $58.29, получили ${total_amount}"

    driver.quit()