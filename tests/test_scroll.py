from playwright.sync_api import expect, Page
import allure
import time


class TestScroll:

    @allure.title('Test verify scroll up and down using arrow button')
    def test_should_verify_scroll_up_using_arrow_button_and_down(self, home_page, page: Page):

        with allure.step('Scroll down page to bottom'):
            page.locator('//h2[contains(text(),"Subscription")]').scroll_into_view_if_needed()

        with allure.step('Verify "SUBSCRIPTION" is visible'):
            expect(page.locator('//h2[contains(text(),"Subscription")]')).to_be_visible()
        page.locator('#scrollUp').scroll_into_view_if_needed()
        # Closed-mode shadow roots are not supported !!!
        # page.click('#scrollUp')
        # text = page.query_selector('//h2[contains(text(),"Full-Fledged practice website for Automation Engineers")]')
        # assert text.is_visible


    @allure.title('Test verify scroll up and down without using arrow button')
    def test_should_verify_scroll_up_without_using_arrow_button_and_down(self, home_page, page: Page):
        with allure.step('Scroll down page to bottom'):
            page.locator('//h2[contains(text(),"Subscription")]').scroll_into_view_if_needed()

        with allure.step('Verify "SUBSCRIPTION" is visible'):
            expect(page.locator('//h2[contains(text(),"Subscription")]')).to_be_visible()

        with allure.step('Scroll up page to top'):
            page.locator('#header').scroll_into_view_if_needed
            page.locator('#header').click()

        with allure.step(' Verify that "Full-Fledged practice website for Automation Engineers" text is visible'):
            elem = page.query_selector('//h2[contains(text(),"Full-Fledged")]')
            assert elem.is_visible()
