from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright

@fixture
def playwright_browser_chrome(context):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False, slow_mo=300, channel="chrome")
    context.page = browser.new_page()

def before_all(context):
    use_fixture(playwright_browser_chrome, context)

def after_all(context):
    #context.page.close()
    pass 