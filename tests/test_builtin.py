# ===================================================
# 備註：此測試依賴既有資料。若執行時觸發 App 初始化，將會導致登入後的內容呈現空白狀態。
# ===================================================

import time
from pages.gocayin.main_page import GoCayinPage
from pages.gocayin.login_page import LoginPage
from pages.gocayin.dashboard_page import DashboardPage
from pages.gocayin.modules.builtin_page import BuiltInPage
# 機器人驗證使用方式
from pages.gocayin.login_page import LoginPage


# 機器人驗證使用方式
def wait_manual_captcha():
    input("請完成 reCAPTCHA，完成後按 Enter...")


def test_login(driver):
    gocayin = GoCayinPage(driver)
    login = LoginPage(driver)

    gocayin.click_login()

    # 等登入頁出現
    login.wait_login_page()

    login.login(
        "hankruan@cayintech.com",
        "Cayin1234"
    )
    input("請完成機器人驗證後按 Enter 繼續...")

    # login.click_login_btn()

    time.sleep(5)

    # 進入登入後畫面
    dashboard = DashboardPage(driver)
    assert dashboard.is_loaded()
    print(dashboard.get_account_name())
    print(dashboard.get_login_account_status())

    # 調整 builtin 設定測試
    dashboard.select_content_type("內建播放清單")
    builtin = BuiltInPage(driver)
    builtin.select_builtin_set("New Playlist")
    builtin.scroll_to_element(builtin.PLAY_BUTTON)
    builtin.is_preview_displayed()
    builtin.click_play()