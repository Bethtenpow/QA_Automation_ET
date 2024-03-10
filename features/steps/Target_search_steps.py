from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')


@when('Click on the Shopping cart')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()


@then('verify “Your cart is empty” message is shown')
def verify_cart_empty_message(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR,  "h1[class*='StyledHeading']").text
    assert 'your cart is empty' == actual_text, f"expected 'your cart is empty' but got {actual_text}"


@when('Click sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()


@when('From right side navigation menu, click Sign In')
def right_click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()


@then('Verify Sign in form opened')
def verify_sign_in_form(context):
    sign_in_message = context.driver.find_element(By.CSS_SELECTOR, "[data-test='content-wrapper']").text
    assert 'Sign into your Target account' == sign_in_message, f"expected 'Sign into your Target account' but got {sign_in_message}"

