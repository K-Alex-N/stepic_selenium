import math
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/file_input.html")

browser.find_element(By.TAG_NAME, "input").send_keys('fdssdf')
browser.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys('asdasd')
browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys('asdasd')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file')
browser.find_element(By.ID, "file").send_keys(file_path)

browser.find_element(By.CLASS_NAME, "btn").click()

time.sleep(10)
browser.quit()