import re
from playwright.sync_api import Page, expect
import csv
import pytest
import allure
import os
import datetime
import locale
locale.setlocale(locale.LC_ALL, 'fr')
from pathlib import Path


address = "https://pprod.aldemia.fr/"
def test_login(page: Page):
    page.goto(address)

    page.locator("#menu-item-28912").click()

    login = os.environ["EMAIL"]
    password = os.environ["PASSWORD"]
    page.locator("#rpress_user_login").fill(login)
    page.locator("#rpress_user_pass").fill(password)
    page.locator("#rpress_login_submit").click()
    png_bytes = page.screenshot()
    allure.attach(
        png_bytes,
        name="full-page",
        attachment_type=allure.attachment_type.PNG
    )

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

@allure.parent_suite("Tests for web interface")
@allure.suite("Tests for essential features")
@allure.sub_suite("Tests for authentication")           
class TestToto:

    @pytest.mark.parametrize("article_name, service_type, service_time", dataset_test_parametre_de_commande())
    @allure.title("Test Authentication")
    @allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
    @allure.tag("NewUI", "Essentials", "Authentication")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "John Doe")
    @allure.link("https://dev.example.com/", name="Website")
    @allure.issue("AUTH-123")
    @allure.testcase("TMS-456")
    def test_parametre_de_commande(self, page: Page, article_name, service_type, service_time):
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
        # date = date_time.strftime("%d")
        date= "19"
        month = date_time.strftime("%B")
        year = date_time.strftime("%Y")
        
        text_visible = f"{service_type}, {date} {month} {year}, {service_time}"
            
        expect.set_options(1000)
        try:
            expect(page.locator("div.delivery-opts"), "Fonction parametre de commande râté!").to_contain_text(text_visible)            
        except:
            self.capture_and_attach_screenshot(page)
            raise


    @pytest.fixture
    @allure.title("Prerequisite pour test")
    def prerequisite_test_ajouter_multiple_article_avec_multiple_topping(self, page: Page):
        page.goto(address)

        page.locator("div.rpress-price-holder:not(.rpress-grid-view-holder)").locator('a[data-title="12 wings"]').click() 
        expect(page.get_by_text("Vos paramètres de commande")).to_be_visible()

        page.locator("#nav-delivery-tab").click()
        
        page.locator('#rpress-delivery-hours').select_option(value="20:00")
        page.locator("a.rpress-delivery-opt-update").click()
        page.locator("a.submit-fooditem-button").click()

    @pytest.mark.parametrize("article_name, topping", dataset_test_ajouter_multiple_article_avec_multiple_topping())
    def test_ajouter_multiple_article_avec_multiple_topping(self, page: Page, prerequisite_test_ajouter_multiple_article_avec_multiple_topping, article_name, topping):
        
        page.locator("div.rpress-price-holder:not(.rpress-grid-view-holder)").locator(f'a[data-title="{article_name}"]').click()
        
        topping = topping.split(",")
        for i in range(0, len(topping)):
            topping[i] = topping[i].strip()
            self.validate_topping(topping[i])
            page.locator(f'div.food-item-list input[name="{topping[i]}"]').locator('..').check()
        
        page.locator("a.submit-fooditem-button").click()
        png_bytes = page.screenshot()
        Path("full-page.png").write_bytes(png_bytes)
        allure.attach.file(
        "full-page.png",
        name="full-page",
        attachment_type=allure.attachment_type.PNG
        )

    def validate_topping(self, topping):
        accepted_values = {'Ketchup', 'Sauce douce', 'Sauce piquante'}
        if topping not in accepted_values:
            # pytest.skip(f"Invalid topping {topping}") # --> gray    
            # assert False, f"Invalid topping {topping}" # --> red
            raise Exception(f"Invalid topping {topping}") # --> yellow
        
    def capture_and_attach_screenshot(self, page, name="full-page"):
        png_bytes = page.screenshot()
        allure.attach(
            png_bytes,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
    