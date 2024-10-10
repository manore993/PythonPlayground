from time import sleep
from behave import then, given, when
from playwright.sync_api import expect

use_step_matcher("cfparse")

address = "https://pprod.aldemia.fr/"

@given('the current order is empty')
def step_current_order_is_empty(context):
    # todo assert no order
    pass 

@when('the user select the "{option}" option')
@given('the user select the "{option}" option')
def step_user_select_option(context, option):
    page = context.page

    page.locator("div.rpress-price-holder:not(.rpress-grid-view-holder)").locator(f'a[data-title="{option}"]').click() 

@given(u'the user select "delivery" and "time"')
def step_user_set_up_delivery(context):
    page = context.page
    page.locator("#nav-delivery-tab").click()
        
    page.locator('#rpress-delivery-hours').select_option(value="20:00")
    page.locator("a.rpress-delivery-opt-update").click()
    page.locator("a.submit-fooditem-button").click()


@when('user select toppings')
def step_select_toppings(context):
    page = context.page
    for row in context.table:    
        page.locator(f'div.food-item-list input[name="{row['topping']}"]').locator('..').check()
    page.locator("a.submit-fooditem-button").click()

@then('the user should be able to select order type (delivery or pick up)')
def step_user_can_select_order_type(context):
    page = context.page

    expect(page.get_by_text("Vos paramètres de commande")).to_be_visible()

@then('there are two items in the basket')
def step_count_items_in_basket(context):
    page = context.page

    expect(page.get_by_text("Total (2 Articles)")).to_be_visible()
