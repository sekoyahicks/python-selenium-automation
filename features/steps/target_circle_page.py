from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify {number} links')
def verify_10_benefit_links(context, number):
    number = int(number)
    links = context.driver.find_elements(By.CSS_SELECTOR, "[href='/icons/ArrowRight.svg#ArrowRight']")
    assert len(links) == number, f'Expected {number} links but got {len(links)}'


