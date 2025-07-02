from behave import given, when, then
from features.pages.registration_page import RegistrationPage
import os

@given('I open the registration form page')
def step_impl(context):
    context.registration_page = RegistrationPage(context.driver)
    context.registration_page.navigate_to_page()

@when('I fill in the form with dummy profile data "{field}" with "{value}"')
def step_impl(context, field, value):
    data = {field: value}
    context.registration_page.fill_form_data(data)

@when('I select gender as "{gender}"')
def step_impl(context, gender):
    context.registration_page.select_gender(gender)

@when('I select the days: "{days}"')
def step_impl(context, days):
    context.registration_page.select_days(days)

@when('I select country as "{country}"')
def step_impl(context, country):
    context.registration_page.select_country(country)

@when('I select color as "{color}"')
def step_impl(context, color):
    context.registration_page.select_color(color)

@when('I select sorted list item "{item}"')
def step_impl(context, item):
    context.registration_page.select_sorted_item(item)

@when('I pick "{date}" on Date Picker')
def step_impl(context, date):
    context.registration_page.pick_date(date)

@when('I click the Submit button')
def step_impl(context):
    context.registration_page.submit_form()

@given('I open the file upload section')
def step_impl(context):
    context.registration_page = RegistrationPage(context.driver)
    context.registration_page.navigate_to_page()

@when('I choose "{file_name}" to upload')
def step_impl(context, file_name):
    context.registration_page.upload_single_file(file_name)

@when('I choose the files "{file_names}" to upload')
def step_impl(context, file_names):
    files = [f.strip() for f in file_names.split(',')]
    context.registration_page.upload_multiple_files(files)

@when('I click the "{button_text}" button')
def step_impl(context, button_text):
    context.registration_page.click_upload_button(button_text)

@then('I should see "{expected_date}" on Date Picker')
def step_impl(context, expected_date):
    actual_date = context.registration_page.get_date_picker_value()
    assert actual_date == expected_date, f"Expected {expected_date} but got {actual_date}"



@then('I should see message "{expected_message}"')
def step_impl(context, expected_message):
    assert context.registration_page.verify_message(expected_message)
    
    # Clean up test file
    if hasattr(context, 'test_file_path') and os.path.exists(context.test_file_path):
        os.remove(context.test_file_path)
