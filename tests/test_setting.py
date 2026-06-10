from pages.setting_page import SettingPage
from pages.cmsws_page import CmsWsPage

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

# def test_login_success(driver):
#     page = CmsWsPage(driver)
#
#     page.login(
#         protocol="HTTP",
#         ip="172.16.20.146",
#         port="80",
#         username="administrator",
#         password="admin"
#     )
#
#     page.click_play()

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

def test_login_wrong_username(driver):
    page = CmsWsPage(driver)

    page.login(
        protocol="HTTP",
        ip="172.16.20.146",
        port="80",
        username="wrong_user",
        password="admin"
    )
    page.trigger_validation(page.USERNAME)
    assert page.is_username_format_error()