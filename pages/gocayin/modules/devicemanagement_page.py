from selenium.webdriver.common.by import By
from utils.base_page import BasePage


class DeviceManagementPage(BasePage):
    PLAY_BUTTON = (By.ID, "com.cayintech.cmswsplayer:id/play_btn")
    REGISTER_STATUS_TEXT = (By.ID, "com.cayintech.cmswsplayer:id/registergocayin_btn")

    # 🎯 填入剛剛確認的 Dialog 確認按鈕定位
    DIALOG_OK_BUTTON = (By.ID, "android:id/button1")

    def click_play(self):
        self.click(self.PLAY_BUTTON)

    def get_register_status(self):
        return self.get_text(self.REGISTER_STATUS_TEXT)

    # 🎯 點擊 Dialog 「確認」
    def click_dialog_ok(self):
        self.click(self.DIALOG_OK_BUTTON)