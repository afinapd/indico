from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import logging

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)  # Increase timeout to 30 seconds
        self.logger = logging.getLogger(__name__)
    
    def find_element(self, locator_type, locator_value):
        return self.wait.until(
            EC.presence_of_element_located((locator_type, locator_value))
        )
    
    def find_elements(self, locator_type, locator_value):
        return self.wait.until(
            EC.presence_of_all_elements_located((locator_type, locator_value))
        )
    
    def click_element(self, locator_type, locator_value):
        self.logger.info(f"Attempting to click element with locator: {locator_type}={locator_value}")
        try:
            # First try to find if element exists
            element = self.wait.until(
                EC.presence_of_element_located((locator_type, locator_value))
            )
            self.logger.info("Element found, waiting for it to be clickable")
            
            # Then wait for it to be clickable
            clickable = self.wait.until(
                EC.element_to_be_clickable((locator_type, locator_value))
            )
            self.logger.info("Element is clickable, attempting to click")
            
            # Try to click
            clickable.click()
            self.logger.info("Element clicked successfully")
        except Exception as e:
            self.logger.error(f"Failed to click element: {str(e)}")
            # Take screenshot
            self.driver.save_screenshot('error_screenshot.png')
            raise
    
    def send_keys(self, locator_type, locator_value, text):
        element = self.find_element(locator_type, locator_value)
        element.clear()
        element.send_keys(text)
    
    def is_element_present(self, locator_type, locator_value, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((locator_type, locator_value))
            )
            return True
        except TimeoutException:
            return False
