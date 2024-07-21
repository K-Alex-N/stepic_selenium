from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")



class LoginPageLocators():
    pass



class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = By.CSS_SELECTOR, "#add_to_basket_form button"