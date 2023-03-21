from playwright.sync_api import Page, expect
import pytest
import pages
import config


@pytest.fixture()
def login_page(home_page, page: Page):
    page.locator(pages.home_page.loginBtn).click()
    page.goto(config.url.DOMAIN + 'login')
    expect(page).to_have_url(config.url.DOMAIN + 'login')
    yield login_page
