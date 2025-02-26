from time import sleep
from behave import use_step_matcher, given, when, then
from playwright.sync_api import expect
import json

use_step_matcher("re")

address = "https://pprod.aldemia.fr/"

@given(u'the current order is empty')
def step_current_order_is_empty(context):
    page = context.page
    try:
        expect(page.locator("li.cart_item.empty")).to_be_visible()
    except AssertionError:
        page.screenshot()
        raise Exception(f"The current order is not empty.")

@when(u'the user creates "(?P<order_name>.*)" with following choices "(?P<articles>.*)"')
def step_create_order(context,order_name, articles):
    page = context.page
    articles_dict = json.loads(articles)
    for article in articles_dict:
        x = article
        page.locator("div.rpress-price-holder:not(.rpress-grid-view-holder)").locator(f'a[data-title="{article["article"]}"]').click()
        for topping in article["options"]:
            page.locator(f'div.food-item-list input[name="{topping}"]').locator('..').check()
            sleep(2)
        for i in range(0,article["quantity"]):
            page.locator("input.qtyplus.qtyplus-style.qtyplus-style-edit").click()
            sleep(2)
        page.locator("a.submit-fooditem-button").click()
        sleep(2)

@then(u'the order summary should display "(?P<order_name>.*)" with following choices "(?P<articles>.*)"')
def step_check_order_summary(context, order_name, articles):
    page = context.page
    articles_dict = json.loads(articles)
    article_count = 0
    for article in articles_dict:
        x = article
        article_locator = page.locator("li.rpress-cart-item data-cart-key=\"{article_count}\"")
        try:
            expect(article_locator.locator("span.rpress-cart-item-title").get_by_text(article)).to_be_visible()
        except AssertionError:
            page.screenshot()
            raise Exception(f"For the {order_name} cannot find {article} in the cart.")

        for topping in article["options"]:
            try:
                expect(article_locator.get_by_text(topping)).to_be_visible()
            except AssertionError:
                page.screenshot()
                raise Exception(f"For the {order_name} -- {article} -- cannot find {topping} in the cart.")
            sleep(2)
        
        try:
            expect(article_locator.locator("span.rpress-cart-item-qty.qty-class").get_by_text(topping)).to_be_visible()
        except AssertionError:
            page.screenshot()
            raise Exception(f"For the {order_name} -- {article} -- the quantity is not equal to the expected {article["quantity"]} in the cart.")

        article_count += 1


@when(u'the user select the "{option}" option')
@given(u'the user select the "{option}" option')
def step_user_select_option(context, option):
    page = context.page

    page.locator("div.rpress-price-holder:not(.rpress-grid-view-holder)").locator(f'a[data-title="{option}"]').click() 

@given(u'the user select "delivery" and "time"')
def step_user_set_up_delivery(context):
    page = context.page
    page.on("dialog", lambda dialog: dialog.accept())
    page.locator("div.rpress-price-holder:not(.rpress-grid-view-holder)").locator(f'a[data-title="12 wings"]').click()
    page.locator("#nav-delivery-tab").click()
        
    page.locator('#rpress-delivery-hours').select_option(value="20:00")
    page.locator("a.rpress-delivery-opt-update").click()
    page.locator("a.submit-fooditem-button").click()
    page.locator("a.rpress-remove-from-cart").click()


@when(u'user select toppings')
def step_select_toppings(context):
    page = context.page
    for row in context.table:    
        page.locator(f'div.food-item-list input[name="{row['topping']}"]').locator('..').check()
    page.locator("a.submit-fooditem-button").click()

@then(u'the user should be able to select order type (delivery or pick up)')
def step_user_can_select_order_type(context):
    page = context.page

    expect(page.get_by_text("Vos paramètres de commande")).to_be_visible()

@then(u'there are two items in the basket')
def step_count_items_in_basket(context):
    page = context.page

    expect(page.get_by_text("Total (2 Articles)")).to_be_visible()
