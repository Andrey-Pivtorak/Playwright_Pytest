import pages
import data
import data.functions
from playwright.sync_api import expect, Page
import config


class TestLogin:

    def test_login_user_with_correct_email_and_password(self, login_page: Page):
        expect(login_page.locator('.login-form h2')).to_be_visible()
        login_page.fill(pages.login_page.emailLoginInput, data.user_data.email)
        login_page.fill(pages.login_page.passwordInput,
                        data.user_data.password)
        login_page.locator(pages.login_page.loginBtn).click()
        expect(login_page.locator('.fa-user')).to_be_visible()

        # not a logical action !!!
        # page.locator(pages.login_page.deleteAccountBtn).click()
        # expect(page.locator('h2[data-qa="account-deleted"]')).to_be_visible()

    def test_login_user_with_incorrect_email_and_password(self, login_page: Page):
        expect(login_page.locator('.login-form h2')).to_be_visible()
        login_page.fill(pages.login_page.emailLoginInput,
                        data.user_data.incorrectEmail)
        login_page.fill(pages.login_page.passwordInput,
                        data.user_data.incorrectPassword)
        login_page.locator(pages.login_page.loginBtn).click()
        expect(login_page.locator(
            'input[data-qa="login-password"] ~ p')).to_be_visible()

    def test_logout(self, login_page, page: Page):
        self.test_login_user_with_correct_email_and_password(login_page)
        page.locator(pages.login_page.logoutBtn).click()
        expect(page).to_have_url(config.url.DOMAIN + 'login')


    def test_register_user_with_existing_email(self, login_page: Page):
        expect(login_page.locator('.signup-form h2')).to_be_visible()
        login_page.fill(pages.login_page.nameInput, data.user_data.name)
        login_page.fill(pages.login_page.emailInput,
                        data.user_data.email)
        login_page.locator(pages.login_page.signupBtn).click()
        expect(login_page.locator(
            'input[data-qa="signup-name"] ~ p')).to_be_visible()
