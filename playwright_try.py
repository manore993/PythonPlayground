import re
from playwright.sync_api import sync_playwright
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, slow_mo=100)

page =browser.new_page()



page.goto("http://127.0.0.1:5000")




page.get_by_role("link", name="Register", exact=True).click()


page.get_by_role("textbox", name="name").fill("Lulu")
page.get_by_role("textbox", name="email").fill("lulu@gmail.com")
page.get_by_role("textbox", name="password").fill("lulu4789")

page.get_by_role("button", name="Register").last.click()

x = input()