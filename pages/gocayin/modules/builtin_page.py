from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from utils.base_page import BasePage

class BuiltInPage(BasePage):
    BUILTIN_SET = (By.ID, "com.cayintech.cmswsplayer:id/gocayin_playlist_spinner")
    PREVIEW_IMAGE = (By.ID, "com.cayintech.cmswsplayer:id/gocayin_playlist_img")
    PLAY_BUTTON = (By.ID, "com.cayintech.cmswsplayer:id/play_btn")

    def select_builtin_set(self, room_set):
        self.click(self. BUILTIN_SET)
        option = (By.XPATH, f"//android.widget.TextView[@text='{room_set}']")
        self.click(option)

    def click_play(self):
        self.click(self.PLAY_BUTTON)

    def is_preview_displayed(self):
        return self.is_displayed(self.PREVIEW_IMAGE)

    # 往下滑動作(找完後不要加點擊的動作，很容易因為畫面還沒穩定，導致點擊失敗)
    def scroll_to_element(self, locator):
        by, value = locator

        if by == By.ID:
            uiautomator_cmd = (
                f'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                f'.scrollIntoView(new UiSelector().resourceId("{value}").instance(0));'
            )
        else:
            uiautomator_cmd = (
                f'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                f'.scrollIntoView(new UiSelector().text("{value}").instance(0));'
            )

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, uiautomator_cmd)