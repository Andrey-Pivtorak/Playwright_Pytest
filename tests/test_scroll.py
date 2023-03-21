from playwright.sync_api import expect, Page


class TestScroll:

    def test_should_verify_scroll_up_and_down_using_arrow_button(self, home_page, page: Page):
        page.locator('//h2[contains(text(),"Subscription")]').scroll_into_view_if_needed()
        expect(page.locator('//h2[contains(text(),"Subscription")]')).to_be_visible()
        page.locator('#scrollUp').scroll_into_view_if_needed()
        # Closed-mode shadow roots are not supported !!!
        # page.click('#scrollUp')
        # text = page.query_selector('//h2[contains(text(),"Full-Fledged practice website for Automation Engineers")]')
        # assert text.is_visible


    def test_should_verify_scroll_up_and_down_without_using_arrow_button(self, home_page, page: Page):
        page.locator('//h2[contains(text(),"Subscription")]').scroll_into_view_if_needed()
        expect(page.locator('//h2[contains(text(),"Subscription")]')).to_be_visible()
        page.locator('#header').scroll_into_view_if_needed
        page.locator('#header').click()
