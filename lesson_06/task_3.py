from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

WebDriverWait(driver, 10).until(
    lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 4
)

images = driver.find_elements(By.TAG_NAME, "img")
print(images[3].get_attribute("src"))

driver.quit()