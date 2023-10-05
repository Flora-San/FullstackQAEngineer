Feature: User Registration and Email Already Registered

  Scenario: User enters an email address already registered
    Given the user is on the registration page
    When the user fills in the registration form with the following details:
      | Field            | Value                            |
      | First Name       | John                             |
      | Last Name        | Doe                              |
      | Date of Birth    | 01/01/1990                       |
      | Email            | existing_user@example.com         |
      | Repeat Email     | existing_user@example.com         |
      | Password         | Passw0rd                         |
      | Terms and Conditions | Checked                      |
    And the user submits the registration form
    Then the user should be redirected to the login page
    And a message should be displayed on the login page indicating: "There is an existing account associated with existing_user@example.com"

