from utils.base_page import BasePage

class LoginPage(BasePage):

    EMAIL = ("id", "email")
    PASSWORD = ("id", "password")
    LOGIN_BTN = ("text", "登入")

    def login(self, user, pwd):
        self.find(self.EMAIL).send_keys(user)
        self.find(self.PASSWORD).send_keys(pwd)
        self.find(self.LOGIN_BTN).click()