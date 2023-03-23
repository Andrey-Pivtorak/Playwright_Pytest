from playwright.sync_api import expect, Page
import pages
import data
import allure


class TestSubscription:

    @allure.title('Test verify subscription in home page')
    def test_should_verify_subscription_in_home_page(self, home_page, page: Page):

        with allure.step('Scroll down page to bottom'):
            page.locator('//h2[contains(text(),"Subscription")]').scroll_into_view_if_needed()

        with allure.step('Verify "SUBSCRIPTION" is visible'):
            expect(page.locator('//h2[contains(text(),"Subscription")]')).to_be_visible()

        with allure.step('Enter email address in input and click arrow button'):
            page.fill(pages.home_page.emailInput, data.user_data.email)
            page.click(pages.home_page.submitBtn)

        with allure.step('Verify success message "You have been successfully subscribed!" is visible'):
            expect(page.locator('.alert-success')).to_be_visible()


    @allure.title('Test verify subscription in cart page')
    def test_should_verify_subscription_in_cart_page(self, open_cart_page, page: Page):
        # self.test_should_verify_subscription_in_home_page(open_cart_page, page)

        with allure.step('Scroll down page to bottom'):
            page.locator('//h2[contains(text(),"Subscription")]').scroll_into_view_if_needed()

        with allure.step('Verify "SUBSCRIPTION" is visible'):
            expect(page.locator('//h2[contains(text(),"Subscription")]')).to_be_visible()

        with allure.step('Enter email address in input and click arrow button'):
            page.fill(pages.home_page.emailInput, data.user_data.email)
            page.click(pages.home_page.submitBtn)

        with allure.step('Verify success message "You have been successfully subscribed!" is visible'):
            expect(page.locator('.alert-success')).to_have_text("You have been successfully subscribed!")
