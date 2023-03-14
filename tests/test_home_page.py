import pytest
import pages
import data
import data.functions
import config
from playwright.sync_api import expect, Page
import time

class TestRegister:

    def test_user_should_be_able_to_register(self, page: Page):
        pages.home_page.open_homepage(page)

        page.locator(pages.home_page.loginBtn).click()
        expect(page.locator('.signup-form h2')).to_be_visible()

        page.fill(pages.login_page.nameInput, data.user_data.name)
        page.fill(pages.login_page.emailInput, data.functions.generate_random_email())


        page.locator(pages.login_page.signupBtn).click()
        expect(page.locator('.login-form :first-child b')).to_be_visible()
        page.locator(pages.login_page.titleRadioBtn).click()
        page.fill(pages.login_page.passwordInput, data.user_data.password)
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
        expect(page.locator('.fa-user')).to_be_visible()
        page.locator(pages.login_page.deleteAccountBtn).click()
        expect(page.locator('h2[data-qa="account-deleted"]')).to_be_visible()
        time.sleep(2)

