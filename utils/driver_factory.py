from appium import webdriver
from appium.options.android import UiAutomator2Options


def create_driver():

    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "Android"

    options.app_package = "com.cayintech.cmswsplayer"
    options.app_activity = ".activity.StartActivity"

    options.no_reset = False

    options.set_capability("skipDeviceInitialization", True)
    options.set_capability("ignoreHiddenApiPolicyError", True)

    return webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )