from selenium.webdriver.common.by import By
from behave import then
from selenium.webdriver.support import expected_conditions as EC
from behave import then, when
from time import sleep


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
# IMAGE_COLOR = (By.CSS_SELECTOR, "['']")


@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com')


@when('Search for {product}')
def search_product(context, product):
    # find search field and enter text
    context.driver.find_element(By.ID, 'search').send_keys(product)
    # click search
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    # wait for the page with search results to load
    context.driver.wait.until(EC.visibility_of_element_located(ADD_TO_CART_BTN))
    sleep(7)


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='chooseOptionsButton']").click()
    # context.driver.find_elements(By.CSS_SELECTOR, "[id*='addToCartButton']")[0].click()
    context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME))


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print(f'Product stored: {context.product_name}')


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    sleep(6)


@when('Open cart page')
def open_target(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify search results shown for {expected_product}')
def verify_search_results(context, expected_product):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
    assert expected_product in actual_text, f'Expected {expected_product} not in actual {actual_text}'
    sleep(7)


@then('Verify correct search results URL opens for {expected_product}')
def verify_url(context, expected_product):
    url = context.driver.current_url
    assert expected_product in url, f'Expected {expected_product} not in {url}'