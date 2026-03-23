Feature: Activities Management
  As a student
  I want to view and sign up for extracurricular activities
  So that I can participate in school activities

  Scenario: View all activities
    When I request all activities
    Then I should receive a list of all activities

  Scenario: Successful signup for an activity
    When I sign up "newstudent@mergington.edu" for "Chess Club"
    Then the signup should be successful
    And "newstudent@mergington.edu" should be added to "Chess Club" participants

  Scenario: Signup for non-existent activity
    When I sign up "student@mergington.edu" for "Nonexistent Activity"
    Then the signup should fail with 404
    And the error message should be "Activity not found"

  Scenario: Signup when already signed up
    When I sign up "michael@mergington.edu" for "Chess Club"
    Then the signup should fail with 400
    And the error message should be "Student already signed up for this activity"

  Scenario: Successful unregister from an activity
    When I unregister "michael@mergington.edu" from "Chess Club"
    Then the unregister should be successful
    And "michael@mergington.edu" should be removed from "Chess Club" participants

  Scenario: Unregister from non-existent activity
    When I unregister "student@mergington.edu" from "Nonexistent Activity"
    Then the unregister should fail with 404
    And the error message should be "Activity not found"

  Scenario: Unregister when not signed up
    When I unregister "notsigned@mergington.edu" from "Chess Club"
    Then the unregister should fail with 400
    And the error message should be "Student not signed up for this activity"