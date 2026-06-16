from pages.home_page import HomePage
from pages.password_page import PasswordPage
from pages.gocayin.login_page import LoginPage

def test_open_setting_and_enter_password(driver):

    home = HomePage(driver)
    password = PasswordPage(driver)

    # 1. 點設定
    home.open_setting()

    # 2. 輸入 0000
    password.enter_password("0000")

    # 機器人驗證使用方式
    def wait_manual_captcha():
        input("請完成 reCAPTCHA，完成後按 Enter...")

    def test_login(driver):
        login = LoginPage(driver)

        login.login("admin", "admin")

        wait_manual_captcha()