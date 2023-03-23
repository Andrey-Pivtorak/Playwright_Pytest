from playwright.sync_api import expect, Page
import pages
import config
import allure


class TestContactUs:

    @allure.title('Test "contact us" form')
    def test_contact_us_form(self, home_page, page: Page):

        with allure.step('Open "contact us" page'):
            pages.contact_us_page.open_contact_us_page(page)
            expect(page.locator('//h2[contains(text(),"Get In Touch")]')).to_be_visible()

        with allure.step('Fill "contact us" form'):
            pages.contact_us_page.fill_contact_us_form(page)

        with allure.step('Check success filling "contact us" form'):
            page.on("dialog", lambda dialog: dialog.accept())
            page.click(pages.contact_us_page.submitBtn)
            expect(page.locator('h2 ~ div.alert-success')).to_be_visible()

        with allure.step('Move to home page'):
            page.click(pages.contact_us_page.homeBtn)
            page.goto(config.url.DOMAIN)
            expect(page).to_have_url(config.url.DOMAIN)
