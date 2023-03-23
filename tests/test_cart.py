from playwright.sync_api import expect, Page
import pages
import data.functions
import data
import allure


class TestCart:

    @allure.title('Test to add products in cart')
    def test_should_add_products_in_cart(self, open_products_page, page: Page, screenshot_if_failure):

        with allure.step('Add products into cart'):
            pages.products_page.add_products(page)

        with allure.step('Open cart'):
            pages.products_page.open_cart(page)

        with allure.step('Check products details'):
            for num in [1, 2]:
                expect(page.locator(f'#product-{num}')).to_be_visible()
                expect(page.locator(f'#product-{num} .cart_price p')).to_contain_text('Rs.')
                assert page.locator(f'#product-{num} .cart_quantity button').inner_text() != ''
                expect(page.locator(f'#product-{num} .cart_total p')).to_contain_text('Rs.')


    @allure.title('Test verify product quantity in cart')
    def test_should_verify_product_quantity_in_cart(self, home_page, page: Page, screenshot_if_failure):

        with allure.step('Open product details'):
            page.click('a[href="/product_details/3"]')
            page.goto('https://automationexercise.com/product_details/3')

        with allure.step('Set quantity "4"'):
            page.fill('#quantity', '4')

        with allure.step('Open cart'):
            page.click('.cart')
            page.click('.modal-body a[href="/view_cart"]')

        with allure.step('Check the quantity count'):
            expect(page.locator('a[href="/product_details/3"]')).to_be_visible()
            expect(page.locator('.cart_quantity button')).to_have_text('4')


    @allure.title('Test register while checkout')
    def test_should_register_while_checkout(self, open_products_page, page: Page, screenshot_if_failure):

        with allure.step('Add products into cart'):
            pages.products_page.add_products(page)

        with allure.step('Open cart'):
            pages.products_page.open_cart(page)

        with allure.step('Move to the login page'):
            page.click('a.check_out')
            page.click('#checkoutModal a[href="/login"]')

        with allure.step('Registration new user'):
            data.functions.registration_new_user(page)
            expect(page.locator('.fa-user ~ b')).to_have_text(data.user_data.name)

        with allure.step('Open cart'):
            pages.products_page.open_cart(page)

        with allure.step('Create order'):
            page.click('a.check_out')
            pages.products_page.create_order(page)

        with allure.step('Delete account'):
            pages.products_page.delete_account(page)


    @allure.title('Test register before checkout')
    def test_should_register_before_checkout(self, login_page, page: Page, screenshot_if_failure):

        with allure.step('Registration new user'):
            data.functions.registration_new_user(page)
            expect(page.locator('.fa-user ~ b')).to_have_text(data.user_data.name)

        with allure.step('Add products into cart'):
            pages.products_page.add_products(page)

        with allure.step('Open cart'):
            pages.products_page.open_cart(page)
            page.click('a.check_out')

        with allure.step('Create order'):
            pages.products_page.create_order(page)

        with allure.step('Delete account'):
            pages.products_page.delete_account(page)


    @allure.title('Test login before checkout')
    def test_should_login_before_checkout(self, login_page, page: Page, screenshot_if_failure):

        with allure.step('Fill login form'):
            pages.login_page.fill_login_form(page)
            expect(page.locator('.fa-user ~ b')).to_have_text(data.user_data.name)

        with allure.step('Add products into cart'):
            pages.products_page.add_products(page)

        with allure.step('Open cart'):
            pages.products_page.open_cart(page)
            page.click('a.check_out')

        with allure.step('Create order'):
            pages.products_page.create_order(page)
        #Not a logical action !!!
        # pages.products_page.delete_account(page)

    @allure.title('Test remove products fro the cart')
    def test_should_remove_products_from_cart(self, home_page, page: Page, screenshot_if_failure):

        with allure.step('Add products into cart'):
            pages.products_page.add_products(page)

        with allure.step('Open cart'):
            pages.products_page.open_cart(page)

        with allure.step('Delete all products'):
            pages.products_page.delete_all_products(page)
            expect(page.locator('#empty_cart b')).to_have_text('Cart is empty!')
