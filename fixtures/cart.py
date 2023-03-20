from playwright.sync_api import Page, expect
import config
import pytest
import pages


@pytest.fixture()
def open_cart_page(home_page, page: Page):
    page.click(pages.home_page.cartBtn)
    page.goto('https://automationexercise.com/view_cart')
    expect(page).to_have_url(config.url.DOMAIN + 'view_cart')
    yield open_cart_page
