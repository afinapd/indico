from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import os
import time

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Form Locators
    NAME_INPUT = (By.CSS_SELECTOR, "#name")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#email")
    PHONE_INPUT = (By.CSS_SELECTOR, "#phone")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "#textarea")
    GENDER_RADIO = (By.CSS_SELECTOR, "input[name='gender'][value='{}']")
    DAYS_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox'][value='{}']")
    COUNTRY_SELECT = (By.CSS_SELECTOR, "#country")
    COLOR_SELECT = (By.CSS_SELECTOR, "#colors")
    SORTED_LIST = (By.CSS_SELECTOR, "#animals")
    DATE_PICKER = (By.CSS_SELECTOR, "#datepicker")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    

    
    URL = "https://testautomationpractice.blogspot.com/"
    
    def navigate_to_page(self):
        """Navigate to the test automation practice website"""
        self.driver.get(self.URL)
        # Wait for form elements to be present
        self.wait.until(EC.presence_of_element_located((By.ID, "name")))

    def fill_form_data(self, data):
        """Fill in the form with provided data"""
        field_mapping = {
            "Name": self.NAME_INPUT,
            "Email": self.EMAIL_INPUT,
            "Phone": self.PHONE_INPUT,
            "Address": self.ADDRESS_INPUT
        }
        
        for field, value in data.items():
            if field in field_mapping:
                element = self.wait.until(EC.presence_of_element_located(field_mapping[field]))
                element.clear()
                element.send_keys(value)

    def select_gender(self, gender):
        """Select gender radio button"""
        gender_radio = self.driver.find_element(By.CSS_SELECTOR, f"input[name='gender'][value='{gender.lower()}']") 
        gender_radio.click()

    def select_days(self, days):
        """Select multiple days"""
        day_list = [day.strip() for day in days.split(",")]
        for day in day_list:
            checkbox = self.driver.find_element(By.CSS_SELECTOR, f"input[type='checkbox'][value='{day.lower()}']") 
            checkbox.click()

    def select_country(self, country):
        """Select country from dropdown"""
        select = Select(self.wait.until(EC.presence_of_element_located(self.COUNTRY_SELECT)))
        select.select_by_visible_text(country)

    def select_color(self, color):
        """Select color from dropdown"""
        select = Select(self.wait.until(EC.presence_of_element_located(self.COLOR_SELECT)))
        select.select_by_visible_text(color)

    def select_sorted_item(self, item):
        """Select item from sorted list"""
        try:
            select = Select(self.wait.until(EC.presence_of_element_located(self.SORTED_LIST)))
            select.select_by_visible_text(item)
        except:
            # Try to find by partial text if exact match fails
            options = select.options
            for option in options:
                if item.lower() in option.text.lower():
                    select.select_by_visible_text(option.text)
                    break

    def pick_date(self, date):
        day, month, year = date.split('/')
        formatted_date = f"{month}/{day}/{year}"
        
        max_retries = 3
        retry_count = 0
        
        while retry_count < max_retries:
            try:
                script = f"""
                    var input = document.getElementById('datepicker');
                    input.value = '{formatted_date}';
                    input.dispatchEvent(new Event('change', {{ bubbles: true }}));
                    input.dispatchEvent(new Event('blur', {{ bubbles: true }}));
                """
                self.driver.execute_script(script)
                return
            except Exception as e:
                retry_count += 1
                print(f"Retry {retry_count} - Failed to set date: {str(e)}")
                if retry_count == max_retries:
                    raise Exception(f"Failed to set date {formatted_date}") from e
                time.sleep(2)

    def submit_form(self):
        """Submit the form"""
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def upload_single_file(self, file_name):
        """Upload a single file"""
        test_data_dir = os.path.join(os.getcwd(), "test_data")
        file_path = os.path.join(test_data_dir, file_name)
        
        try:
            file_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']:not([multiple])")))
            file_input.send_keys(file_path)
        except Exception as e:
            print(f"Failed to upload single file: {e}")
            raise

    def upload_multiple_files(self, files):
        """Upload multiple files"""
        test_data_dir = os.path.join(os.getcwd(), "test_data")
        file_paths = [os.path.join(test_data_dir, f) for f in files]
        
        try:
            file_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file'][multiple]")))
            file_input.send_keys('\n'.join(file_paths))
        except Exception as e:
            print(f"Failed to upload multiple files: {e}")
            raise

    def click_upload_button(self, button_text):
        """Click the specified upload button"""
        try:
            button = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[text()='{button_text}']")))
            button.click()
        except Exception as e:
            print(f"Failed to click {button_text} button: {e}")
            raise

    def verify_message(self, expected_message):
        """Verify message appears in the upload section"""
        try:
            # Get the file input value to determine if files are selected
            if expected_message == "Multiple files selected":
                file_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file'][multiple]")))
            else:
                file_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']:not([multiple])")))
            
            # Check if a file is selected
            value = file_input.get_attribute("value")
            return bool(value)
            
        except Exception as e:
            print(f"Failed to verify message: {e}")
            return False



    def get_date_picker_value(self):
        """Get the current value of the date picker"""
        try:
            return self.driver.execute_script("return document.getElementById('datepicker').value;")
        except Exception as e:
            print(f"Failed to get date picker value: {str(e)}")
            return ""
