import pytest
import allure


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
        # page.screenshot(path="failure.png")
        allure.attach(body=page.screenshot(),
                      name='screenshot_of_a_failed_test',
                      attachment_type=allure.attachment_type.PNG)
