from pages.home_page import HomePage
from pages.password_page import PasswordPage


def test_open_setting_and_enter_password(driver):

    home = HomePage(driver)
    password = PasswordPage(driver)

    # 1. 點設定
    home.open_setting()

    # 2. 輸入 0000
    password.enter_password("0000")