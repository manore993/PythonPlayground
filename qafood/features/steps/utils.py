from behave import given

address = "https://pprod.aldemia.fr/"

@given('user is logged in')
def step_user_is_logged_in(context):
    page = context.page

    page.goto(address)
    page.locator("#menu-item-28912").click()

    login = context.config.userdata["EMAIL"]
    password = context.config.userdata["PASSWORD"]

    page.locator("#rpress_user_login").fill(login)
    page.locator("#rpress_user_pass").fill(password)
    page.locator("#rpress_login_submit").click()
