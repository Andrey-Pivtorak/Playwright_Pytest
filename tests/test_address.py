from playwright.sync_api import Page
import pages
import data.functions
import allure


class TestAddressDetails:

    @allure.title('Test for verification address details in checkout page')
    def test_should_verify_address_details_in_checkout_page(self, login_page, page: Page, screenshot_if_failure):
      with allure.step('Registration a new user'):
            data.functions.registration_new_user(page)

      with allure.step('Add products into cart'):
          for num in [3, 5, 9]:
              page.click(f'.col-sm-9 div.features_items > :nth-child({num}) .productinfo > a')
              page.click('.modal-footer button.btn-success')

      with allure.step('Open cart'):
          pages.products_page.open_cart(page)
          page.click('a.check_out')

      with allure.step('Element matching check'):
          numb_address_items = [2, 3, 4, 5, 6, 7, 8]
          for num in numb_address_items:
            assert page.locator(f'#address_delivery > :nth-child({num})').inner_text() == page.locator(f'#address_invoice > :nth-child({num})').inner_text()
