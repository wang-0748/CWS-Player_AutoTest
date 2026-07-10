import time
from pages.gocayin.main_page import GoCayinPage
from pages.gocayin.login_page import LoginPage
from pages.gocayin.dashboard_page import DashboardPage
from pages.gocayin.modules.slideshow_page import SlideShowPage
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

    # 調整 slideshow 設定測試
    dashboard.select_content_type("GO CAYIN 輪播清單")
    slideshow = SlideShowPage(driver)
    slideshow.select_slideshow_set("test")
    slideshow.scroll_to_element(slideshow.PLAY_BUTTON)
    slideshow.is_preview_displayed()
    slideshow.click_play()