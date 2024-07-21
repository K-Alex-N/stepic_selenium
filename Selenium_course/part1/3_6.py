import math
import os
import time

import pytest
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from conftest import browser

load_dotenv()

# link = "https://stepik.org/lesson/236895/step/1"

# answer = math.log(int(time.time()))

links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"]


class TestLogin():

    @pytest.mark.parametrize("link", links)
    def test_sfsdfsdf(self, browser, link):
        browser.get(link)
        browser.implicitly_wait(10)

        ans = (math.log(int(time.time())))

        browser.find_element(By.ID, "ember459").click()
        browser.find_element(By.ID, "id_login_email").send_keys(os.getenv("EMAIL"))
        browser.find_element(By.ID, "id_login_password").send_keys(os.getenv("PASSWORD"))
        browser.find_element(By.CLASS_NAME, "sign-form__btn").click()
        time.sleep(1)
        browser.find_element(By.CLASS_NAME, "again-btn").click()

        text_field = browser.find_element(By.CLASS_NAME, "ember-text-area")
        try:
            text_field.clear()
            text_field.send_keys(ans)
        except:
            pass



        button = WebDriverWait(browser, 10).until(
            expected_conditions.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
        # button.click()
        time.sleep(0.5)
        button.click()

        # browser.find_element(By.CLASS_NAME, "submit-submission").click()
        # time.sleep(1)
        msg = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
        print(msg.text)

        # browser.find_element(By.CLASS_NAME, "submit-submission").click()
        time.sleep(1)
