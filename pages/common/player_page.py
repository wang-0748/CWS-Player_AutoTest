from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class PlayerPage(BasePage):

    WEBVIEW = (AppiumBy.ID, "com.cayintech.cmswsplayer:id/web_view")

    # 1️⃣ 進入播放頁（App 層）
    def wait_player_loaded(self):
        self.wait_for_visible(self.WEBVIEW)

    # 2️⃣ WebView ready（可選）
    def wait_web_ready(self):
        return self.driver.execute_script("return document.readyState")

    # 3️⃣ 影片真的在播（重點）
    def wait_video_playing(self):
        return self.driver.execute_script("""
            const v = document.querySelector('video');
            return v && !v.paused && !v.ended;
        """)