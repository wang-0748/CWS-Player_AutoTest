from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from utils.base_page import BasePage

class CmsWsMainPage(BasePage):

    CHANGE_BTN = (By.ID, "com.cayintech.cmswsplayer:id/change_btn")
    GROUP_SPINNER = (By.ID, "com.cayintech.cmswsplayer:id/group_spinner")
    HOSTNAME_INPUT = (By.ID, "com.cayintech.cmswsplayer:id/hostname_edit_text")
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

    def select_group(self, group_name):
        self.click(self.GROUP_SPINNER)
        option = (By.XPATH, f"//android.widget.TextView[@text='{group_name}']")
        self.click(option)

    def input_hostname(self, hostname):
        self.input_text(self.HOSTNAME_INPUT, hostname)

    def is_hostname_required_error(self):
        return "這個欄位不能是空的" in self.driver.page_source

    # 流程
    def change_group_and_hostname(self, group, hostname):
        self.scroll_to_element(self.GROUP_SPINNER)
        self.input_hostname(hostname)
        self.select_group(group)
        self.click_play()

    # 驗證正確
    def is_page_displayed(self):
        pass