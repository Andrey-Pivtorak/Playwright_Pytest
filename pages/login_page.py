from playwright.sync_api import Page

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



