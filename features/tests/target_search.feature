Feature: Target main page search tests
  # Enter feature description here

  Scenario: User can search for a product on Target
    Given Open Target main page
    When Search for product
#    Then Verify search worked

  Scenario: User can add product to cart
    Given Open Target main page
    When Search for toothpaste
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart Button
    And Open cart
#    Then Verify cart has 1 item




#    And Click on Add to Cart button
#    And Confirm Add to Cart button
#    And Open Cart page
#    Then verify Cart has 1 item