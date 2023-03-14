from playwright.sync_api import Page, expect

class ContactUsPage:

    nameInput = 'input[data-qa="name"]'
    emailInput = 'input[data-qa="email"]'
    subjectInput = 'input[data-qa="subject"]'
    messageInput = 'textarea[data-qa="message"]'
    uploadFileBtn = 'input[type="file"]'
    submitBtn = 'input[data-qa="submit-button"]'
    
    message = 'h2 ~ div.alert-success'
