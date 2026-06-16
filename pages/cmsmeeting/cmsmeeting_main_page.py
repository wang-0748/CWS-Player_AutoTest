from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from utils.base_page import BasePage
import time

class CmsWsMainPage(BasePage):

    CHANGE_BTN = (By.ID, "com.cayintech.cmswsplayer:id/change_btn")
    ROOM_SET = (By.ID, "com.cayintech.cmswsplayer:id/room_room_set_spinner")
    ROOM_SPINNER = (By.ID, "com.cayintech.cmswsplayer:id/room_spinner")
    PLAY_BTN = (By.ID, "com.cayintech.cmswsplayer:id/play_btn")

    # ===== Actions =====

    def click_change(self):
        self.click(self.CHANGE_BTN)

    def click_play(self):
        self.click(self.PLAY_BTN)

    def trigger_validation(self, locator):
        self.click(locator)

    # 往下滑動作(找完後不要加點擊的動作，很容易因為畫面還沒穩定，導致點擊失敗)
    def scroll_to_element(self, locator):
        by, value = locator

        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().resourceId("{value}"))'
        )

    def select_room_set(self, room_set):
        self.click(self.ROOM_SET)
        option = (By.XPATH,f"//android.widget.TextView[@text='{room_set}']")
        self.click(option)

    def select_room(self, room_name):
        self.click(self.ROOM_SPINNER)
        option = (By.XPATH,f"//android.widget.TextView[@text='{room_name}']")
        self.click(option)

    # 流程
    def change_room_set_and_room(self, room_set, room_name):
        self.scroll_to_element(self.ROOM_SET)
        time.sleep(3)
        self.select_room_set(room_set)
        self.select_room(room_name)
        self.click_play()

    # 驗證正確
    def is_page_displayed(self):
        pass