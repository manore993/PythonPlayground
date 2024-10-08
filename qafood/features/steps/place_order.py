from behave import then, given, when
from playwright.sync_api import expect

address = "https://pprod.aldemia.fr/"

@given('the current order is empty')
def step_current_order_is_empty(context):
    page = context.page
    page.goto(address)

    # todo assert no order
    pass 

@when('the user select the 12 wings option')
def step_user_select_option(context):
    page = context.page

    page.locator("div.rpress-price-holder:not(.rpress-grid-view-holder)").locator('a[data-title="12 wings"]').click() 


@then('the user should be able to select order type (delivery or pick up)')
def step_user_can_select_order_type(context):
    page = context.page

    expect(page.get_by_text("Vos paramètres de commande")).to_be_visible()
