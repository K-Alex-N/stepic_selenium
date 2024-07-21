import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = browser.find_element(By.ID, "book")

WebDriverWait(browser, 12).until(
    ec.text_to_be_present_in_element((By.ID, "price"), "$100")
)

button.click()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x = browser.find_element(By.ID, "input_value")
y = calc(x.text)

browser.find_element(By.ID, "answer").send_keys(y)
browser.find_element(By.ID, "solve").click()

time.sleep(10)
browser.quit()
