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

#Open URL
driver.get('https://www.amazon.com')

#Amazon Logo
driver.find_element(By.ID, 'nav-logobar')

#Email field
driver.find_element(By. XPATH, "//type[@name='email']")

#Continue Button
driver.find_element(By.ID, 'continue')

#Conditions of use link
driver.find_element(By.XPATH, "//a[@href='/gp/aw/help/ref=ap_mobile_signin_notification_condition_of_use?id=508088']")

#Privacy Notice link
driver.find_element(By.XPATH, "//a[@href='/gp/aw/help/ref=ap_mobile_signin_notification_privacy_notice?id=468496']")

#Need help link
driver.find_element(By.CLASS_NAME, 'a-expander-prompt')

#Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

#Other issues with Sign-In link
driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']")

#Create your Amazon account button
driver.find_element(By.CLASS_NAME, 'a-icon a-accordion-radio a-icon-radio-active')