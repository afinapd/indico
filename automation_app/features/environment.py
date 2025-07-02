import os
import logging
from appium import webdriver
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def before_all(context):
    load_dotenv()

def before_scenario(context, scenario):
    # Set up Appium capabilities
    capabilities = {
        'platformName': 'Android',
        'automationName': 'UiAutomator2',
        'deviceName': 'RR8R708RESJ',
        'app': os.path.join(os.getcwd(), 'apk', 'latest.apk'),
        'appPackage': 'com.wallet.crypto.trustapp',
        'appActivity': '.ui.app.AppActivity',
        'autoGrantPermissions': True,
        'fullReset': True,
        'app': os.path.join(os.getcwd(), 'apk', 'latest.apk')
    }
    
    # Initialize Appium driver
    options = UiAutomator2Options().load_capabilities(capabilities)
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
    context.driver.implicitly_wait(10)

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()

def after_all(context):
    pass
