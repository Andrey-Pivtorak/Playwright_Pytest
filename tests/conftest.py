import pytest
import allure
from playwright.sync_api import Playwright, Browser, Page, sync_playwright, Browser, BrowserContext
import os


pytest_plugins = [
    'fixtures.page',
    'fixtures.login',
    'fixtures.home_page',
    'fixtures.products',
    'fixtures.cart'
]


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object.
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def screenshot_if_failure(request, page):
    yield
    if request.node.rep_call.failed:
        allure.attach(body=page.screenshot(),
                      name='screenshot_of_a_failed_test',
                      attachment_type=allure.attachment_type.PNG)


def get_browser(playwright: Playwright, browser_name: str) -> Browser:
    os.environ['LOCALE'] = 'en-US'
    if browser_name == 'firefox':
        return get_firefox_browser(playwright)
    elif browser_name == 'chrome':
        return get_chrome_browser(playwright)
    elif browser_name == 'edge':
        return get_edge_browser(playwright)
    else:
        return get_chrome_browser(playwright)


def get_firefox_browser(playwright: Playwright) -> Browser:
    return playwright.firefox.launch(headless=False, slow_mo=50)


def get_chrome_browser(playwright: Playwright) -> Browser:
    return playwright.chromium.launch(headless=False, slow_mo=50)


def get_edge_browser(playwright: Playwright) -> Browser:
    edge = playwright.webkit
    browser = edge.launch(headless=False, slow_mo=50)
    return browser


def get_context(browser: Browser) -> BrowserContext:
    return browser.new_context()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox", "edge"],
        help="Specify the browser to use for testing"
    )


@pytest.fixture(scope='session')
def playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope='session')
def browser(playwright: Playwright, request) -> Browser:
    browser_name = request.config.getoption("--test-browser")
    browser = get_browser(playwright, browser_name)
    yield browser
    browser.close()


@pytest.fixture(scope='function')
def context(browser: Browser) -> BrowserContext:
    context = get_context(browser)
    yield context
    context.close()


@pytest.fixture(scope='function')
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    page.set_viewport_size({'width': 1500, 'height': 700})
    yield page
    page.close()
