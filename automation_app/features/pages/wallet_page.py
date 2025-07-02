from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage

class WalletPage(BasePage):
    # Locators
    CREATE_WALLET_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Create new wallet')]")
    DENY_BIOMETRIC = (AppiumBy.XPATH, "//android.widget.TextView[@text='Deny']")
    SKIP_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Skip')]")

    
    def tap_create_wallet(self):
        self.click_element(*self.CREATE_WALLET_BUTTON)
        
    def set_passcode(self, passcode):
        self.logger.info(f"Setting passcode: {passcode}")
        for digit in passcode:
            # Define locator for each number button
            number_button = (AppiumBy.XPATH, f"//android.widget.TextView[@text='{digit}']")            
            self.click_element(*number_button)
    
    def confirm_passcode(self, passcode):
        self.set_passcode(passcode)  # Reuse the same method since it's the same keypad
    
    def deny_biometric(self):
        # Wait for biometric dialog to appear
        self.logger.info("Waiting for biometric dialog...")
        import time
        time.sleep(5)  # Wait 5 seconds for animation and dialog
        self.click_element(*self.DENY_BIOMETRIC)
    
    def tap_skip(self):
        self.click_element(*self.SKIP_BUTTON)
    

