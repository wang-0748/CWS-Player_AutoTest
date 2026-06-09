from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # -----------------------
    # Wait 層
    # -----------------------
    def wait_for(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    # -----------------------
    # Action 層
    # -----------------------
    def click(self, locator):
        element = self.wait_for_clickable(locator)
        element.click()

    def input_text(self, locator, text):
        element = self.wait_for_clickable(locator)
        element.clear()
        element.send_keys(text)

    # -----------------------
    # Find / Get
    # -----------------------
    def find(self, locator):
        return self.wait_for(locator)

    def get_text(self, locator):
        return self.find(locator).text

    def get_attribute(self, locator, attribute):
        return self.find(locator).get_attribute(attribute)

    # -----------------------
    # State check
    # -----------------------
    def is_displayed(self, locator):
        try:
            return self.wait_for(locator).is_displayed()
        except TimeoutException:
            return False

    # -----------------------
    # Utility: click by text
    # -----------------------
    def click_text(self, locator, text):
        elements = self.driver.find_elements(*locator)

        for el in elements:
            if el.text == text:
                el.click()
                return

        raise Exception(f"Cannot find text: {text}")