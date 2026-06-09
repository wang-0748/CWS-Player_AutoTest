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

    # 補成功畫面、錯誤資訊、空白內容的顯示