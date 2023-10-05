Feature: User Registration and Missing Mandatory Fields

  Scenario: User leaves one or more mandatory fields empty
    Given the user is on the registration page
    When the user leaves one or more mandatory fields empty
    And the user clicks the "Register" button
    Then error messages should be displayed below the corresponding empty mandatory fields indicating: "Please fill in this <<FIELD>>."
