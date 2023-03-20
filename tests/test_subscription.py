from playwright.sync_api import expect, Page
import pages
import time
import data


class TestSubscription:

    def test_should_verify_subscription_in_home_page(self, home_page: Page):
        assert "SUBSCRIPTION" in home_page.inner_text("id=footer")
        home_page.fill(pages.home_page.emailInput, data.user_data.email)
        home_page.click(pages.home_page.submitBtn)
        expect(home_page.locator('.alert-success')).to_be_visible()


    def test_should_verify_subscription_in_cart_page(self, open_cart_page, page: Page):
        assert "SUBSCRIPTION" in page.inner_text('id=footer')
        page.fill(pages.home_page.emailInput, data.user_data.email)
        page.click(pages.home_page.submitBtn)
        expect(page.locator('.alert-success')).to_have_text("You have been successfully subscribed!")
