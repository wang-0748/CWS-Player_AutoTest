import copy

from pages.common.setting_page import SettingPage
from pages.cmsws.cmsws_page import CmsWsPage
from pages.cmsws.cmsws_main_page import CmsWsMainPage

# 直接拿test_data裡面的資料來使用
from config.cmsws_base.test_data import BASE_ACCOUNT
from config.cmsws_base.test_data import INVALID_USERNAME, INVALID_PASSWORD, EMPTY, BAD_IP

# 機器人驗證使用方式
from pages.gocayin.login_page import LoginPage
# def test_setting_page(driver):
#     page = SettingPage(driver)
#
#     # 1. 測 tab
#     page.switch_tab("playback")
#     page.switch_tab("advance")
#     page.switch_tab("playback")
#
#     page.select_model("CMS-WS")
#     page.select_model("GO CAYIN")
#
#     # 2. 測 back button（如果不會離開頁面就跳回來）
#     page.click_back()

def test_login_success(driver):
    page = CmsWsPage(driver)

    page.login(
        protocol="HTTP",
        ip="192.168.100.7",
        port="80",
        username="administrator",
        password="admin"
    )
    page_main = CmsWsMainPage(driver)
    page_main.change_group_and_hostname("Player","hostname")

# def test_dialog_success(driver):
#     page = CmsWsPage(driver)
#     page.login(
#         protocol="HTTP",
#         ip="999.999.999.999",
#         port="80",
#         username="admin",
#         password="admin"
#     )
#
#     assert page.is_error_dialog_shown()
#     assert "無法正確連線" in page.get_error_dialog_text()
#
#     page.close_error_dialog()

# def test_login_wrong_username(driver):
#     page = CmsWsPage(driver)
#
#     page.login(
#         protocol="HTTP",
#         ip="172.16.20.146",
#         port="80",
#         username="",
#         password="admin"
#     )
#     page.trigger_validation(page.USERNAME)
#     assert page.is_username_required_error()

# config 正確資料標準用法
def test_dialog_success(driver):
    page = CmsWsPage(driver)
    page.login(**BASE_ACCOUNT)

# config 替換錯誤資料標使用法
def test_login_invalid_username(driver):
    data = copy.deepcopy(BASE_ACCOUNT)
    data["username"] = INVALID_USERNAME

    page = CmsWsPage(driver)
    page.login(**data)

# 機器人驗證使用方式
def wait_manual_captcha():
    input("請完成 reCAPTCHA，完成後按 Enter...")

def test_login(driver):
    login = LoginPage(driver)

    login.login("admin", "admin")

    wait_manual_captcha()
