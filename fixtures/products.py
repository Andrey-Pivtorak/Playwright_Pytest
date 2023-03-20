import pytest
import pages
from playwright.sync_api import Page, expect


@pytest.fixture()
def open_products_page(home_page: Page, page: Page):
    home_page.click(pages.home_page.productsBtn)
    page.goto('https://automationexercise.com/products')
    expect(page).to_have_title('Automation Exercise - All Products')
    expect(page.locator('//h2[contains(text(),"All Products")]')).to_be_visible()
    yield open_products_page
