from playwright.sync_api import expect, Page
import pages
import data.functions
import data


class TestCart:

    def test_should_add_products_in_cart(self, open_products_page, page: Page):
        page.click('a[data-product-id="1"]')
        page.click('.modal-footer .btn-success')
        page.click('a[data-product-id="2"]')
        page.click('.modal-body a[href="/view_cart"]')
        expect(page.locator('#product-1')).to_be_visible()
        expect(page.locator('#product-2')).to_be_visible()
        expect(page.locator('#product-1 .cart_price p')).to_contain_text('Rs.')
        expect(page.locator('#product-2 .cart_price p')).to_contain_text('Rs.')
        assert page.locator('#product-1 .cart_quantity button').inner_text() != ''
        assert page.locator('#product-2 .cart_quantity button').inner_text() != ''
        expect(page.locator('#product-1 .cart_total p')).to_contain_text('Rs.')
        expect(page.locator('#product-2 .cart_total p')).to_contain_text('Rs.')


    def test_should_verify_product_quantity_in_cart(self, home_page, page: Page):
        page.click('a[href="/product_details/3"]')
        page.goto('https://automationexercise.com/product_details/3')
        page.fill('#quantity', '4')
        page.click('.cart')
        page.click('.modal-body a[href="/view_cart"]')
        expect(page.locator('a[href="/product_details/3"]')).to_be_visible()
        expect(page.locator('.cart_quantity button')).to_have_text('4')


    def test_should_register_while_checkout(self, open_products_page, page: Page):
        pages.products_page.add_products(page)
        pages.products_page.open_cart(page)
        page.click('a.check_out')
        page.click('#checkoutModal a[href="/login"]')

        data.functions.registration_new_user(page)
        expect(page.locator('.fa-user ~ b')).to_have_text(data.user_data.name)
        pages.products_page.open_cart(page)
        page.click('a.check_out')
        pages.products_page.create_order(page)
        pages.products_page.delete_account(page)


    def test_should_register_before_checkout(self, login_page, page: Page):
        data.functions.registration_new_user(page)
        expect(page.locator('.fa-user ~ b')).to_have_text(data.user_data.name)

        pages.products_page.add_products(page)
        pages.products_page.open_cart(page)
        page.click('a.check_out')
        pages.products_page.create_order(page)
        pages.products_page.delete_account(page)


    def test_should_login_before_checkout(self, login_page, page: Page):
        pages.login_page.fill_login_form(page)
        expect(page.locator('.fa-user ~ b')).to_have_text(data.user_data.name)
        pages.products_page.add_products(page)
        pages.products_page.open_cart(page)
        page.click('a.check_out')
        pages.products_page.create_order(page)
        #Not a logical action !!!
        # pages.products_page.delete_account(page)


    def test_should_remove_products_from_cart(self, home_page, page: Page):
        pages.products_page.add_products(page)
        pages.products_page.open_cart(page)
        pages.products_page.delete_all_products(page)
        expect(page.locator('#empty_cart b')).to_have_text('Cart is empty!')

