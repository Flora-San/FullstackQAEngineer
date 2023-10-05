Feature: User Registration and Invalid Email Format

  Scenario: User enters an invalid email format
    Given the user is on the registration page
    When the user fills in the registration form with the following details:
      | Field            | Value                            |
      | First Name       | John                             |
      | Last Name        | Doe                              |
      | Date of Birth    | 01/01/1990                       |
      | Email            | invalid_email                    |
      | Repeat Email     | invalid_email                    |
      | Password         | Passw0rd                         |
      | Terms and Conditions | Checked                      |
    And the user submits the registration form
    Then an error message should be displayed below the Email text box indicating: "Invalid email."
