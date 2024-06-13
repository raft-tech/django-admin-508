Feature: Admin Console Filtering
    Scenario: An Admin User can Filter Users
      Given The admin logs in
        When The admin navigates to the users page
        And The admin filters for user ...
        Then Only the filtered user is displayed
    Scenario: An Admin User can Create a New Filter and Use it
      Given The admin logs in
        When The admin navigates to the users page
        And The admin creates a filter
        Then The admin uses the new filter
        And Only the filtered data is displayed
