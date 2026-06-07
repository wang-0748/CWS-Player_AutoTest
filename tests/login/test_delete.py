from pages.home_page import HomePage
from pages.password_page import PasswordPage

# 測試 first Delete 按鈕
def test_first_launch_delete_button(driver):

    home = HomePage(driver)
    home.open_setting()

    password = PasswordPage(driver)
    password.enter_password("123")
    password.click_delete()
    password.enter_password("4")

    assert password.is_pin_page_displayed()

# 測試 Delete 按鈕
def test_normal_launch_password(password_already_set):

    home = HomePage(password_already_set)
    home.open_setting()

    password = PasswordPage(password_already_set)
    password.enter_password("123")
    password.click_delete()
    password.enter_password("4")

    assert password.is_pin_page_displayed()