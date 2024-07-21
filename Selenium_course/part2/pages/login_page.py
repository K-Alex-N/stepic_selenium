from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        # ID "login_form"
        # self.browser
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        # register_form
        # реализуйте проверку, что есть форма регистрации на странице
        assert True
