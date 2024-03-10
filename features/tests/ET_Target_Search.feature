# Created by elizabethtenpow at 3/9/24
Feature: Shopping Cart tests

  Scenario: “Your cart is empty” message is shown for empty carts
    Given Open Target main page
    When Click on the Shopping cart
    Then verify “Your cart is empty” message is shown

  # Make sure Scenario names are unique:
  Scenario: User can sign in when signed out on Target.com
    Given Open Target main page
    When Click sign in
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened


