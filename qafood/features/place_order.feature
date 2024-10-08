Feature: Place an order
    As a customer
    I want to order some food to be delivered to my flat

Scenario: Selecting order type
    Given user is logged in
    Given the current order is empty 
    When the user select the 12 wings option 
    Then the user should be able to select order type (delivery or pick up)   


Scenario: Ordering mutliple dish
    Given user is logged in
    Given the current order is empty 
    When the user select the "12 wings" option     
    When the user select delivery at 18:00
    When the user select the "milkshake" option     
    When the user select the "sashimi" option     
    When the user select the "ramen" option     
    Then the basket contains two dishes 
