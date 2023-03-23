from playwright.sync_api import Page, expect
import pages
import config
import allure


class ProductsPage:

    productInfo_tags = ['h2', 'p', 'span', 'p', 'p', 'p']
    productInfo_texts = ['Blue Top', 'Category: Women > Tops', 'Rs. 500', ' In Stock', ' New', ' Polo']
    searchbarInput = 'input[id="search_product"]'
    searchBtn = 'button[id="submit_search"]'


    def add_products(self, page):
        page.click('a[data-product-id="1"]')
        page.click('.modal-footer .btn-success')
        page.click('a[data-product-id="2"]')
        page.click('.modal-footer .btn-success')


    def open_cart(self, page):
        page.click(pages.home_page.cartBtn)
        page.goto(config.url.DOMAIN + 'view_cart')
        expect(page).to_have_url(config.url.DOMAIN + 'view_cart')


    def create_order(self, page):
        expect(page.locator('//h2[contains(text(),"Address Details")]')).to_be_visible()
        expect(page.locator('//h2[contains(text(),"Review Your Order")]')).to_be_visible()

        page.fill('.form-control', 'Testing the "Comment" form. If you have any suggestion areas or improvements, do let us know. We will definitely work on it.')
        page.click('a[href="/payment"]')
        page.goto(config.url.DOMAIN + 'payment')

        page.fill('input[data-qa="name-on-card"]', 'SuperVisa')
        page.fill('input[data-qa="card-number"]', '1234567898765432')
        page.fill('input[data-qa="cvc"]', '123')
        page.fill('input[data-qa="expiry-month"]', '11')
        page.fill('input[data-qa="expiry-year"]', '2025')
        page.click('#submit')
        expect(page.locator('h2[data-qa="order-placed"] ~ p')).to_have_text('Congratulations! Your order has been confirmed!')


    def delete_account(self, page):
        page.click(pages.login_page.deleteAccountBtn)
        expect(page.locator('h2[data-qa="account-deleted"] b')).to_have_text('Account Deleted!')
        page.click('a[data-qa="continue-button"]')
        page.goto(config.url.DOMAIN)


    def delete_all_products(self, page: Page):
        products = page.query_selector_all('.cart_quantity_delete')
        for product in products:
            product.click()


    def search_product(self, page):
        search_text = 'Jeans'
        page.fill(pages.products_page.searchbarInput, search_text)
        page.click(pages.products_page.searchBtn)

        search_elements = page.query_selector_all('.productinfo p')
        for element in search_elements:
            element_text = element.inner_text()
            assert search_text in element_text, f"'{search_text}' not found in element: {element_text}"


    def check_downloading_file(self, page):
        with page.expect_download() as download_info:
            page.get_by_text("Download Invoice").click()
            download = download_info.value
            print(download.path())
            download.save_as("data/invoice.txt")

    def open_products_category_subcategory(self, page, category_name, category_link, product_num):
        with allure.step(f'Open "{category_name}" category'):
            page.click(category_link)

        with allure.step(f'Open "{category_name}" sub-category'):
            page.click(f'#{category_name} ul > :first-child a')
            page.goto(config.url.DOMAIN + f'category_products/{product_num}')

        with allure.step('Verify that user is navigated to that category page'):
            expect(page).to_have_url(config.url.DOMAIN + f'category_products/{product_num}')
