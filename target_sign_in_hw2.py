from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get('https://www.target.com/')

# click SignIn Button
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()

#Verify
# expected = 'Sign into Target account'
# actual = driver.find_element(By.XPATH, "//h1[(@class, 'accountNav-signIn']").text
