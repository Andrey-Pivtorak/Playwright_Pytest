import pytest
import pages
from playwright.sync_api import Page


@pytest.fixture()
def login_page(home_page: Page):
    home_page.locator(pages.home_page.loginBtn).click()
    yield home_page
