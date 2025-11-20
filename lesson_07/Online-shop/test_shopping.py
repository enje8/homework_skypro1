from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Pages.cart_page import CartPage
from Pages.checkout_page import CheckoutPage
from Pages.overview_page import OverviewPage


def test_shopping():

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    overview = OverviewPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_item("sauce-labs-backpack")
    inventory.add_item("sauce-labs-bolt-t-shirt")
    inventory.add_item("sauce-labs-onesie")
    inventory.go_to_cart()

    cart.checkout()

    checkout.fill_user_info("Enje", "Mazitova", "420064")
    checkout.continue_checkout()

    total_amount = overview.get_total()

    assert total_amount == "58.29", f"Ожидали $58.29, получили ${total_amount}"

    driver.quit()