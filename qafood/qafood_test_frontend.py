import re
from playwright.sync_api import Page, expect
import csv
import pytest

address = "https://pprod.aldemia.fr/"

def test_access_homepage(page: Page):
    page.goto(address)

    expect(page).to_have_title(re.compile("QAFOOD"))

# def test_register_username(page: Page):
#     page.goto(address)

#     page.get_by_role("link", name="Inscription", exact=True).click()
#     expect(page.locator("h1")).to_contain_text(re.compile("Inscription"))

#     page.locator("#rpress-user-login").fill("Zlu")
#     page.locator("#rpress-user-email").fill("zlu@gmail.com")
#     page.locator("#rpress-user-pass").fill("zlu4789")
#     page.locator("#rpress-user-pass2").fill("zlu4789")

#     page.get_by_role("button", name="Inscription").last.click()
#     expect(page.get_by_text("Vous n'avez passé aucune commande")).to_be_visible()
dataset_test_parameter_de_commande = []

with open('./qafood/test_parametre_de_commande.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    has_parsed_header = False
    article_name = 0
    service_type = 1
    service_time = 2

    for row in spamreader:
        
        for i in range(0,len(row)):
            row[i] = row[i].strip()

        if not has_parsed_header:
            has_parsed_header = True
            print (row)
            article_name = row.index('article_name')
            service_type = row.index('service_type')
            service_time = row.index('service_time')
            continue

        #dataset_test_parameter_de_commande += [row]
        ordered_row = (row[article_name], row[service_type], row[service_time])
        dataset_test_parameter_de_commande += [ordered_row]
        

@pytest.mark.parametrize("article_name, service_type, service_time", dataset_test_parameter_de_commande)

def test_parametre_de_commande(page: Page, article_name, service_type, service_time):
    page.goto(address)

    #page.locator('div.rp-col-md-3 a[data-title="12 wings"]').click() 
    page.locator("div.rpress-price-holder:not(.rpress-grid-view-holder)").locator(f'a[data-title="{article_name}"]').click() 
    expect(page.get_by_text("Vos paramètres de commande")).to_be_visible()

    if (service_type == "Liveraison"):
        id_data_service_type = "#nav-delivery-tab"
        locator_service_time = '#rpress-delivery-hours'
    if (service_type == "À emporter"):
        id_data_service_type = "#nav-pickup-tab"
        locator_service_time = '#rpress-pickup-hours'

    page.locator(id_data_service_type).click()
    
    service_time = "18:30"

    page.locator(locator_service_time).select_option(value=service_time)
    page.locator("a.rpress-delivery-opt-update").click()
    page.locator("a.submit-fooditem-button").click()