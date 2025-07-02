from behave import given, when, then
from appium.webdriver.common.appiumby import AppiumBy
from features.pages.wallet_page import WalletPage

@given('I launch Trust Wallet app')
def step_impl(context):
    context.wallet_page = WalletPage(context.driver)

@when('I tap Create New Wallet button')
def step_impl(context):
    context.wallet_page.tap_create_wallet()

@when('I set a secure passcode "{passcode}"')
def step_impl(context, passcode):
    context.wallet_page.set_passcode(passcode)

@when('I confirm the passcode "{passcode}"')
def step_impl(context, passcode):
    context.wallet_page.confirm_passcode(passcode)

@when('I choose Deny to biometric login')
def step_impl(context):
    context.wallet_page.deny_biometric()

@when('I tap Skip, I\'ll do it later')
def step_impl(context):
    context.wallet_page.tap_skip()

@then('I should see the message "{message}"')
def step_impl(context, message):
    message_locator = (AppiumBy.XPATH, f"//android.widget.TextView[@text='{message}']")
    assert context.wallet_page.is_element_present(*message_locator), f"Message '{message}' is not visible"
