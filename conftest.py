import allure
import pytest
import time
from utils.driver_factory import create_driver
from pages.common.home_page import HomePage
from pages.common.password_page import PasswordPage
from pages.common.setting_page import SettingPage
from pages.gocayin.dashboard_page import DashboardPage
from pages.gocayin.main_page import GoCayinPage
from pages.gocayin.login_page import LoginPage

@pytest.fixture(scope="session")
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

@pytest.fixture(scope="session")
def logged_in_driver(driver):
    dashboard_page = DashboardPage(driver)
    home = HomePage(driver)
    home.open_setting()

    password = PasswordPage(driver)
    password.enter_password("0000")

    setting = SettingPage(driver)
    assert setting.is_page_displayed()
    setting.select_model("GO CAYIN")

    # 1. 優先檢查是否已經是登入狀態 (例如 noReset 保留了 Session)
    try:
        is_logged_in = dashboard_page.is_dashboard_displayed()
    except Exception:
        is_logged_in = False

    # 2. 若未登入，才執行手動/自動輔助登入流程
    if not is_logged_in:
        print("\n［Fixture］偵測到未登入，啟動登入前置流程...")
        gocayin = GoCayinPage(driver)
        login = LoginPage(driver)

        gocayin.click_login()
        login.wait_login_page()
        login.login("hankruan@cayintech.com", "Cayin1234")

        # 提示人工完成 CAPTCHA
        input("\n請手動完成 reCAPTCHA 機器人驗證後，在此處按下 Enter 鍵繼續...")

        # login.click_login_btn()

        # 等待登入成功並加載首頁
        time.sleep(5)
        is_logged_in = dashboard_page.is_dashboard_displayed()

    # 3. 最終驗證
    if not is_logged_in:
        raise AssertionError("App 登入失敗，請確認帳密與機器人驗證是否通過。")

    yield driver

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """測試失敗時自動擷取手機螢幕並附於 Allure 報告中"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("logged_in_driver") or item.funcargs.get("driver")
        if driver:
            try:
                screenshot = driver.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name="失敗當下手機畫面",
                    attachment_type=allure.attachment_type.PNG,
                )
            except Exception as e:
                print(f"\n［Hook］截圖失敗: {e}")