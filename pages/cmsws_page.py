from selenium.webdriver.common.by import By
from utils.base_page import BasePage


class CmsWsPage(BasePage):
    # CMS-WS 專屬
    PROTOCOL = (By.ID, "com.cayintech.cmswsplayer:id/text1")
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

    def login(self, protocol, ip, port, username, password):
        self.select_protocol(protocol)
        self.input_ip(ip)
        self.input_port(port)
        self.input_username(username)
        self.input_password(password)
        self.click_confirm()

    # IP、USERNAME、PASSWORD 為空欄位
    def get_field_error(self, field):
        return self.driver.find_element(*field).get_attribute("error")

    def is_ip_required_error(self):
        return self.get_field_error(self.IP) == "這個欄位不能是空的"

    def is_ip_format_error(self):
        return self.get_field_error(self.IP) == "IP位址不正確"

    def is_username_required_error(self):
        return self.get_field_error(self.USERNAME) == "這個欄位不能是空的"

    def is_password_required_error(self):
        return self.get_field_error(self.PASSWORD) == "這個欄位不能是空的"

    def get_login_error(self):
        # 這裡是整體 login fail（username/password錯）
        return self.driver.find_element(
            By.XPATH,
            "//*[contains(@text, '使用者名稱或密碼錯誤')]"
        ).text


    # 補成功畫面、錯誤資訊(OK)、空白內容的顯示(OK)、跳出的dialog