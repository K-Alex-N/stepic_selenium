from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")

    x = browser.find_element(By.ID, "num1")
    y = browser.find_element(By.ID, "num2")

    browser.find_element(By.ID, "dropdown").click()
    browser.find_element(By.CSS_SELECTOR, "option[value='" + str(int(x.text)+int(y.text)) + "']").click()

    browser.find_element(By.TAG_NAME, "button").click()


finally:
    time.sleep(10)
    browser.quit()