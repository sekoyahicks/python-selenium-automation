from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open URL
driver.get('https://www.amazon.com')

# Amazon logo
driver.find_element(By.CSS_SELECTOR, "#nav-main")

# Create account
driver.find_element(By.CSS_SELECTOR, ".a-icon")

# Name
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

# Email
driver.find_element(By.CSS_SELECTOR, "#ap_email")

# Password
driver.find_element(By.CSS_SELECTOR, "#ap_password")

# Password length requirement
driver.find_element(By.CSS_SELECTOR, "#passwordInformationMessage")

# Re-enter password
## Not shown in website

# Continue
driver.find_element(By.CSS_SELECTOR, "#continue")

# Conditions of use
driver.find_element(By.CSS_SELECTOR, "a[href*='href=ap_mobile_register_notification_condition_of_use']")

# Privacy notice
driver.find_element(By.CSS_SELECTOR, "a[href*='href=ap_mobile_register_notification_privacy_notice']")

# Sign in
driver.find_element(By.CSS_SELECTOR, ".a-accordion-radio")