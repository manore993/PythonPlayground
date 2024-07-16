import re
from playwright.sync_api import sync_playwright
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, slow_mo=200)

page =browser.new_page()

page.goto("http://127.0.0.1:5000")

page.get_by_role("link", name="Register", exact=True).click()


page.get_by_role("textbox", name="name").fill("Lulu")
page.get_by_role("textbox", name="email").fill("lulu@gmail.com")
page.get_by_role("textbox", name="password").fill("lulu4789")

page.get_by_role("button", name="Register").last.click()


page.get_by_role("link", name="Login Page").click()

page.get_by_role("textbox", name="email").fill("lulu@gmail.com")
page.get_by_role("textbox", name="password").fill("lulu4789")

page.get_by_role("button", name="Login").last.click()

page.select_option('select#base',value='10')
page.get_by_role("textbox", name="input").fill("10")
page.get_by_role("button", name="Calculate").click()

page.get_by_role("link", name="History").click()

x = input()