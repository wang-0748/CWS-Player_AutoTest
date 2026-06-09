from pages.setting_page import SettingPage

def test_setting_page(driver):
    page = SettingPage(driver)

    # 1. 測 tab
    page.switch_tab("playback")
    page.switch_tab("advance")
    page.switch_tab("playback")

    page.select_model("CMS-WS")
    page.select_model("GO CAYIN")

    page.select_menu_item("隱私權政策")
    # 2. 測 back button（如果不會離開頁面就跳回來）
    page.click_back()