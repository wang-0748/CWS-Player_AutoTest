# pages/common/setting_advance_page.py
from selenium.webdriver.common.by import By
from pages.common.setting_page import SettingPage  # 繼承你原本的 SettingPage


class SettingAdvancePage(SettingPage):

    STORAGE_SIZE_TXT = (By.ID, "com.cayintech.cmswsplayer:id/storage_size_txt")
    BROWSER_SPINNER = (By.ID, "com.cayintech.cmswsplayer:id/browser_spinner")
    DISPLAY_SPINNER = (By.ID, "com.cayintech.cmswsplayer:id/display_spinner")
    AUTO_LAUNCH_SWITCH = (By.ID, "com.cayintech.cmswsplayer:id/auto_launch_switch")
    SYNC_PRELOAD_STATUS = (By.ID, "com.cayintech.cmswsplayer:id/sync_preload_status_tv")
    SYNC_PRELOAD_BTN = (By.ID, "com.cayintech.cmswsplayer:id/sync_preload_img")
    DEFAULT_CONTENT_ROW = (By.ID, "com.cayintech.cmswsplayer:id/default_content_row")
    DEFAULT_CONTENT_SWITCH = (By.ID, "com.cayintech.cmswsplayer:id/default_content_switch")
    FILE_LIST_RECYCLER = (By.ID, "com.cayintech.cmswsplayer:id/file_rv")

    def get_storage_info(self):
        """取得檔案儲存空間文字 (例如: 已使用 32.3 GB (256 GB))"""
        return self.get_text(self.STORAGE_SIZE_TXT)

    def click_storage_size(self):
        self.click(self.STORAGE_SIZE_TXT)

    def click_browser_spinner(self):
        self.click(self.BROWSER_SPINNER)

    def click_display_spinner(self):
        self.click(self.DISPLAY_SPINNER)

    def click_auto_launch(self):
        self.click(self.AUTO_LAUNCH_SWITCH)

    def is_auto_launch_enabled(self):
        """檢查自動啟動開關是否為開啟狀態 (回傳 True/False)"""
        return self.get_attribute(self.AUTO_LAUNCH_SWITCH, "checked") == "true"

    # 1. 同步預載相關
    def get_sync_preload_status(self):
        """取得同步預載模式目前的狀態 (例如: "停用" 或 "啟用")"""
        return self.get_text(self.SYNC_PRELOAD_STATUS)

    def click_sync_preload_setting(self):
        self.click(self.SYNC_PRELOAD_BTN)

    # 2. 預設內容相關
    def is_default_content_enabled(self):
        """檢查預設內容開關是否為開啟狀態 (回傳 True/False)"""
        return self.get_attribute(self.DEFAULT_CONTENT_SWITCH, "checked") == "true"

    def set_default_content(self, expect_on: bool):
        """
        設定預設內容開關
        :param expect_on: True 代表要開啟, False 代表要關閉
        """
        current_state = self.is_default_content_enabled()
        if current_state != expect_on:
            self.click(self.DEFAULT_CONTENT_SWITCH)
            print(f"［LOG］預設內容開關已切換為: {expect_on}")
        else:
            print(f"［LOG］預設內容開關已是預期狀態: {expect_on}，不需點擊")

    # 3. 選擇多媒體檔案相關
    def select_media_file_by_name(self, file_name):
        """
        在 RecyclerView 檔案列表中，根據檔案名稱點擊特定的多媒體檔案
        :param file_name: 想要選擇的檔案名稱 (例如: 'video.mp4')
        """
        file_option_locator = (
            By.XPATH,
            f"//androidx.recyclerview.widget.RecyclerView[@resource-id='com.cayintech.cmswsplayer:id/file_rv']"
            f"//android.widget.TextView[@text='{file_name}']"
        )

        self.scroll_to_element(file_option_locator)
        self.click(file_option_locator)
        print(f"［LOG］已在列表中點擊多媒體檔案: {file_name}")