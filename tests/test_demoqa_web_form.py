from selene import browser, have, be
import os

import tests


def test_demoqa_form():
    # Открываем форму
    browser.open('/automation-practice-form')

    # Удаляем баннеры
    browser.driver.execute_script("$('#RightSide_Advertisement').remove()")
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

    # Создаем переменные для заполнения формы
    first_name = 'Masha'
    last_name = 'Ivanova'
    email = 'MIvanova@yandex.ru'
    mobile = '5648765439'
    current_address = 'Moscow, Pionovaya street, 12'
    subject = 'History'

    # Заполняем поля формы
    browser.element('#firstName').should(be.blank).type(first_name).click()
    browser.element('#lastName').should(be.blank).type(last_name).click()
    browser.element('#userEmail').should(be.blank).type(email).click()
    browser.element('//label[contains(text(), "Female")]').click()
    browser.element('#userNumber').should(be.blank).type(mobile).click()
    browser.element("#dateOfBirthInput").click()
    browser.element('.react-datepicker__month-select').click().element('option[value="7"]').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1980"]').click()
    browser.element('.react-datepicker__day--022').click()
    browser.element('#subjectsInput').should(be.blank).type(subject).press_enter()
    browser.element("label[for='hobbies-checkbox-2']").should(have.exact_text('Reading')).click()
    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(tests.__file__), 'resources/picture.jpeg')
        )
    )
    browser.element('#currentAddress').should(be.blank).type(current_address)
    browser.element("#state").click()
    browser.all('[id^="react-select-3-option"]').element_by(have.exact_text('NCR')).click()
    browser.element("#city").click()
    browser.all('[id^="react-select-4-option"]').element_by(have.exact_text('Gurgaon')).click()

    # Сохраняем форму
    browser.element('#submit').click()

    # Проверяем, что форма сохранена
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.element('.modal-content').should(be.visible)

    # Проверяем значение полей в сохраненной форме
    browser.element(".table").should(have.text(first_name + ' ' + last_name))
    browser.element(".table").should(have.text(email))
    browser.element(".table").should(have.text('Female'))
    browser.element(".table").should(have.text(mobile))
    browser.element(".table").should(have.text('22 August,1980'))
    browser.element(".table").should(have.text(subject))
    browser.element(".table").should(have.text('Reading'))
    browser.element(".table").should(have.text('picture.jpeg'))
    browser.element(".table").should(have.text(current_address))
    browser.element(".table").should(have.text('NCR Gurgaon'))
