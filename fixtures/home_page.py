import pytest
import config
from playwright.sync_api import Page, expect


@pytest.fixture()
def home_page(page: Page):
    page.goto(config.url.DOMAIN)
    expect(page).to_have_url(config.url.DOMAIN)
    yield page
