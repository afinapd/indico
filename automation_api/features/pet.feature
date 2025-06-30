Feature: Pet Store API Testing

  Scenario: Add a new pet to the store
    Given I have pet details to add
    When I send POST request to add a new pet
    Then the response status code should be 200
    And the response should contain the correct pet details

  Scenario Outline: Find pets by status
    When I send GET request to find pets by status "<status>"
    Then the response status code should be 200
    And all pets in the response should have status "<status>"

    Examples:
      | status    |
      | available |
      | pending   |
