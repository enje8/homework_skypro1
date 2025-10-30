from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("http://the-internet.herokuapp.com/login")

username_field = driver.find_element(By.ID, 'username')
username_field.send_keys("tomsmith")
sleep(2)

password_field = driver.find_element(By.ID, 'password')
password_field.send_keys("SuperSecretPassword!")
sleep(2)

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()
sleep(2)

message = driver.find_element(By.ID, "flash").text
print(message)
sleep(1)

driver.quit()