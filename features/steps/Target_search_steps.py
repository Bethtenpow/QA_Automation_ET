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
    assert 'Your cart is empty' == actual_text, f"expected 'Your cart is empty' but got {actual_text}"


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



@when('Click Target Circle')
def click_target_circle(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/GlobalHeader/UtilityHeader/TargetCircle']").click()


@then('Verify there are 5 Benefits to Target Circle')
def verify_benefits_to_target(context):
    benefits_to_target = context.driver.find_elements(By.CSS_SELECTOR, "li[class*='BenefitCard']")
    assert len(benefits_to_target) == 5, f"expected '5' but got {len(benefits_to_target)}"


@when ('Search for {product}')
def search_product(context, product):
    print(product)
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()


@when ('Click on Add to cart button')
def click_on_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='chooseOptionsButton']").click()

    sleep(3)


@when ('Confirm Add to cart on side navigation')
def click_on_side_navigation(context):
    context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButton']").click()


@when('View Cart and check out')
def view_cart_checkout(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='styles__ButtonSecondary']").click()


@then('Verify items are in cart')
def verify_items_in_cart(context):
    items = context.driver.find_elements(By.CSS_SELECTOR, "[class*='styles__CartSummary']")
    assert 'items in cart' == items[0].text, f"Expected 'items in cart' but got {items[0].text}"

