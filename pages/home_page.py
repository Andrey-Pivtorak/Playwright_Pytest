from playwright.sync_api import Page, expect

class HomePage:

    loginBtn = 'a[href="/login"]'
    contactUsBtn = '.navbar-nav a[href="/contact_us"]'


    # def open_homepage(self, page: Page) -> None:
    #     page.goto(config.url.DOMAIN)
    #     expect(page).to_have_url(config.url.DOMAIN)

    # def click_login_button(self, page: Page):
    #     page.locator(self.loginBtn).click()

