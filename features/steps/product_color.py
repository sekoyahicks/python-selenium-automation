from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep

COLORS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open Target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(10)


@then('Verify product has color options')
def click_colors(context):
    expected_colors = ['Black', 'Olive Green', 'Silver', 'White', 'Light Blue', 'Light Green', 'Vibrant Pink']
    actual_colors = []

    colors = context.driver.find_elements(*COLORS)
    for color in colors:
        color.click()

        selected_color = context.driver.find_elements(*SELECTED_COLOR).text
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
