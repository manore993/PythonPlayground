Feature: Place an order
    As a customer
    I want to order some food to be delivered to my flat

Scenario: Selecting order type
    Given user is logged in
    Given the current order is empty 
    When the user select the "12 wings" option 
    Then the user should be able to select order type (delivery or pick up)   


Scenario: Selecting multiple options
    Given user is logged in
    Given the user select the "12 wings" option 
    Given the user select "delivery" and "time"
    When  the user select the "12 wings" option 
    When user select toppings
        | topping |
        | Ketchup |
        | Sauce douce |     
    Then there are two items in the basket
