import time
from pages.gocayin.main_page import GoCayinPage
from pages.gocayin.login_page import LoginPage
from pages.gocayin.dashboard_page import DashboardPage
from pages.gocayin.modules.meetingpost_page import MeetingPostPage
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

    dashboard.select_content_type("GO CAYIN meetingPost+")

    # 調整 meetingpost 設定測試

    meetingpost = MeetingPostPage(driver)
    meetingpost.select_room_set("會議室")
    meetingpost.select_room("BB")
    meetingpost.click_play()