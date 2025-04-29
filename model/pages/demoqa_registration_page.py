import os

from selene import have, command, be
from selene.support.shared import browser

import tests


class RegistrationPage:
    def __init__(self):
        pass

    def open(self):
        browser.open('/automation-practice-form')

    def remove_banners(self):
        browser.driver.execute_script("$('#RightSide_Advertisement').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value).click()

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value).click()

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value).click()

    def fill_gender(self):
        browser.element('//label[contains(text(), "Female")]').click()

    def fill_mobile_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value).click()

    def fill_date_of_birth(self):
        browser.element("#dateOfBirthInput").click()
        browser.element('.react-datepicker__month-select').click().element('option[value="6"]').click()
        browser.element('.react-datepicker__year-select').click().element('option[value="1980"]').click()
        browser.element('.react-datepicker__day--022').click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value).press_enter()

    def fill_hobby(self):
        browser.element("label[for='hobbies-checkbox-2']").should(have.exact_text('Reading')).click()

    def upload_picture(self):
        browser.element('#uploadPicture').set_value(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), 'resources/picture.jpeg')
            )
        )

    def fill_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)

    def fill_state(self):
        browser.element("#state").click()
        browser.all('[id^="react-select-3-option"]').element_by(have.exact_text('NCR')).click()

    def fill_city(self):
        browser.element("#city").click()
        browser.all('[id^="react-select-4-option"]').element_by(have.exact_text('Gurgaon')).click()

    def submit(self):
        browser.element('#submit').click()

    def should_have_registered(self, full_name, email, gender, phone, date_of_birth, subject, hobbies, avatar,
                               current_address, city):
        browser.element('.modal-content').should(be.visible)
        browser.element('.modal-title').should(have.exact_text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone,
                date_of_birth,
                subject,
                hobbies,
                avatar,
                current_address,
                city
            )
        )
