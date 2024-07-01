Feature: Admin user can log into DAC
    Scenario: An admin user can log in
      Given The admin logs in
        Then The admin sees DAC home page
