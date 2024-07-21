import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def abs(link):
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, "input").send_keys('fdssdf')
    browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys('asdasd')
    browser.find_element(By.CLASS_NAME, "third").send_keys('asdasd')
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    msg = welcome_text_elt.text
    browser.quit()
    return msg


class TestAbs():

    def test_link_ok(self):
        link = "http://suninjuly.github.io/registration1.html"
        assert (abs(link), "Congratulations! You have successfully registered!", "there is no welcome, congrat etc")

    def test_link_nok(self):
        link = "http://suninjuly.github.io/registration2.html"
        assert (abs(link), "Congratulations! You have successfully registered!", "there is no welcome, congrat etc")

# if __name__ == "__main__":
#     unittest.main()
