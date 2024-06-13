Feature: Admin user apply filters in DAC
    Scenario: A user can log in
      Given The admin logs in
        And The admin navigates to the users page
        When The admin filters for user ...
        Then Only the filtered user is displayed
