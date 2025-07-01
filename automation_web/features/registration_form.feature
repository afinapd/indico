Feature: Website UI Automation - Form Submission and Upload

  @test_form
  Scenario: Fill basic form data
    Given I open the registration form page
    When I fill in the form with dummy profile data "Name" with "John Doe"
    And I fill in the form with dummy profile data "Email" with "john@example.com"
    And I fill in the form with dummy profile data "Phone" with "08123456789"
    And I fill in the form with dummy profile data "Address" with "123 Dummy St."
    And I select gender as "Male"
    And I select the days: "Monday, Wednesday, Friday"
    And I select country as "United States"
    And I select color as "Blue"
    And I select sorted list item "Dog"

  @test_date1
  Scenario: Fill Date Picker 1
    Given I open the registration form page
    When I pick "15/08/2024" on Date Picker 1

  @test_date2
  Scenario: Fill Date Picker 2
    Given I open the registration form page
    When I pick "08/20/2024" on Date Picker 2

  @test_date3
  Scenario: Fill Date Picker 3
    Given I open the registration form page
    When I pick date range "01/07/2025 - 03/07/2025" on Date Picker 3
    And I click the Submit button
    Then the form should be submitted successfully

  @test_upload_single
  Scenario: Upload a single file
    Given I open the file upload section
    When I choose "dummy.png" to upload
    And I click the "Upload Single File" button
    Then I should see message "Single file selected"

  @test_upload_multiple
  Scenario: Upload multiple files
    Given I open the file upload section
    When I choose the files "dummy.png, dummy.pdf" to upload
    And I click the "Upload Multiple Files" button
    Then I should see message "Multiple files selected"