# pages/common/setting_advance_page.py
from selenium.webdriver.common.by import By
from pages.common.setting_page import SettingPage  # 繼承你原本的 SettingPage


class SettingAdvancePage(SettingPage):
    # ==========================================
    # 🎯 進階頁面專屬定位器 (Locators)
    # ==========================================
    STORAGE_SIZE_TXT = (By.ID, "com.cayintech.cmswsplayer:id/storage_size_txt")      # 檔案儲存空間文字
    BROWSER_SPINNER = (By.ID, "com.cayintech.cmswsplayer:id/browser_spinner")        # 瀏覽器下拉選單
    DISPLAY_SPINNER = (By.ID, "com.cayintech.cmswsplayer:id/display_spinner")        # 顯示方向下拉選單
    AUTO_LAUNCH_SWITCH = (By.ID, "com.cayintech.cmswsplayer:id/auto_launch_switch")  # 自動啟動開關

    # ==========================================
    # 🎯 進階頁面專屬動作 (Actions)
    # ==========================================
    def get_storage_info(self):
        """取得檔案儲存空間文字 (例如: 已使用 31.8 GB (256 GB))"""
        return self.get_text(self.STORAGE_SIZE_TXT)

    def is_auto_launch_enabled(self):
        """檢查自動啟動開關是否為開啟狀態 (回傳 True/False)"""
        # Android 的 Switch 通常可以用 checked 屬性來判斷狀態
        return self.get_attribute(self.AUTO_LAUNCH_SWITCH, "checked") == "true"

    def click_auto_launch(self):
        """單純點擊自動啟動開關"""
        self.click(self.AUTO_LAUNCH_SWITCH)