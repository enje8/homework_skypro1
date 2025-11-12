from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

def test_shopping():
    try:
        driver.get("https://www.saucedemo.com/")
        
        wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
        
        wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Enje")
        driver.find_element(By.ID, "last-name").send_keys("Mazitova")
        driver.find_element(By.ID, "postal-code").send_keys("420064")

        driver.find_element(By.ID, "continue").click()
        
        total_element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text
        
        total_amount = total_text.replace("Total: $", "")
        
        assert total_amount == "58.29", f"Ожидаемая сумма: $58.29, Фактическая сумма: ${total_amount}"
        
    finally:
        driver.quit()


if __name__ == "__main__":
    test_shopping()