from playwright.sync_api import expect, Page
import pages
import data


class TestContactUs:

    def test_contact_us_form(self, home_page: Page, page: Page):
        home_page.locator(pages.home_page.contactUsBtn).click()
        expect(page.locator('//h2[contains(text(),"Get In Touch")]')).to_be_visible()
        page.fill(pages.contact_us_page.nameInput, data.user_data.name)
        page.fill(pages.contact_us_page.emailInput, data.user_data.email)
        page.fill(pages.contact_us_page.subjectInput, 'Testing the "Contact us" form')
        page.fill(pages.contact_us_page.messageInput, 'Testing the "Contact us" form. If you have any suggestion areas or improvements, do let us know. We will definitely work on it.')
        page.set_input_files(pages.contact_us_page.uploadFileBtn, 'data/fileForUpload.txt')

        page.on("dialog", lambda dialog: dialog.accept())
        page.click(pages.contact_us_page.submitBtn)

        expect(page.locator('h2 ~ div.alert-success')).to_be_visible()
