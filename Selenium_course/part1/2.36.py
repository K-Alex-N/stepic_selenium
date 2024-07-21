import math
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

browser.find_element(By.TAG_NAME, "button").click()
browser.switch_to.window(browser.window_handles[1])

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element(By.ID, "input_value")
y = calc(x.text)

browser.find_element(By.ID, "answer").send_keys(y)
browser.find_element(By.TAG_NAME, "button").click()


time.sleep(10)
browser.quit()
