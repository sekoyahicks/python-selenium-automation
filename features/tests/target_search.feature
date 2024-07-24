Feature: Target main page search tests
  # Enter feature description here

  Scenario: User can search for a product on Target
    Given Open Target main page
    When Search for product
#    Then Verify search worked

  Scenario: User can add a product to cart
    Given Open target main page
    When Search for toothpaste
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify search results shown for {expected_product}
    And Verify correct search results URL opens for {expected_product}