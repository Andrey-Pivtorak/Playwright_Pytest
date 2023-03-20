from playwright.sync_api import Page
import pages
import data

class LoginPage:

    nameInput = 'input[data-qa="signup-name"]'
    emailInput = 'input[data-qa="signup-email"]'
    emailLoginInput = 'input[data-qa="login-email"]'
    passwordInput = 'input[data-qa="login-password"]'
    loginBtn = 'button[data-qa="login-button"]'
    # emailFilled = '#email'
    signupBtn = 'button[data-qa="signup-button"]'
    accountInfoTitle = '.login-form :first-child b'
    titleRadioBtn = '#id_gender1'
    passwordInput_signup = '#password'
    daySelect = '#days'
    monthSelect = '#months'
    yearSelect = '#years'
    signUpCheckBox = '#newsletter'
    receiveOffersCheckBox = '#optin'
    firstNameInput = '#first_name'
    lastNameInput = '#last_name'
    companyInput = '#company'
    addressInput = '#address1'
    address2Input = '#address2'
    countrySelect = '#country'
    stateInput = '#state'
    cityInput = '#city'
    zipcodeInput = '#zipcode'
    mobileNumInput = '#mobile_number'
    createAccBtn = 'button[data-qa="create-account"]'
    continueBtn = 'a[data-qa="continue-button"]'
    deleteAccountBtn = 'a[href="/delete_account"]'
    logoutBtn = '.navbar-nav a[href="/logout"]'


    def fill_login_form(self, page):
        page.fill(pages.login_page.emailLoginInput, data.user_data.email)
        page.fill(pages.login_page.passwordInput, data.user_data.password)
        page.locator(pages.login_page.loginBtn).click()


    def fill_login_form_incorrect(self, page):
        page.fill(pages.login_page.emailLoginInput, data.user_data.incorrectEmail)
        page.fill(pages.login_page.passwordInput, data.user_data.incorrectPassword)
        page.locator(pages.login_page.loginBtn).click()


    def fill_signUp_form(self, page):
        page.fill(pages.login_page.nameInput, data.user_data.name)
        page.fill(pages.login_page.emailInput,
                        data.user_data.email)
        page.locator(pages.login_page.signupBtn).click()
