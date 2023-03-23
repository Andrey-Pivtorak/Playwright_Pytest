from playwright.sync_api import expect, Page
import pages
import config
import allure


class TestVerifyTestCases:

    @allure.title('Test verify test cases page')
    def test_should_verify_test_cases_page(self, home_page, page: Page):

        with allure.step('Click on "Test Cases" button'):
            page.click(pages.home_page.testCasesBtn)
            page.goto(config.url.DOMAIN + 'test_cases')

        with allure.step('Verify user is navigated to test cases page successfully'):
            expect(page).to_have_url(config.url.DOMAIN + 'test_cases')
            expect(page.locator('//b[contains(text(),"Test Cases")]')).to_be_visible()
