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

# 生成 Allure 報告 & 失敗自動截圖
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """測試失敗時自動擷取手機螢幕並附於 Allure 報告中"""
    outcome = yield
    report = outcome.get_result()

    # 只針對執行（call）階段且結果為失敗（failed）的案例進行截圖
    if report.failed:
        driver = None

        # 1. 優先從測試案例傳入的參數中找 driver
        for arg in item.funcargs.values():
            if hasattr(arg, "get_screenshot_as_png"):
                driver = arg
                break

        # 2. 若 setup 階段出錯 (例如 logged_in_driver 壞掉)，嘗試從 session 級別的 fixture 抓取 driver
        if not driver and hasattr(item, "_request"):
            try:
                driver = item._request.getfixturevalue("driver")
            except Exception:
                driver = None

        # 3. 執行截圖並附加到 Allure 報告
        if driver:
            try:
                screenshot = driver.get_screenshot_as_png()
                stage_name = "前置準備 (Setup)" if report.when == "setup" else "測試執行 (Call)"
                allure.attach(
                    screenshot,
                    name=f"💥 [{stage_name}] 失敗當下畫面截圖",
                    attachment_type=allure.attachment_type.PNG,
                )
                print(f"\n［Hook］已成功將 [{stage_name}] 失敗畫面附加至 Allure 報告！")
            except Exception as e:
                print(f"\n［Hook］截圖失敗: {e}")

