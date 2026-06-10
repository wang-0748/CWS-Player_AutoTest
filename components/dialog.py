from selenium.webdriver.common.by import By
from utils.base_page import BasePage


class Dialog(BasePage):

    # Locators
    VIEW = (By.ID, "com.cayintech.cmswsplayer:id/dialog_view")
    TEXT = (By.ID, "com.cayintech.cmswsplayer:id/dialog_content")
    CONFIRM_BTN = (By.ID, "com.cayintech.cmswsplayer:id/confirm_button")


    def is_visible(self):
        return self.is_displayed(self.VIEW)

    def get_content_text(self):
        return self.get_text(self.TEXT)

    def close(self):
        self.click(self.CONFIRM_BTN)

    def is_error_message(self, expected_text=None):
        if expected_text:
            return expected_text in self.get_content_text()
        return self.is_visible()