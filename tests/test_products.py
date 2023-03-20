from playwright.sync_api import expect, Page
import pages
import config
import data
import time


class TestProducts:

    def test_should_verify_all_products_and_product_detail_page(self, open_products_page: Page, page: Page):
        page.click('a[href="/product_details/1"]')
        page.goto(config.url.DOMAIN + 'product_details/1')
        expect(page).to_have_url(config.url.DOMAIN + 'product_details/1')

        tags = pages.products_page.productInfo_tags
        texts = pages.products_page.productInfo_texts
        for i in range(0, len(tags)-1):
            expect(page.locator(
                f'//{tags[i]}[contains(text(),"{texts[i]}")]')).to_be_visible()

    def test_should_search_product(self, open_products_page, page: Page):
        # search_text = 'Jeans'
        # page.fill(pages.products_page.searchbarInput, search_text)
        # page.click(pages.products_page.searchBtn)

        # search_elements = page.query_selector_all('.productinfo p')
        # for element in search_elements:
        #     element_text = element.inner_text()
        #     assert search_text in element_text, f"'{search_text}' not found in element: {element_text}"
        pages.products_page.search_product(page)



    def test_should_view_category_products(self, home_page, page: Page):
        expect(page.locator(
            '//h2[contains(text(),"Category")]')).to_be_visible()

        page.click(pages.home_page.womenCategoryLink)
        page.click('#Women ul > :first-child a')
        page.goto(config.url.DOMAIN + 'category_products/1')
        expect(page).to_have_url(config.url.DOMAIN + 'category_products/1')
        expect(page.locator('//h2[contains(text(),"Women")]')).to_have_text('Women - Dress Products')

        page.click(pages.home_page.menCategoryLink)
        page.click('#Men ul > :first-child a')
        expect(page.locator('//h2[contains(text(),"Tshirts")]')).to_have_text('Men - Tshirts Products')

    def test_should_view_and_cart_brand_products(self, open_products_page, page: Page):
        expect(page.locator('.brands_products h2')).to_be_visible()
        page.click(pages.home_page.poloBrandLink)
        page.goto(config.url.DOMAIN + 'brand_products/Polo')
        expect(page).to_have_url(config.url.DOMAIN + 'brand_products/Polo')
        expect(page.locator('//h2[contains(text(),"Polo")]')).to_be_visible()

        page.click(pages.home_page.babyhugBrandLink)
        expect(page).to_have_url(config.url.DOMAIN + 'brand_products/Babyhug')
        expect(page.locator('//h2[contains(text(),"Babyhug")] /..')).to_be_visible()


    def test_search_products_and_verify_cart_after_login(self, open_products_page, page: Page):
        expect(page.locator('//h2[contains(text(),"All Products")]')).to_be_visible()
        pages.products_page.search_product(page)

        products = page.query_selector_all('.productinfo > .add-to-cart')

        for product in products:
            product.click()
            page.click('button[data-dismiss="modal"]')

        page.click(pages.home_page.cartBtn)
        cart_products = page.locator('#cart_info_table tbody tr').all()

        for prod in cart_products:
            expect(prod).to_be_visible()

        page.click(pages.home_page.loginBtn)
        pages.login_page.fill_login_form(page)
        page.click(pages.home_page.cartBtn)

        for prod in cart_products:
            expect(prod).to_be_visible()


    def test_add_review_on_product(self, open_products_page, page: Page):
        page.click('a[href="/product_details/5"]')
        page.goto(config.url.DOMAIN + 'product_details/5')
        expect(page.locator('a[href="#reviews"]')).to_be_visible()
        expect(page.locator('a[href="#reviews"]')).to_have_text('Write Your Review')
        page.fill('#name', data.user_data.name)
        page.fill('#email', data.user_data.email)
        review_text = 'All QA engineers can use this website for automation practice and API testing either they are at beginner or advance level. This is for everybody to help them brush up their automation skills.'
        page.fill('#review', review_text)
        page.click('#button-review')
        expect(page.locator('.alert-success span')).to_be_visible()
        expect(page.locator('.alert-success span')).to_have_text('Thank you for your review.')


    def test_add_to_cart_fro_recommended_items(self, home_page, page: Page):
        page.locator('.recommended_items > h2').scroll_into_view_if_needed()
        expect(page.locator('.recommended_items > h2')).to_be_visible()
        expect(page.locator('.recommended_items > h2')).to_have_text('recommended items')
        page.click('div[id="recommended-item-carousel"] .col-sm-4 a')
        page.click('#cartModal a[href="/view_cart"]')
        expect(page.locator('tbody .cart_description h4')).to_be_visible()

        time.sleep(5)
