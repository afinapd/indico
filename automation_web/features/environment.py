from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import shutil

def before_all(context):
    """Initialize test environment and WebDriver before all tests"""
    # Create test files directory
    context.test_files_dir = os.path.join(os.getcwd(), "test_files")
    os.makedirs(context.test_files_dir, exist_ok=True)
    
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920,1080')
    
    # Let Selenium handle ChromeDriver installation
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()

def after_all(context):
    """Clean up test environment after all tests"""
    # Clean up test files directory
    if hasattr(context, 'test_files_dir') and os.path.exists(context.test_files_dir):
        shutil.rmtree(context.test_files_dir)

def before_scenario(context, scenario):
    """Reset browser state before each scenario"""
    context.driver.delete_all_cookies()
    context.driver.refresh()

def after_scenario(context, scenario):
    """Take screenshot on failure"""
    if scenario.status == "failed":
        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{scenario.name.replace(' ', '_')}.png")
        context.driver.save_screenshot(screenshot_path)
    
    # Create test files directory
    context.test_files_dir = os.path.join(os.getcwd(), "test_files")
    os.makedirs(context.test_files_dir, exist_ok=True)

def after_all(context):
    """Clean up WebDriver and test environment after all tests"""
    if hasattr(context, 'driver'):
        context.driver.quit()
    
    # Clean up test files directory
    if hasattr(context, 'test_files_dir') and os.path.exists(context.test_files_dir):
        shutil.rmtree(context.test_files_dir)

def before_scenario(context, scenario):
    """Initialize scenario-specific resources"""
    # Reset browser state
    context.driver.delete_all_cookies()
    context.driver.refresh()

def after_scenario(context, scenario):
    """Clean up scenario-specific resources"""
    # Take screenshot on failure
    if scenario.status == "failed":
        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{scenario.name.replace(' ', '_')}.png")
        context.driver.save_screenshot(screenshot_path)
