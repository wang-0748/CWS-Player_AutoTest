
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.base_page import BasePage


class GoCayinPage(BasePage):

    # === locators ===
    LOGIN_BTN = (By.ID, "com.cayintech.cmswsplayer:id/login_btn")
    PLAY_BTN = (By.ID, "com.cayintech.cmswsplayer:id/play_btn")

    def click_login(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BTN))
        btn.click()

    def click_play(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.PLAY_BTN))
        btn.click()

    def is_loaded(self):
        return self.wait.until(EC.presence_of_element_located(self.LOGIN_BTN))