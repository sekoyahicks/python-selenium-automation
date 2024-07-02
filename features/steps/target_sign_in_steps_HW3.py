from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target')
def open_target(context):
    context.driver.get('https://www.target.com')


@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[aria-label='Account, sign in']").click()


@when('Click Sign In from side nav')
def click_sign_in_from_side_nav(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()


@then('Verify Sign In form opened')
def verify_sign_in_form_opened(context):
    expected_text = 'Sign into your Target Account'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, ".styles__StyledHeading-sc-1awz1yh-0").text
    assert expected_text in actual_text, f'Expected {expected_text} not in actual_text: {actual_text}'

# I do not understand why verify step fails


sleep(6)
