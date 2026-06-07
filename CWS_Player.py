from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = UiAutomator2Options()

options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "Android"

options.app_package = "com.cayintech.cmswsplayer"
options.app_activity = ".activity.StartActivity"

options.no_reset = True

# 開啟app
options.set_capability("skipDeviceInitialization", True)
options.set_capability("ignoreHiddenApiPolicyError", True)

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)

print("App launched successfully!")

time.sleep(5)

# 點設定按鈕
setting_btn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.ID, "com.cayintech.cmswsplayer:id/setting_btn")
    )
)
setting_btn.click()

# 輸入驗證碼(0000)
for i in range (4):
    key_0 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "com.cayintech.cmswsplayer:id/keyboard_0")
        )
    )
    key_0.click()

driver.quit()