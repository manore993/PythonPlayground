Feature: As a customer, I want to check that I can claim an available airspace to "Rent" in SkyTrade platform by entering an address manually in map feature

  Background: Navigate to the SkyTrade Platform and LoginOrRegister
    Given I am on sky.trade
    And I have navigated to the App
    And I am logged in as a user

  Scenario: Define Air Space Location By Writing Adress
    Given I am on the "Airspace" tab
    When I click on the search bar "Search Air Spaces"
    And I enter the <address_location>
    And I choose <address_location> from dropdown list
    Then I should see the map zoomed to the location <address_location>

    Examples:
      | address_location                                        |
      | 11 Wall Street, New York, New York 10005, United States |

  Scenario: Specify Claim Details for an available address
    Given There is an address displayed on the map
    When I click on the "Claim Airspace" button
    And I verify the address is <address_location>
    And I add the name <name>
    And I select "rent"
    And I set "Variable Fee Rental Range (per transit)" to <fee_range>
    And I set "Time Zone" to <time_zone>
    And I click on the "Claim Airspace"
    Then The message "Congratulations on claiming your piece of the sky successfully!" appears
    And the form is closed

    Examples:
      | address_location                                        | name           | fee_range | time_zone              |
      | 11 Wall Street, New York, New York 10005, United States | Stock Exchange | $100-$199 | (GMT+0:00) UTC Etc/GMT |

  Scenario: Specify Claim Details for an unavailable address
    Given There is an address displayed on the map
    When I click on the "Claim Airspace" button
    And I verify the address is <address_location>
    And I add the name <name>
    And I select “rent”
    And I set "Variable Fee Rental Range (per transit)" to <fee_range>
    And I set "Time Zone" to <time_zone>
    And I click on the "Claim Airspace"
    Then The message "Error: This airspace is not available!" appears
    And the form is still open

    Examples:
      | address_location                                        | name           | fee_range | time_zone              |
      | 11 Wall Street, New York, New York 10005, United States | Stock Exchange | $100-$199 | (GMT+0:00) UTC Etc/GMT |
