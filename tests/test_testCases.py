from playwright.sync_api import expect, Page
import pages
import config


class TestVerifyTestCases:

    def test_should_verify_test_cases_page(self, home_page: Page, page: Page):

        home_page.click(pages.home_page.testCasesBtn)
        page.goto('https://automationexercise.com/test_cases')
        expect(page).to_have_url(config.url.DOMAIN + 'test_cases')
        expect(page.locator(
            '//b[contains(text(),"Test Cases")]')).to_be_visible()
