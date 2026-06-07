from pages.home_page import HomePage
from pages.password_page import PasswordPage

# 測試 first_Back按鈕
def test_first_launch_back_button(driver):

    home = HomePage(driver)
    home.wait_home_page()

    home.open_setting()
    password = PasswordPage(driver)
    assert password.is_pin_page_displayed()

    password.click_back()

    assert home.is_home_page()

# 測試 Back按鈕
def test_normal_launch_back_button(password_already_set):

    home = HomePage(password_already_set)
    home.wait_home_page()

    home.open_setting()
    password = PasswordPage(password_already_set)
    assert password.is_pin_page_displayed()

    password.click_back()

    assert home.is_home_page()