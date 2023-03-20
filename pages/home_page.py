from playwright.sync_api import Page, expect


class HomePage:

    loginBtn = 'a[href="/login"]'
    contactUsBtn = '.navbar-nav a[href="/contact_us"]'
    testCasesBtn = '.navbar-nav a[href="/test_cases"]'
    productsBtn = '.navbar-nav a[href="/products"]'
    emailInput = 'input[id="susbscribe_email"]'
    submitBtn = 'button[id="subscribe"]'
    cartBtn = '.navbar-nav a[href="/view_cart"]'
    womenCategoryLink = '#accordian > :first-child a[href="#Women"]'
    menCategoryLink = '#accordian > :nth-child(2)  a[href="#Men"]'
    poloBrandLink = '.brands-name ul a[href="/brand_products/Polo"]'
    babyhugBrandLink = '.brands-name ul a[href="/brand_products/Babyhug"]'

    # def open_homepage(self, page: Page) -> None:
    #     page.goto(config.url.DOMAIN)
    #     expect(page).to_have_url(config.url.DOMAIN)

    # def click_login_button(self, page: Page):
    #     page.locator(self.loginBtn).click()
