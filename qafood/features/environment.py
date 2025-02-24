from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright
import copy
from behave.model import ScenarioOutline, Row
import json
@fixture
def playwright_browser_chrome(context):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False, slow_mo=300, channel="chrome")
    context.page = browser.new_page()

def before_all(context):
    use_fixture(playwright_browser_chrome, context)

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
                # n = copy.deepcopy(orig)
                print (f'{order_loop_count} order loop')
                articles = []
                options = []
                quantity = []
                
                articles_bis = [article["article"] for article in order["articles"]]

                for article in order["articles"]:
                    articles.append(article["article"])
                    # if articles == "":
                    #     articles = article
                    # else:
                    #     articles = articles+";"+article
                    # article_options = ""
                    article_options = array_to_string(article["options"], ",")
                    # for option in article["options"]:
                    #     if article_options == "":
                    #         article_options = option
                    #     else:
                    #         article_options = article_options+","+option
                    options.append(article_options)
                    # if options == "":
                    #     options = article_options
                    # else:
                    #     options = options+";"+article_options
                    quantity.append(str(article["quantity"]))

                articles = array_to_string(articles, ";")
                # articles = ";".join(articles)
                options =  array_to_string(options, ";")
                quantity = array_to_string(quantity, ";")   
                #     n.cells = ['{}'.format(order["order_name"]), '{}'.format(article["article"]) , '{}'.format(article["options"]), '{}'.format(article["quantity"])]
                #     example.table.rows.append(n)
               
                n = Row(headings=headers, cells=['{}'.format(order["order_name"]),
                           '{}'.format(articles),
                           '{}'.format(options),
                           '{}'.format(quantity)])

                example.table.rows.append(n)
                order_loop_count += 1
            print (f'final example value is {example.table.rows}')
                
        # Print the data
        # print(data)      

def array_to_string (array, separator:str):

    # string_result = ""
    string_result= separator.join(array)
    # for item in array:
        # if string_result == "":
        #     string_result = item
        # else:
        #     string_result = string_result+separator+item
    return string_result
    