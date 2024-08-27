import re
from playwright.sync_api import Page, expect
import csv
import pytest
import allure
import os
import datetime
import locale
locale.setlocale(locale.LC_ALL, 'fr')


address = "https://pprod.aldemia.fr/"

def test_login(page: Page):
    page.goto(address)

    page.locator("#menu-item-28912").click()

    login = os.environ["EMAIL"]
    password = os.environ["PASSWORD"]
    page.locator("#rpress_user_login").fill(login)
    page.locator("#rpress_user_pass").fill(password)
    page.locator("#rpress_login_submit").click()

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

def dataset_test_parametre_de_commande():
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
    return dataset_test_parameter_de_commande

def dataset_test_ajouter_multiple_article_avec_multiple_topping():
    dataset_test_ajouter_multiple_article_avec_multiple_topping = []

    with open('./qafood/test_ajouter_multiple_article_avec_multiple_topping.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        has_parsed_header = False
        article_name = 0
        topping = 1

        for row in spamreader:
            
            for i in range(0,len(row)):
                row[i] = row[i].strip()

            if not has_parsed_header:
                has_parsed_header = True
                print (row)
                article_name = row.index('article_name')
                topping = row.index('topping')
               
                continue

            #dataset_test_parameter_de_commande += [row]
            ordered_row = (row[article_name], row[topping])
            dataset_test_ajouter_multiple_article_avec_multiple_topping += [ordered_row]
    return dataset_test_ajouter_multiple_article_avec_multiple_topping
           
@pytest.mark.parametrize("article_name, service_type, service_time", dataset_test_parametre_de_commande())

def test_parametre_de_commande(page: Page, article_name, service_type, service_time):
    page.goto(address)

    #page.locator('div.rp-col-md-3 a[data-title="12 wings"]').click() 
    page.locator("div.rpress-price-holder:not(.rpress-grid-view-holder)").locator(f'a[data-title="{article_name}"]').click() 
    expect(page.get_by_text("Vos paramètres de commande")).to_be_visible()

    if (service_type == "Livraison"):
        id_data_service_type = "#nav-delivery-tab"
        locator_service_time = '#rpress-delivery-hours'
    if (service_type == "À emporter"):
        id_data_service_type = "#nav-pickup-tab"
        locator_service_time = '#rpress-pickup-hours'

    page.locator(id_data_service_type).click()
    page.locator(locator_service_time).select_option(value=service_time)
    page.locator("a.rpress-delivery-opt-update").click()
    page.locator("a.submit-fooditem-button").click()

    date_time = datetime.datetime.now()
    date = date_time.strftime("%d")
    month = date_time.strftime("%B")
    year = date_time.strftime("%Y")
    
    text_visible = f"{service_type}, {date} {month} {year}, {service_time}"

    expect(page.locator("div.delivery-opts")).to_contain_text(text_visible)

@pytest.fixture
def prerequisite_test_ajouter_multiple_article_avec_multiple_topping(page: Page):
    page.goto(address)

    page.locator("div.rpress-price-holder:not(.rpress-grid-view-holder)").locator('a[data-title="12 wings"]').click() 
    expect(page.get_by_text("Vos paramètres de commande")).to_be_visible()

    page.locator("#nav-delivery-tab").click()
    
    page.locator('#rpress-delivery-hours').select_option(value="20:00")
    page.locator("a.rpress-delivery-opt-update").click()
    page.locator("a.submit-fooditem-button").click()

@pytest.mark.parametrize("article_name, topping", dataset_test_ajouter_multiple_article_avec_multiple_topping())

def test_ajouter_multiple_article_avec_multiple_topping(page: Page, prerequisite_test_ajouter_multiple_article_avec_multiple_topping, article_name, topping):
    page.locator("div.rpress-price-holder:not(.rpress-grid-view-holder)").locator(f'a[data-title="{article_name}"]').click()
    
    topping = topping.split(",")
    for i in range(0, len(topping)):
        topping[i] = topping[i].strip()
        page.locator(f'div.food-item-list input[name="{topping[i]}"]').locator('..').check()
    
    page.locator("a.submit-fooditem-button").click()
    
