from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class PasswordPage(BasePage):

    BACK_BTN = (
        By.ID,
        "com.cayintech.cmswsplayer:id/left_btn"
    )

    DELETE_BTN = (
        By.ID,
        "com.cayintech.cmswsplayer:id/pin_code_delete"
    )

    PASSWORD_IMG_1 = (
        By.ID,
        "com.cayintech.cmswsplayer:id/password_img1"
    )

    PASSWORD_IMG_2 = (
        By.ID,
        "com.cayintech.cmswsplayer:id/password_img2"
    )

    PASSWORD_IMG_3 = (
        By.ID,
        "com.cayintech.cmswsplayer:id/password_img3"
    )

    PASSWORD_IMG_4 = (
        By.ID,
        "com.cayintech.cmswsplayer:id/password_img4"
    )

    ERROR_TEXT = (
        By.ID,
        "com.cayintech.cmswsplayer:id/error_text"
    )

    def click_delete(self):
        self.click(self.DELETE_BTN)

    def click_back(self):
        self.click(self.BACK_BTN)

    def get_error_message(self):
        return self.get_text(self.ERROR_TEXT)


    def is_locked(self):
        return "嘗試次數過多" in self.get_error_message()

    def is_pin_page_displayed(self):
        return self.is_displayed(self.PASSWORD_IMG_1)

    def has_error_message(self):
        return self.get_error_message() == "錯誤的PIN碼"

    def enter_password(self, password):

        for digit in password:

            key_locator = (
                By.ID,
                f"com.cayintech.cmswsplayer:id/keyboard_{digit}"
            )

            self.click(key_locator)
