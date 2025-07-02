Feature: Trust Wallet Creation

  @test_wallet_creation
  Scenario: Create a new wallet
    Given I launch Trust Wallet app
    When I tap Create new wallet button
    And I set a secure passcode "123456"
    And I confirm the passcode "123456"
    And I choose Deny to biometric login
    And I tap Skip, I'll do it later
    Then I should see the message "Brilliant, your wallet is ready!"
