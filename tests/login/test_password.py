from pages.home_page import HomePage
from pages.password_page import PasswordPage
from pages.setting_page import SettingPage

# 測試正確密碼
def test_correct_password(password_already_set):

    home = HomePage(password_already_set)
    home.open_setting()

    password = PasswordPage(password_already_set)
    password.enter_password("0000")

    assert not password.is_pin_page_displayed()

# 測試錯誤密碼
def test_wrong_password(password_already_set):

    home = HomePage(password_already_set)
    home.open_setting()

    password = PasswordPage(password_already_set)
    password.enter_password("9999")

    assert password.get_error_message() == "錯誤的PIN碼"

# 測試錯誤五次會出現倒數
def test_lock_5_attempts(password_already_set):

    home = HomePage(password_already_set)
    home.open_setting()

    password = PasswordPage(password_already_set)
    for attempt in range(5):
        password.enter_password("9999")

    assert password.is_locked()


