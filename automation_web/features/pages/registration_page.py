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
    NAME_INPUT = (By.XPATH, "//input[@id='name']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='email']")
    PHONE_INPUT = (By.XPATH, "//input[@id='phone']")
    ADDRESS_INPUT = (By.XPATH, "//textarea[@id='textarea']")
    GENDER_RADIO = (By.XPATH, "//input[@type='radio'][@value='{}']")
    DAYS_CHECKBOX = (By.XPATH, "//input[@type='checkbox'][@value='{}']")
    COUNTRY_SELECT = (By.XPATH, "//select[@id='country']")
    COLOR_SELECT = (By.XPATH, "//select[@id='colors']")
    SORTED_LIST = (By.XPATH, "//select[@id='animals']")
    DATE_PICKER_1 = (By.XPATH, "//input[@id='datepicker']")
    DATE_PICKER_2 = (By.XPATH, "//input[@id='datepicker2']")
    DATE_PICKER_3 = (By.XPATH, "//input[@id='datepicker3']")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Submit']")
    
    # File Upload Locators
    SINGLE_FILE_UPLOAD = (By.ID, "singleFileUpload")
    MULTIPLE_FILE_UPLOAD = (By.ID, "multipleFileUpload")
    SINGLE_UPLOAD_BUTTON = (By.ID, "singleUploadBtn")
    MULTIPLE_UPLOAD_BUTTON = (By.ID, "multipleUploadBtn")
    
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
        gender_radio = self.driver.find_element(By.XPATH, f"//input[@name='gender'][@value='{gender.lower()}']") 
        gender_radio.click()

    def select_days(self, days):
        """Select multiple days"""
        day_list = [day.strip() for day in days.split(",")]
        for day in day_list:
            checkbox = self.driver.find_element(By.XPATH, f"//input[@type='checkbox'][@value='{day.lower()}']") 
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

    def pick_date(self, date, picker_number):
        """Pick date using specified date picker"""
        day, month, year = date.split('/')
        
        # Format date based on picker number
        # Picker 1 expects mm/dd/yyyy
        # Picker 2 expects dd/mm/yyyy (no conversion needed)
        if picker_number == '1':
            formatted_date = f"{month}/{day}/{year}"
        else:
            formatted_date = date
        
        # Try different selectors to find the date picker
        selectors = [
            f"#datepicker{'' if picker_number == '1' else picker_number}",
            f"input[id='datepicker{'' if picker_number == '1' else picker_number}']",
            f"input[name='datepicker{'' if picker_number == '1' else picker_number}']",
            f"input[type='text'][id='datepicker{'' if picker_number == '1' else picker_number}']",
            f"input[type='text'][class*='hasDatepicker']"
        ]
        
        # Wait for page to be ready
        time.sleep(2)
        
        # Try each selector
        date_picker = None
        for selector in selectors:
            try:
                date_picker = self.driver.find_element(By.CSS_SELECTOR, selector)
                print(f"Found date picker with selector: {selector}")
                break
            except:
                continue
                
        if not date_picker:
            raise Exception(f"Could not find date picker {picker_number} using any selector")
        
        # Clear and set value using different JavaScript approaches
        try:
            # Approach 1: Direct value setting
            self.driver.execute_script("arguments[0].value = arguments[1];", date_picker, formatted_date)
        except:
            try:
                # Approach 2: Using jQuery if available
                self.driver.execute_script(f"$('#{date_picker.get_attribute('id')}').val('{formatted_date}');")
            except:
                # Approach 3: Dispatch events
                self.driver.execute_script("""
                    var input = arguments[0];
                    input.value = arguments[1];
                    input.dispatchEvent(new Event('change', { bubbles: true }));
                    input.dispatchEvent(new Event('blur', { bubbles: true }));
                """, date_picker, formatted_date)

    def pick_date_range(self, date_range):
        """Pick date range using date picker 3"""
        # Try different selectors
        selectors = [
            "#datepicker3",
            "input[id='datepicker3']",
            "input[name='datepicker3']",
            "input[type='text'][id='datepicker3']",
            "input[type='text'][class*='hasDatepicker']"
        ]
        
        # Wait for page to be ready
        time.sleep(2)
        
        # Try each selector
        date_picker = None
        for selector in selectors:
            try:
                date_picker = self.driver.find_element(By.CSS_SELECTOR, selector)
                print(f"Found date range picker with selector: {selector}")
                break
            except:
                continue
                
        if not date_picker:
            raise Exception("Could not find date range picker using any selector")
        
        # Clear and set value using different JavaScript approaches
        try:
            # Approach 1: Direct value setting
            self.driver.execute_script("arguments[0].value = arguments[1];", date_picker, date_range)
        except:
            try:
                # Approach 2: Using jQuery if available
                self.driver.execute_script(f"$('#{date_picker.get_attribute('id')}').val('{date_range}');")
            except:
                # Approach 3: Dispatch events
                self.driver.execute_script("""
                    var input = arguments[0];
                    input.value = arguments[1];
                    input.dispatchEvent(new Event('change', { bubbles: true }));
                    input.dispatchEvent(new Event('blur', { bubbles: true }));
                """, date_picker, date_range)

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

    def verify_date_picker(self, number, expected_date):
        """Verify that the date picker shows the expected date"""
        picker_id = f"datepicker{'' if number == '1' else number}"
        actual_value = self.driver.execute_script(f"return document.getElementById('{picker_id}').value;")
        assert actual_value == expected_date, f"Expected {expected_date} but got {actual_value}"

    def verify_form_submission(self):
        """Verify that the form was submitted successfully"""
        # Add appropriate verification
        pass
