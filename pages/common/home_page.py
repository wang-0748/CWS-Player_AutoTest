from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class HomePage(BasePage):

    SETTING_BTN = (
        By.ID,
        "com.cayintech.cmswsplayer:id/setting_btn"
    )

    PLAY_BTN = (
        By.ID,
        "com.cayintech.cmswsplayer:id/playback_btn"
    )

    TITLE = (
        By.ID,
        "com.cayintech.cmswsplayer:id/main_app_name"
    )


    def wait_home_page(self):
        self.wait_for(self.SETTING_BTN)

    def open_setting(self):
        self.wait_for(self.SETTING_BTN)
        self.click(self.SETTING_BTN)

    def open_playback(self):
        self.wait_for(self.SETTING_BTN)
        self.click(self.PLAY_BTN)

    def is_home_page(self):
        return (
            self.is_displayed(self.SETTING_BTN) and
            self.is_displayed(self.PLAY_BTN)
        )
