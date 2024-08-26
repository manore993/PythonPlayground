import re
from playwright.sync_api import sync_playwright
import csv

# with open('./qafood/test_parametre_de_commande.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
#     for row in spamreader:
#         print(row)

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, slow_mo=200)

page =browser.new_page()

page.goto("https://pprod.aldemia.fr/")

# page.get_by_role("link", name="Inscription", exact=True).click()
# print(page.locator("h1").text_content())

#page.get_by_role("textbox", name="rpress_user_login").fill("Hulu")
#page.locator("#rpress-user-login").fill("Hulu")
article_name = "12 wings" 
page.locator("div.rpress-price-holder:not(.rpress-grid-view-holder)").locator(f'a[data-title="{article_name}"]').click() 
   
page.locator("#nav-delivery-tab").click()
optionValue = "18:30"
page.locator('#rpress-delivery-hours').select_option(value=optionValue)
page.locator("a.rpress-delivery-opt-update").click()

page.locator("div.rpress-price-holder:not(.rpress-grid-view-holder)").locator(f'a[data-title="{article_name}"]').click()
page.locator('div.food-item-list input[name="Ketchup"]').locator('..').click()