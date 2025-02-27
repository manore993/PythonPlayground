from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright
import copy
from behave.model import ScenarioOutline, Row
import json
from time import sleep

@fixture
def playwright_browser_chrome(context):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False, slow_mo=300, channel="chrome")
    context.page = browser.new_page()
@fixture
def logged_in_context(context):
    address = "https://pprod.aldemia.fr/"
    page = context.page

    page.goto(address)
    page.locator("#menu-item-29218").click()
    page.get_by_text("vous déconnecter").click()
    
    page.goto(address)
    page.locator("#menu-item-28912").click()

    login = context.config.userdata["EMAIL"]
    password = context.config.userdata["PASSWORD"]

    page.locator("#rpress_user_login").fill(login)
    page.locator("#rpress_user_pass").fill(password)
    page.locator("#rpress_login_submit").click()
    page.locator("#menu-item-28852").click()

def before_all(context):
    use_fixture(playwright_browser_chrome, context)
    use_fixture(logged_in_context, context)


def before_feature(context, feature):
    features = (scenario for scenario in feature.scenarios if type(scenario) == ScenarioOutline and 'dynamic' in scenario.tags)
    for scenario in features:
        
        for example in scenario.examples: 
            
            with open('./features/place_order.json',encoding="utf-8") as file:
                orders = json.load(file)  # Load JSON data as a Python dictionary

            orig: Row = example.table.rows[0]
            headers = orig.headings

            example.table.rows = []

            order_loop_count = 0
            for order in orders:
                
                print (f'{order_loop_count} order loop')

                n = Row(headings=headers, 
                         cells=[order["order_name"],
                             json.dumps(order["articles"])])

                example.table.rows.append(n)
                order_loop_count += 1
            print (f'final example value is {example.table.rows}')
                    

    # if "Constructing an order" in feature.name:
    #     page = context.page
    #     page.on("dialog", lambda dialog: dialog.accept())
    #     page.locator("div.rpress-price-holder:not(.rpress-grid-view-holder)").locator(f'a[data-title="12 wings"]').click()
    #     page.locator("#nav-delivery-tab").click()
            
    #     page.locator('#rpress-delivery-hours').select_option(value="20:00")
    #     page.locator("a.rpress-delivery-opt-update").click()
    #     page.locator("a.submit-fooditem-button").click()
    #     page.locator("a.rpress-remove-from-cart").click()

def before_scenario(context, scenario):
    if "User creates an order with multiple items and options" in scenario.name:
        page = context.page
        page.on("dialog", lambda dialog: dialog.accept())
        page.locator("div.rpress-price-holder:not(.rpress-grid-view-holder)").locator(f'a[data-title="12 wings"]').click()
        page.locator("#nav-delivery-tab").click()
            
        page.locator('#rpress-delivery-hours').select_option(value="20:00")
        page.locator("a.rpress-delivery-opt-update").click()
        page.locator("a.submit-fooditem-button").click()
        page.locator("a.rpress-remove-from-cart").click()
# 
def after_scenario(context, scenario):
    if "User creates an order with multiple items and options" in scenario.name:
        page = context.page
        page.on("dialog", lambda dialog: dialog.accept())
        page.locator("a.rpress-clear-cart").click()
        sleep(2)


# def before_feature(context, feature):
#     features = (scenario for scenario in feature.scenarios if type(scenario) == ScenarioOutline and 'dynamic' in scenario.tags)
#     for scenario in features:
        
#         for example in scenario.examples: 
            
#             with open('./features/place_order.json',encoding="utf-8") as file:
#                 orders = json.load(file)  # Load JSON data as a Python dictionary

#             orig: Row = example.table.rows[0]
#             headers = orig.headings

#             example.table.rows = []

#             order_loop_count = 0
#             for order in orders:
#                 # n = copy.deepcopy(orig)
#                 print (f'{order_loop_count} order loop')
#                 articles = []
#                 options = []
#                 quantity = []
                
#                 articles_bis = [article["article"] for article in order["articles"]]

#                 for article in order["articles"]:
#                     articles.append(article["article"])
                
#                     article_options = array_to_string(article["options"], ",")
                    
#                     options.append(article_options)
                    
#                     quantity.append(str(article["quantity"]))

#                 articles = array_to_string(articles, ";")
#                 # articles = ";".join(articles)
#                 options =  array_to_string(options, ";")
#                 quantity = array_to_string(quantity, ";")   
               
#                 n = Row(headings=headers, cells=['{}'.format(order["order_name"]),
#                            '{}'.format(articles),
#                            '{}'.format(options),
#                            '{}'.format(quantity)])

#                 example.table.rows.append(n)
#                 order_loop_count += 1
#             print (f'final example value is {example.table.rows}')
                
#         # Print the data
#         # print(data)      

#     if "Constructing an order" in feature.name:
#         page = context.page
#         page.on("dialog", lambda dialog: dialog.accept())
#         page.locator("div.rpress-price-holder:not(.rpress-grid-view-holder)").locator(f'a[data-title="12 wings"]').click()
#         page.locator("#nav-delivery-tab").click()
            
#         page.locator('#rpress-delivery-hours').select_option(value="20:00")
#         page.locator("a.rpress-delivery-opt-update").click()
#         page.locator("a.submit-fooditem-button").click()
#         page.locator("a.rpress-remove-from-cart").click()

# def array_to_string (array, separator:str):

#     # string_result = ""
#     string_result= separator.join(array)
#     # for item in array:
#         # if string_result == "":
#         #     string_result = item
#         # else:
#         #     string_result = string_result+separator+item
#     return string_result