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

driver.get(' https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&prevRID=9K9WQ64B0JXQAHNNZD2Q&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

#logo
driver.find_element(By.CSS_SELECTOR, '.a-icon-logo')

#create account
driver.find_element(By.CSS_SELECTOR, '.a-spacing-small')

#your name
driver.find_element(By.CSS_SELECTOR, '.auth-autofocus.auth-required-field')

#email
driver.find_element(By.CSS_SELECTOR, '.a-spacing-micro.auth-required-field.auth-require-claim-validation')

#password
driver.find_element(By.CSS_SELECTOR, '.auth-required-field.auth-require-fields-match.auth-require-password-validation')

#password length
driver.find_element(By.CSS_SELECTOR, '.a-alert-content')

#reenter password
driver.find_element(By.CSS_SELECTOR, '.auth-required-field.auth-require-fields-match')

#create your account
driver.find_element(By.CSS_SELECTOR, '.a-button-input')

#conditions of use and privacy notice
driver.find_element(By.CSS_SELECTOR, '.a-row.a-spacing-top-medium.a-size-small')

#sign in
driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis')
