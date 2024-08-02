Feature: Showcasing the BDD
  Scenario Outline: search for Healthcare
    Given I am on page called Cura
    When  Entering the <Email> and <pwd>
    Then I got <output>
    Examples:
    |Email   |pwd       |output        |
    |admin   |admin     |Login failed! |
    |admin3  |password  |Login failed! |
    |admin   |admin     |Login failed! |