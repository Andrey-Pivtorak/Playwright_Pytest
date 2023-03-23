from playwright.sync_api import expect, Page
import pages
import config
import allure


class TestLogin:

    @allure.title('Test login user with correct email and password')
    def test_should_login_user_with_correct_email_and_password(self, login_page, page: Page):

        with allure.step('Check login form is visible'):
            expect(page.locator('.login-form h2')).to_be_visible()

        with allure.step('Fill login form with correct credentials'):
            pages.login_page.fill_login_form(page)

        with allure.step('Check is user logged'):
            expect(page.locator('.fa-user')).to_be_visible()
        # Not a logical action !!!
        # page.locator(pages.login_page.deleteAccountBtn).click()
        # expect(page.locator('h2[data-qa="account-deleted"]')).to_be_visible()


    @allure.title('Test login user with incorrect email and password')
    def test_should_login_user_with_incorrect_email_and_password(self, login_page, page: Page):

        with allure.step('Check "login form" is visible'):
            expect(page.locator('.login-form h2')).to_be_visible()

        with allure.step('Fill login form with incorrect credentials'):
            pages.login_page.fill_login_form_incorrect(page)

        with allure.step('Check the message is showed about wrong credentials'):
            expect(page.locator(
            'input[data-qa="login-password"] ~ p')).to_have_text('Your email or password is incorrect!')


    @allure.title('Test logout user')
    def test_should_logout(self, login_page, page: Page):

        with allure.step('Login user on the site'):
            self.test_should_login_user_with_correct_email_and_password(login_page, page)

        with allure.step('Logout user'):
            page.locator(pages.login_page.logoutBtn).click()
            expect(page).to_have_url(config.url.DOMAIN + 'login')


    @allure.title('Test register user with existing email')
    def test_should_register_user_with_existing_email(self, login_page, page: Page):

        with allure.step('Check "sign up" form is visible'):
            expect(page.locator('.signup-form h2')).to_be_visible()

        with allure.step('Fill "sign up" form'):
            pages.login_page.fill_signUp_form_with_exist_email(page)

        with allure.step('Check message is showed that email has already exist'):
            expect(page.locator('input[data-qa="signup-email"] ~ p')).to_have_text('Email Address already exist!')
