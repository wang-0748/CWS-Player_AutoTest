from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from utils.base_page import BasePage


class LoginPage(BasePage):

    EMAIL = (AppiumBy.XPATH,"//android.widget.EditText[@resource-id='email']")
    PASSWORD = (AppiumBy.XPATH,"//android.widget.EditText[@resource-id='password']")
    LOGIN_BTN = (AppiumBy.XPATH,"//android.widget.Button[@text='Login']")

    def wait_login_page(self):
        self.wait_for(self.EMAIL)

    def login(self, user, pwd):
        print("開始輸入 Email")
        self.input_text(self.EMAIL, user)

        print("開始輸入 Password")
        self.input_text(self.PASSWORD, pwd)

    def click_login_btn(self):
        self.click(self.LOGIN_BTN)
