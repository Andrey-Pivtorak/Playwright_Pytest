from playwright.sync_api import expect, Page
import pages
import data
import data.functions
import allure


class TestRegister:

    @allure.title('Test user be able to register')
    def test_should_user_be_able_to_register(self, login_page, page: Page):

        with allure.step('Verify "New User Signup!" is visible'):
            expect(page.locator('.signup-form h2')).to_be_visible()

        with allure.step('Fill "sign up" form'):
            pages.login_page.fill_signUp_form(page)

        with allure.step('Verify that "ENTER ACCOUNT INFORMATION" is visible'):
            expect(page.locator('.login-form :first-child b')).to_be_visible()

        with allure.step('Fill details of "register" form'):
            page.locator(pages.login_page.titleRadioBtn).click()
            page.fill(pages.login_page.passwordInput_signup, data.user_data.password)
            page.locator(pages.login_page.daySelect).select_option('25')
            page.locator(pages.login_page.monthSelect).select_option('March')
            page.locator(pages.login_page.yearSelect).select_option('1998')
            page.locator(pages.login_page.signUpCheckBox).click()
            page.locator(pages.login_page.receiveOffersCheckBox).click()
            page.fill(pages.login_page.firstNameInput, data.user_data.first_name)
            page.fill(pages.login_page.lastNameInput, data.user_data.last_name)
            page.fill(pages.login_page.companyInput, data.user_data.company)
            page.fill(pages.login_page.addressInput, data.user_data.address)
            page.fill(pages.login_page.address2Input, data.user_data.address_2)
            page.locator(pages.login_page.countrySelect).select_option( 'United States')
            page.fill(pages.login_page.stateInput, data.user_data.state)
            page.fill(pages.login_page.cityInput, data.user_data.city)
            page.fill(pages.login_page.zipcodeInput, data.user_data.zipcode)
            page.fill(pages.login_page.mobileNumInput, data.user_data.mobile_number)

        with allure.step('Click "Create Account button"'):
            page.click(pages.login_page.createAccBtn)

        with allure.step('Verify that "ACCOUNT CREATED!" is visible'):
            expect(page.locator('h2[data-qa="account-created"]')).to_be_visible()

        with allure.step('Click "Continue" button'):
            page.locator(pages.login_page.continueBtn).click()

        with allure.step('Verify that "Logged in as username" is visible'):
            expect(page.locator('.fa-user')).to_be_visible()

        with allure.step('Delete account'):
            page.locator(pages.login_page.deleteAccountBtn).click()
            expect(page.locator('h2[data-qa="account-deleted"]')).to_be_visible()
