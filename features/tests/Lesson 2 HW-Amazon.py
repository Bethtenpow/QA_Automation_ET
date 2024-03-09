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

driver.get('https://www.amazon.com/sign-in')
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
driver.find_element(By.XPATH, "//input[@id='ap_email']")
driver.find_element(By.XPATH, "//input[@aria-labelledby='continue-announce']")

#note: I do not think these searches for 'Conditions of Use' and 'Privacy Notice' are correct and I am having issues with finding links

#driver.find_element(By.XPATH, "//a[@href=/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&amp;nodeId=508088'>Conditions of Use</a>']")
#driver.find_element(By.XPATH, "//a[@href=/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&amp;nodeId=468496>Privacy Notice</a>']")

driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")
driver.find_element(By.XPATH, "//a[@class='a-link-normal']")
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")

sleep(4)
