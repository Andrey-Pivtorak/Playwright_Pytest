import pytest
import pages
from playwright.sync_api import Page, expect


@pytest.fixture()
def login_page(home_page: Page, page: Page):
    home_page.locator(pages.home_page.loginBtn).click()
    expect(page).to_have_url('https://automationexercise.com/login')
    # yield home_page
    yield login_page
