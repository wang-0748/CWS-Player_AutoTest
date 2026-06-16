from utils.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(BasePage):

    CONTENT_SPINNER = (By.ID, "com.cayintech.cmswsplayer:id/content_spinner")
    ACCOUNT_TEXT = (By.ID, "com.cayintech.cmswsplayer:id/account_text")
    ACCOUNT_STATUS = (By.ID, "com.cayintech.cmswsplayer:id/account_status_text")
    LOGOUT_BTN = (By.ID, "com.cayintech.cmswsplayer:id/logout_btn")  # 如果有

    def is_loaded(self):
        return self.wait.until(EC.presence_of_element_located(self.ACCOUNT_STATUS))

    def get_account_name(self):
        return self.find(self.ACCOUNT_TEXT).text

    def get_login_status(self):
        return self.find(self.ACCOUNT_STATUS).text

    def select_content_type(self, content_name: str):
        spinner = self.wait.until(EC.element_to_be_clickable(self.CONTENT_SPINNER))
        spinner.click()
        self.driver.find_element(
            By.XPATH,
            f"//*[contains(@text,'{content_name}')]"
        ).click()

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BTN)).click()