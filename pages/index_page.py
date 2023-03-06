from playwright.sync_api import Page
import config

class IndexPage:

    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)
