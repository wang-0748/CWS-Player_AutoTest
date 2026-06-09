from selenium.webdriver.common.by import By
from utils.base_page import BasePage


class SettingPage(BasePage):

    # 共用導航
    BACK_BTN = (By.ID, "com.cayintech.cmswsplayer:id/left_btn")
    PLAYBACK_TAB = (By.ID, "com.cayintech.cmswsplayer:id/playback")
    ADVANCE_TAB = (By.ID, "com.cayintech.cmswsplayer:id/advance")
    MENU_BTN = (By.ID, "com.cayintech.cmswsplayer:id/right_btn")
    # TODO
    # open_menu()
    # open_reset_pin()
    # open_privacy_policy()
    # open_terms()

    # 共用入口
    PRODUCT_MODEL_SPINNER = (By.ID, "com.cayintech.cmswsplayer:id/text1")

    # actions
    def click_back(self):
        self.click(self.BACK_BTN)

    def switch_tab(self, tab_name):
        tabs = {
            "playback": self.PLAYBACK_TAB,
            "advance": self.ADVANCE_TAB,
        }

        if tab_name not in tabs:
            raise ValueError(f"Unknown tab: {tab_name}")

        self.click(tabs[tab_name])

    def select_model(self, model_name):
        self.click(self.PRODUCT_MODEL_SPINNER)

        option = (
            By.XPATH,
            f"//android.widget.ListView//android.widget.TextView[@text='{model_name}']"
        )

        self.wait_for(option)
        self.click(option)

    def open_menu(self):
        self.click(self.MENU_BTN)

    def select_menu_item(self, item_name):
        self.open_menu()

        option = (
            By.XPATH,
            f"//android.widget.TextView[@text='{item_name}']"
        )

        self.click(option)
