from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from utils.base_page import BasePage
from components.dialog import Dialog


class CmsBasePage(BasePage):
    # CMS-WS 專屬
    PROTOCOL = (By.ID, "com.cayintech.cmswsplayer:id/protocol_spinner")
    IP = (By.ID, "com.cayintech.cmswsplayer:id/ip_edit_text")
    PORT = (By.ID, "com.cayintech.cmswsplayer:id/port_edit_text")
    USERNAME = (By.ID, "com.cayintech.cmswsplayer:id/username_edit_text")
    PASSWORD = (By.ID, "com.cayintech.cmswsplayer:id/pwd_edit_text")

    # UI control
    CONFIRM_BTN = (By.ID, "com.cayintech.cmswsplayer:id/confirm_btn")
    PLAYBACK_BTN = (By.ID, "com.cayintech.cmswsplayer:id/play_btn")

    def select_protocol(self, protocol):
        self.click(self.PROTOCOL)

        option = (
            By.XPATH,
            f"//android.widget.TextView[@text='{protocol}']"
        )
        self.click(option)

    def input_ip(self, ip):
        self.input_text(self.IP, ip)

    def input_port(self, port):
        self.input_text(self.PORT, port)

    def input_username(self, username):
        self.input_text(self.USERNAME, username)

    def input_password(self, password):
        self.input_text(self.PASSWORD, password)

    def click_confirm(self):
        self.click(self.CONFIRM_BTN)

    def click_play(self):
        self.click(self.PLAYBACK_BTN)

    def trigger_validation(self, locator):
        self.click(locator)

    # 往下滑動作
    def scroll_to_element(self, locator):
        by, value = locator

        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().resourceId("{value}"))'
        )
    # 登入
    def login(self, protocol, ip, port, username, password):
        self.select_protocol(protocol)
        self.input_ip(ip)
        self.input_port(port)
        self.scroll_to_element(self.PASSWORD)
        self.input_username(username)
        self.input_password(password)
        self.click_confirm()

    # IP、USERNAME、PASSWORD 錯誤資訊、空白內容的顯示
    def get_field_error(self, field):
        return self.driver.find_element(*field).text

    def is_ip_required_error(self):
        return "這個欄位不能是空的" in self.driver.page_source

    def is_ip_format_error(self):
        return "IP位址不正確" in self.driver.page_source

    def is_username_required_error(self):
        return "這個欄位不能是空的" in self.driver.page_source

    def is_username_format_error(self):
        return "使用者名稱或密碼錯誤" in self.driver.page_source

    def is_password_required_error(self):
        return "這個欄位不能是空的" in self.driver.page_source

    def is_password_format_error(self):
        return "使用者名稱或密碼錯誤" in self.driver.page_source

    # 補成功畫面、

    # 跳出的dialog
    def __init__(self, driver):
        super().__init__(driver)
        self.dialog = Dialog(driver)

    def is_error_dialog_shown(self):
        return self.dialog.is_visible()

    def get_error_dialog_text(self):
        return self.dialog.get_content_text()

    def close_error_dialog(self):
        self.dialog.close()
