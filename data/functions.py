from playwright.sync_api import Page, expect
import random
import string
import data
import data.functions
import pages
import config
import allure


def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    # Combine the character sets
    all_characters = letters + digits + symbols
    # Generate the password
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password


def generate_random_email():
    # Generate a random username
    username = ''.join(random.choices(
        string.ascii_letters + string.digits, k=10))
    # Generate a random domain name
    domain_name = ''.join(random.choices(string.ascii_lowercase, k=7))
    # Generate a random top-level domain (TLD)
    tlds = ['com', 'net', 'org', 'ua']
    tld = random.choice(tlds)
    # Combine the username, domain name, and TLD to form the email address
    email = f"{username}@{domain_name}.{tld}"
    return email


def registration_new_user(page: Page):
    expect(page.locator('.signup-form h2')).to_be_visible()

    page.fill(pages.login_page.nameInput, data.user_data.name)
    page.fill(pages.login_page.emailInput, data.functions.generate_random_email())
    page.locator(pages.login_page.signupBtn).click()
    expect(page.locator('.login-form :first-child b')).to_be_visible()

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
    page.locator(pages.login_page.countrySelect).select_option('United States')
    page.fill(pages.login_page.stateInput, data.user_data.state)
    page.fill(pages.login_page.cityInput, data.user_data.city)
    page.fill(pages.login_page.zipcodeInput, data.user_data.zipcode)
    page.fill(pages.login_page.mobileNumInput, data.user_data.mobile_number)
    page.locator(pages.login_page.createAccBtn).click()
    expect(page.locator('h2[data-qa="account-created"]')).to_be_visible()

    page.locator(pages.login_page.continueBtn).click()
    page.goto(config.url.DOMAIN)


def take_screenshot(page) -> None:
    allure.attach(
        body=page.screenshot(full_page=True),
        # name=name,
        attachment_type=allure.attachment_type.PNG
    )
