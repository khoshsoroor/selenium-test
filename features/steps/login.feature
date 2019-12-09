Feature: Login to Website


  Scenario: Check Home page
    When GET the URL title



  Scenario: Log in
    When I have logged into the system
    Then I should see "Logged in"