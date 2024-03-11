from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open Target main page')
def open_target_main(context):
    #context.driver.get('https://www.target.com/')
    context.app.main_page.open_main()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product()


@when('Click on the Shopping cart')
def click_cart(context):
    context.app.header.click_cart_icon()



@then('verify “Your cart is empty” message is shown')
def verify_cart_empty_message(context):
    context.app.cart_page.verify_cart_empty_message()


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


@then('Search results for {expected_result} are shown')
def verify_search_results_correct(context, expected_result):
    context.app.search_results_page.verify_search_results_correct()


@then('Page URL has search term {expected_part_url}')
def verify_search_results_page_url(context, expected_part_url):
    context.app.search_results_page.verify_search_results_page_url(expected_part_url)


@when('Click on Add to cart button')
def click_on_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='chooseOptionsButton']").click()


@when('Confirm Add to cart on side navigation')
def click_on_side_navigation(context):
    context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButton']").click()


@when('View Cart and check out')
def view_cart_checkout(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='styles__ButtonSecondary']").click()


@then('Verify items are in cart')
def verify_items_in_cart(context):
    items = context.driver.find_elements(By.CSS_SELECTOR, "[class*='styles__CartSummary']")
    assert 'items in cart' == items[0].text, f"Expected 'items in cart' but got {items[0].text}"


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Black', 'Brown', 'Cream']
    actual_colors = []

    colors = context.driver.find_elements(By.CSS_SELECTOR, "[class*='ButtonWrapper']")
    for color in colors[:3]:
        color.click()
        selected_color = context.driver.find_element(By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']").text
        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)

    assert expected_colors == actual_colors, f"Expected {expected_colors} did not match actual {actual_colors}"

