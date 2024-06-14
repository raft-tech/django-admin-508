Feature: Admin Console Filtering
    Scenario: An Admin User can Filter Users
      Given The admin logs in
        When The admin navigates to the users page
        And The admin filters for user ...
        Then Only the filtered user is displayed
    Scenario: An Admin User can use the MultiSelectFilter
      Given The admin logs in
        When The admin navigates to the dummies page
        And The admin uses the multiselect filter
        Then Only the filtered data is displayed
    Scenario: An Admin User can clear Filters
      Given The admin logs in
        When The admin navigates to the dummies page
        And The admin uses the multiselect filter
        Then The admin clears the filters
