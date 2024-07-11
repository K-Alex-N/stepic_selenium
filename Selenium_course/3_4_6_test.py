import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def browser():
    browser = webdriver.Chrome()
    browser.get(link)
    yield browser
    browser.quit()

@pytest.fixture(autouse=True)
def prepare_data():
    print("\npreparing some critical data for every test")


class TestMainPage1():
    def test_guest_should_see_login_link(self, browser):
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")