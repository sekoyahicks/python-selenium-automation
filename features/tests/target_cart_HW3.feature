Feature: Target main page search tests
  # Enter feature description here

  Scenario: User can search for a product on Target
    Given Open Target home page
    When Click on Cart icon
    Then Verify "Your cart is empty"