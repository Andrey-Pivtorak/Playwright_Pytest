from playwright.sync_api import expect, Page
import pages
import config
import data
import data.functions
import allure
import os


class TestProducts:

    @allure.title('Test verify all products and product detail page')
    def test_should_verify_all_products_and_product_detail_page(self, open_products_page: Page, page: Page):

        with allure.step('Move to product page'):
            page.click('a[href="/product_details/1"]')
            page.goto(config.url.DOMAIN + 'product_details/1')
            expect(page).to_have_url(config.url.DOMAIN + 'product_details/1')

        with allure.step('Verify that detail detail is visible'):
            tags = pages.products_page.productInfo_tags
            texts = pages.products_page.productInfo_texts
            for i in range(0, len(tags)-1):
                expect(page.locator(f'//{tags[i]}[contains(text(),"{texts[i]}")]')).to_be_visible()


    @allure.title('Test search product')
    def test_should_search_product(self, open_products_page, page: Page):

      with allure.step('Search product'):
        pages.products_page.search_product(page)

    @allure.title('Test view category products')
    def test_should_view_category_products(self, home_page, page: Page):

        with allure.step('Check "Category" is visible'):
            expect(page.locator(
            '//h2[contains(text(),"Category")]')).to_be_visible()

        with allure.step('Open "Women" category'):
            women_category_link = pages.home_page.womenCategoryLink
            pages.products_page.open_products_category_subcategory(page, 'Women', women_category_link, 1)

        with allure.step('Verify that user is navigated to that category page'):
            expect(page.locator('//h2[contains(text(),"Women")]')).to_have_text('Women - Dress Products')

        with allure.step('Open "Men" category'):
            men_category_link = pages.home_page.menCategoryLink
            pages.products_page.open_products_category_subcategory(page, 'Men', men_category_link, 3)

        with allure.step('Verify that user is navigated to that category page'):
            expect(page.locator('//h2[contains(text(),"Tshirts")]')).to_have_text('Men - Tshirts Products')


    @allure.title('Test view and cart brand products')
    def test_should_view_and_cart_brand_products(self, open_products_page, page: Page):

        with allure.step('Verify that Brands are visible on left side bar'):
            expect(page.locator('.brands_products h2')).to_be_visible()

        with allure.step('Click on any brand name'):
            page.click(pages.home_page.poloBrandLink)
            page.goto(config.url.DOMAIN + 'brand_products/Polo')

        with allure.step('Verify that user is navigated to brand page and brand products are displayed'):
            expect(page).to_have_url(config.url.DOMAIN + 'brand_products/Polo')
            expect(page.locator('//h2[contains(text(),"Polo")]')).to_be_visible()

        with allure.step('Click on other brand link'):
            page.click(pages.home_page.babyhugBrandLink)

        with allure.step('Verify that user is navigated to that brand page and can see products'):
            expect(page).to_have_url(config.url.DOMAIN + 'brand_products/Babyhug')
            expect(page.locator('//h2[contains(text(),"Babyhug")] /..')).to_be_visible()


    @allure.title('Test search products and verify cart after login')
    def test_should_search_products_and_verify_cart_after_login(self, open_products_page, page: Page):

        with allure.step('Verify user is navigated to ALL PRODUCTS page successfully'):
            expect(page.locator('//h2[contains(text(),"All Products")]')).to_be_visible()

        with allure.step('Search products'):
            pages.products_page.search_product(page)

        with allure.step('Verify "searched products" is visible'):
            expect(page.locator('//h2[contains(text(),"Searched Products")]')).to_be_visible()

        with allure.step('Add products to cart'):
            products = page.query_selector_all('.productinfo > .add-to-cart')
            for product in products:
                product.click()
                page.click('button[data-dismiss="modal"]')

        with allure.step('Open cart'):
            pages.products_page.open_cart(page)

        with allure.step('Verify that products are visible in cart'):
            cart_products = page.locator('#cart_info_table tbody tr').all()
            for prod in cart_products:
                expect(prod).to_be_visible()
        with allure.step('Login user on the site'):
            pages.login_page.open_login_page(page)
            pages.login_page.fill_login_form(page)

        with allure.step('Login user on the site'):
            pages.products_page.open_cart(page)

        with allure.step('Verify that products are visible'):
            for prod in cart_products:
                expect(prod).to_be_visible()


    @allure.title('Test add review on product')
    def test_should_add_review_on_product(self, open_products_page, page: Page):

        with allure.step('Click on "View Product" button'):
            page.click('a[href="/product_details/5"]')
            page.goto(config.url.DOMAIN + 'product_details/5')

        with allure.step('Verify "Write Your Review" is visible'):
            expect(page.locator('a[href="#reviews"]')).to_be_visible()
            expect(page.locator('a[href="#reviews"]')).to_have_text('Write Your Review')

        with allure.step('Enter name, email and review'):
            page.fill('#name', data.user_data.name)
            page.fill('#email', data.user_data.email)
            review_text = 'All QA engineers can use this website for automation practice and API testing either they are at beginner or advance level. This is for everybody to help them brush up their automation skills.'
            page.fill('#review', review_text)

        with allure.step('Click "Submit" button'):
            page.click('#button-review')

        with allure.step('Verify success message "Thank you for your review"'):
            expect(page.locator('.alert-success span')).to_be_visible()
            expect(page.locator('.alert-success span')).to_have_text('Thank you for your review.')


    @allure.title('Test add to cart from recommended items')
    def test_should_add_to_cart_from_recommended_items(self, home_page, page: Page):

        with allure.step('Scroll to bottom of page'):
            page.locator('.recommended_items > h2').scroll_into_view_if_needed()

        with allure.step('Verify "RECOMMENDED ITEMS" are visible'):
            expect(page.locator('.recommended_items > h2')).to_be_visible()
            expect(page.locator('.recommended_items > h2')).to_have_text('recommended items')

        with allure.step('Click on "Add To Cart" on Recommended product'):
            page.click('div[id="recommended-item-carousel"] .col-sm-4 a')

        with allure.step('Click on "View Cart" button'):
            page.click('#cartModal a[href="/view_cart"]')

        with allure.step('Verify that product is displayed in cart page'):
            expect(page.locator('tbody .cart_description h4')).to_be_visible()


    @allure.title('Test download invoice after purchase order')
    def test_should_download_invoice_after_purchase_order(self, home_page, page: Page):

        with allure.step('Add products to cart'):
            pages.products_page.add_products(page)

        with allure.step('Open cart'):
            pages.products_page.open_cart(page)

        with allure.step('Move to login page'):
            page.click('a.check_out')
            page.click('.modal-body a[href="/login"]')
            page.goto(config.url.DOMAIN + 'login')

        with allure.step('Registration new user'):
            data.functions.registration_new_user(page)

        with allure.step('Open cart'):
            pages.products_page.open_cart(page)

        with allure.step('Click "Proceed To Checkout" button'):
            page.click('a.check_out')
            page.goto(config.url.DOMAIN + 'checkout')

        with allure.step('Create order'):
            pages.products_page.create_order(page)

        with allure.step('Click "Download Invoice" button and verify invoice is downloaded successfully'):
            pages.products_page.check_downloading_file(page)
            assert os.path.isfile('data/invoice.txt')

        with allure.step('Click "Continue" button'):
            page.click('a[data-qa="continue-button"]')
            page.goto(config.url.DOMAIN)

        with allure.step('Delete account'):
            pages.products_page.delete_account(page)
