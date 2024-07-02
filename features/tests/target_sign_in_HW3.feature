Feature: Target main page search tests
  # Enter feature description here

  Scenario: User can sign in to Target
    Given Open Target
    When Click Sign In
    When Click Sign In from side nav
    Then Verify Sign In form opened