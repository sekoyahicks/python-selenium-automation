from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target home page')
def open_target(context):
    context.driver.get('https://www.target.com')


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()
    # context.driver.find_element(By.CSS_SELECTOR, ".sc-e487bf3b-0.bYXfno.fRitwa").click()


@then('Verify "Your cart is empty"')
def verify_cart_empty(context):
    context.driver.find_element(By.CSS_SELECTOR)
    expected_text = 'Your Cart is empty'
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_text in actual_text, f'Expected {expected_text} not in actual_text: {actual_text}'


sleep(6)
