from selenium.webdriver.common.by import By
from utils.base_page import BasePage

class MeetingPostPage(BasePage):
    ROOM_SET = (By.ID, "com.cayintech.cmswsplayer:id/gocayin_room_room_set_spinner")
    ROOM_SPINNER = (By.ID, "com.cayintech.cmswsplayer:id/gocayin_room_spinner")
    PLAY_BUTTON = (By.ID,"com.cayintech.cmswsplayer:id/play_btn")

    def select_room_set(self, room_set):
        self.click(self.ROOM_SET)
        option = (By.XPATH,f"//android.widget.TextView[@text='{room_set}']")
        self.click(option)

    def select_room(self, room_name):
        self.click(self.ROOM_SPINNER)
        option = (By.XPATH,f"//android.widget.TextView[@text='{room_name}']")
        self.click(option)

    def click_play(self):
        self.click(self.PLAY_BUTTON)