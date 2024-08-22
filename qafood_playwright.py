import re
from playwright.sync_api import sync_playwright
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, slow_mo=200)

page =browser.new_page()

page.goto("https://pprod.aldemia.fr/")

page.get_by_role("link", name="Inscription", exact=True).click()
print(page.locator("h1").text_content())

#page.get_by_role("textbox", name="rpress_user_login").fill("Hulu")
page.locator("#rpress-user-login").fill("Hulu")

