import pytest
from pages.home_page import HomePage
from pages.password_page import PasswordPage
from utils.driver_factory import create_driver
from pages.setting_page import SettingPage

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

@pytest.fixture
def password_already_set(driver):
    home = HomePage(driver)
    home.open_setting()

    password = PasswordPage(driver)
    password.enter_password("0000")

    setting = SettingPage(driver)
    assert setting.is_page_displayed()

    setting.click_back()

    return driver
