Feature: Showcasing the Scenario Outlin in BDD
  Scenario Outline: search for then App.vwo.com on chrome with different outcomes
    Given I am on the app vo home page
    When I enter the value for <username> and <password>
    Then I get the <message>
    Examples:
    |username|password  |message|
    |admin   |admin2    |did not match |
    |admin3  |password  |did not match |
    |admin6  |admin5    |did not match |