from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.base_page import BasePage


class SettingPage(BasePage):

    # 返回鍵
    BACK_BTN = (By.ID, "com.cayintech.cmswsplayer:id/left_btn")

    # tab
    PLAYBACK_TAB = (By.ID, "com.cayintech.cmswsplayer:id/playback")
    ADVANCE_TAB = (By.ID, "com.cayintech.cmswsplayer:id/advance")

    # form fields
    MODEL = (By.ID, "com.cayintech.cmswsplayer:id/model_spinner")
    PROTOCOL = (By.ID, "com.cayintech.cmswsplayer:id/protocol_spinner")
    IP = (By.ID, "com.cayintech.cmswsplayer:id/ip_edit_text")
    PORT = (By.ID, "com.cayintech.cmswsplayer:id/port_edit_text")
    USERNAME = (By.ID, "com.cayintech.cmswsplayer:id/username_edit_text")

    # actions
    def click_back(self):
        self.click(self.BACK_BTN)

    def switch_to_playback(self):
        self.click(self.PLAYBACK_TAB)

    def switch_to_advance(self):
        self.click(self.ADVANCE_TAB)

    # input actions
    def set_ip(self, ip):
        self.find(self.IP).clear()
        self.find(self.IP).send_keys(ip)

    def set_port(self, port):
        self.find(self.PORT).clear()
        self.find(self.PORT).send_keys(port)

    def set_username(self, username):
        self.find(self.USERNAME).clear()
        self.find(self.USERNAME).send_keys(username)

    def is_page_displayed(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.BACK_BTN)
            )
            return True
        except:
            return False

    def get_title(self):
        return self.get_text(self.TITLE)