from playwright.sync_api import expect, Page
import pages
import config
import data.functions
import time

class TestAddressDetails:

    def test_should_verify_address_details_in_checkout_page(self, login_page, page: Page):
        data.functions.registration_new_user(page)
        page.click('.col-sm-9 div.features_items > :nth-child(3) .productinfo > a')
        page.click('.modal-footer button.btn-success')
        page.click('.col-sm-9 div.features_items > :nth-child(5) .productinfo > a')
        page.click('.modal-footer button.btn-success')
        page.click('.col-sm-9 div.features_items > :nth-child(7) .productinfo > a')
        page.click('.modal-footer button.btn-success')
        pages.products_page.open_cart(page)
        page.click('a.check_out')

        numb_address_items = [2, 3, 4, 5, 6, 7, 8]
        for num in numb_address_items:
            assert page.locator(f'#address_delivery > :nth-child({num})').inner_text() == page.locator(f'#address_invoice > :nth-child({num})').inner_text()


        time.sleep(7)
