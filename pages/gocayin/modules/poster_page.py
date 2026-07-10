from selenium.webdriver.common.by import By
from utils.base_page import BasePage


class PosterPage(BasePage):
    POSTER_SET = (By.ID, "com.cayintech.cmswsplayer:id/gocayin_poster_spinner")
    PLAY_BUTTON = (By.ID, "com.cayintech.cmswsplayer:id/play_btn")

    def select_poster_set(self, room_set):
        self.click(self. POSTER_SET)
        option = (By.XPATH, f"//android.widget.TextView[@text='{room_set}']")
        self.click(option)

    def click_play(self):
        self.click(self.PLAY_BUTTON)