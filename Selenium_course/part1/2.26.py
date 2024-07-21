import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://SunInJuly.github.io/execute_script.html")


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


x = browser.find_element(By.ID, "input_value")
y = calc(x.text)

input_field = browser.find_element(By.ID, "answer")
input_field.send_keys(y)

checkbox = browser.find_element(By.ID, "robotCheckbox")
checkbox.click()

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

radio = browser.find_element(By.ID, "robotsRule")
radio.click()

button.click()

time.sleep(10)
browser.quit()