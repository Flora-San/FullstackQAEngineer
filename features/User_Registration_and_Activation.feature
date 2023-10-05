
Feature: User Registration and Activation

  Scenario: User successfully registers, receives an activation email, and activates the account
    Given the user is on the registration page
    When the user fills in the registration form with the following details:
      | Field            | Value                            |
      | First Name       | John                             |
      | Last Name        | Doe                              |
      | Date of Birth    | 01/01/1990                       |
      | Email            | john.doe@example.com             |
      | Repeat Email     | john.doe@example.com             |
      | Password         | Passw0rd                         |
      | Terms and Conditions | Checked                      |
    And the user submits the registration form
    And the user checks their email inbox for the activation email
    And the user clicks the activation link in the email
    Then the user's account should be successfully activated
    And the user should be redirected to a page with a message indicating the need to activate the account
    And the user should receive an activation email
    And clicking the activation link should activate the account


Feature: User Registration and Date of Birth Exceeds Current Date

  Scenario: User selects a Date of Birth that exceeds the current date
    Given the user is on the registration page
    When the user fills in the registration form with the following details:
      | Field            | Value                            |
      | First Name       | John                             |
      | Last Name        | Doe                              |
      | Date of Birth    | 01/01/future_year                |
      | Email            | john.doe@example.com             |
      | Repeat Email     | john.doe@example.com             |
      | Password         | Passw0rd                         |
      | Terms and Conditions | Checked                      |
    And the user submits the registration form
    Then an error message should be displayed indicating: "Selected date exceeds the current date"

