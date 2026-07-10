from utils.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(BasePage):

    CONTENT_SPINNER = (By.ID, "com.cayintech.cmswsplayer:id/content_spinner")
    ACCOUNT_TEXT = (By.ID, "com.cayintech.cmswsplayer:id/account_text")
    ACCOUNT_STATUS = (By.ID, "com.cayintech.cmswsplayer:id/account_status_text")
    DEVICE_STATUS = (By.ID, "com.cayintech.cmswsplayer:id/registergocayin_btn")
    LOGOUT_BTN = (By.ID, "com.cayintech.cmswsplayer:id/logout_btn")

    # --- 🎯 device management 註冊狀態 ---
    STATUS_PENDING = "裝置註冊待審核"
    STATUS_SUCCESS = "已成功註冊"
    STATUS_FAILED = "註冊失敗"
    STATUS_OTHER = "請確認上次裝置是否有正確登出"

    def is_loaded(self):
        return self.wait.until(EC.presence_of_element_located(self.ACCOUNT_STATUS))

    def get_account_name(self):
        return self.get_text(self.ACCOUNT_TEXT)

    def get_login_account_status(self):
        return self.get_text(self.ACCOUNT_STATUS)

    def get_login_device_status(self):
        return self.get_text(self.DEVICE_STATUS)

    def select_content_type(self, content_name: str):
        spinner = self.wait.until(EC.element_to_be_clickable(self.CONTENT_SPINNER))
        spinner.click()
        self.driver.find_element(
            By.XPATH,
            f"//*[contains(@text,'{content_name}')]"
        ).click()

    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BTN)).click()