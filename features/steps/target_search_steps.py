from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[id='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By. CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")


@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com')


@when('Search for {product}')
def search_product(context, product):
    # find search field and enter text
    context.driver.find_element(By.ID, 'search').send_keys(product)
    # click search
    context.driver.find_element(By.XPATH, "//button[@aria-label='search']").click()
    # wait for the page with search results to load


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='chooseOptionsButton']").click()
    # context.driver.find_elements(By.CSS_SELECTOR, "[id*='addToCartButton']")[0].click()
    sleep(4)


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print(f'Product stored: {context.product_name}')


@when('Confirm Add to Cart Button')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    sleep(6)


@when('Open cart page')
def open_target(context):
    context.driver.get('https://www.target.com/cart')


sleep(6)

#The code failed at step 3 in second scenario. I have no idea what is wrong.

#Rough draft
# def add_to_cart(context):
#     context.driver.find_element(*ADD_TO_CART_BUTTON).click()
#     sleep(4)
#
#
# @when('Confirm Add to Cart button')
# def confirm_add_to_cart(context):
#     context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()


# sleep(6)


# @when('Add shirt to cart')
# def click_product(context):
#     context.driver.find_element(By.ID, "[id='addToCartButtonOrTextIdFor14450618']").click()
#     sleep(6)


# @then('Verify {product} is added to cart')
# def verify_search_results(context, product):
#     expected_text = ''
#     actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
#     assert expected_text in actual_text, f'Expected {expected_text} not in actual_text: {actual_text}'
