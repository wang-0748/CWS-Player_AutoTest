from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from utils.base_page import BasePage
from components.dialog import Dialog

class CmsWsLitePage(BasePage):
    URL_INPUT = (By.ID, "com.cayintech.cmswsplayer:id/url_edit_text")
    PLAY_BTN = (By.ID, "com.cayintech.cmswsplayer:id/play_btn")

    def trigger_validation(self, locator):
        self.click(locator)

    def click_play(self):
        self.click(self.PLAY_BTN)

    def input_url(self, url):
        self.input_text(self.URL_INPUT, url)

    # 驗證正確
    def is_page_displayed(self):
        pass

    # 空白內容
    def is_url_required_error(self):
        return "這個欄位不能是空的" in self.driver.page_source

    # URL錯誤
    def is_url_format_error(self):
        return "URL不正確" in self.driver.page_source

    # 連線錯誤 跳出的dialog
    def __init__(self, driver):
        super().__init__(driver)
        self.dialog = Dialog(driver)

    def is_error_dialog_shown(self):
        return self.dialog.is_visible()

    def get_error_dialog_text(self):
        return self.dialog.get_content_text()

    def close_error_dialog(self):
        self.dialog.close()