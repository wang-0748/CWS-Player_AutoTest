from selenium.webdriver.common.by import By
from utils.base_page import BasePage


class CmsWsMainPage(BasePage):

    GROUP = (By.ID, "com.cayintech.cmswsplayer:id/group_spinner")
    HOSTNAME = (By.ID, "com.cayintech.cmswsplayer:id/hostname_edit_text")
    PLAY_BTN = (By.ID, "com.cayintech.cmswsplayer:id/play_btn")

    def select_group(self, group_name):
        self.click(self.GROUP)
        self.click_text((By.ID, "android:id/text1"), group_name)

    def enter_hostname(self, hostname):
        self.input_text(self.HOSTNAME, hostname)

    def click_play(self):
        self.click(self.PLAY_BTN)

    def is_page_displayed(self):
        return self.is_displayed(self.PLAY_BTN)

# class CmsWsMainPage(BasePage):
#
#     # CMS-WS 第二狀態 UI
#     GROUP
#     HOSTNAME
#     PLAY_BTN
#     CHANGE_BTN
#
#     # 仍可能保留
#     BACK_BTN
#     PLAYBACK_TAB
#     ADVANCE_TAB
#     PRODUCT_MODEL_SPINNER
#
#     # actions
#     select_group()
#     enter_hostname()
#     click_play()
#     click_change()