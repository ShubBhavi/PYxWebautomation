Feature: Google search for the iphone 15
  Scenario: search for the iphone on google
    Given I am on the google page
    When I search for "iphone 15"
    Then I should see the "iphone 15" in the result



