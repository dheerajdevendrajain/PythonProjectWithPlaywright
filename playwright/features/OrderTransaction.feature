Feature: Order Transaction
  Tests related to Order Transactions

  Scenario Outline: Verify Order success message shown in details page
    Given Place the item order with <username> and <password>
    And The user is on landing page
    When I login to portal with <username> and <password>
    And Navigate to orders page
    And Select the orderId
    Then Order message is successfully displayed
    Examples:
      | username    | password  |
      | test@fd.com | Test@1234 |