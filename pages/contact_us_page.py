from playwright.sync_api import expect
import config
import pages
import data


class ContactUsPage:

    nameInput = 'input[data-qa="name"]'
    emailInput = 'input[data-qa="email"]'
    subjectInput = 'input[data-qa="subject"]'
    messageInput = 'textarea[data-qa="message"]'
    uploadFileBtn = 'input[type="file"]'
    submitBtn = 'input[data-qa="submit-button"]'
    homeBtn = '.navbar-nav a[href="/"]'


    def open_contact_us_page(self, page):
        page.locator(pages.home_page.contactUsBtn).click()
        page.goto(config.url.DOMAIN + 'contact_us')


    def fill_contact_us_form(self, page):
        page.fill(pages.contact_us_page.nameInput, data.user_data.name)
        page.fill(pages.contact_us_page.emailInput, data.user_data.email)
        page.fill(pages.contact_us_page.subjectInput, 'Testing the "Contact us" form')
        page.fill(pages.contact_us_page.messageInput, 'Testing the "Contact us" form. If you have any suggestion areas or improvements, do let us know. We will definitely work on it.')
        page.set_input_files(pages.contact_us_page.uploadFileBtn, 'data/fileForUpload.txt')
