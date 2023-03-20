import pages
import data
import data.functions
from playwright.sync_api import expect, Page
import config


class TestLogin:

    def test_should_login_user_with_correct_email_and_password(self, login_page, page: Page):
        expect(page.locator('.login-form h2')).to_be_visible()
        pages.login_page.fill_login_form(page)
        expect(page.locator('.fa-user')).to_be_visible()

        # not a logical action !!!
        # page.locator(pages.login_page.deleteAccountBtn).click()
        # expect(page.locator('h2[data-qa="account-deleted"]')).to_be_visible()

    def test_should_login_user_with_incorrect_email_and_password(self, login_page, page: Page):
        expect(page.locator('.login-form h2')).to_be_visible()
        pages.login_page.fill_login_form_incorrect(page)
        expect(page.locator(
            'input[data-qa="login-password"] ~ p')).to_have_text('Your email or password is incorrect!')


    def test_should_logout(self, login_page, page: Page):
        self.test_should_login_user_with_correct_email_and_password(login_page)
        page.locator(pages.login_page.logoutBtn).click()
        expect(page).to_have_url(config.url.DOMAIN + 'login')


    def test_should_register_user_with_existing_email(self, login_page, page: Page):
        expect(page.locator('.signup-form h2')).to_be_visible()
        pages.login_page.fill_signUp_form(page)
        expect(page.locator('input[data-qa="signup-name"] ~ p')).to_have_text('Email Address already exist!')

