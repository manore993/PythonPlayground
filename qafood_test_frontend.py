import re
from playwright.sync_api import Page, expect

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

def test_add_item_to_cart(page: Page):
    page.goto(address)
    article_name = "12 wings"
    #page.locator('div.rp-col-md-3 a[data-title="12 wings"]').click() 
    page.locator("div.rpress-price-holder:not(.rpress-grid-view-holder)").locator('a[data-title="12 wings"]').click() 
    expect(page.get_by_text("Vos paramètres de commande")).to_be_visible()
    page.locator("#nav-delivery-tab").click()
    optionValue = "18:30"
    page.locator('#rpress-delivery-hours').select_option(value=optionValue)
    page.locator("a.rpress-delivery-opt-update").click()