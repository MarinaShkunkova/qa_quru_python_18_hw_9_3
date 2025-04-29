from model.pages.demoqa_registration_page import RegistrationPage


def test_demoqa_registration_form():
    registration_page = RegistrationPage()
    # GIVEN
    registration_page.open()
    registration_page.remove_banners()

    # WHEN
    registration_page.fill_first_name('Masha')
    registration_page.fill_last_name('Ivanova')
    registration_page.fill_email('MIvanova@yandex.ru')
    registration_page.fill_gender()
    registration_page.fill_mobile_number('5648765439')
    # registration_page.fill_date_of_birth(1987, 1, 22)
    registration_page.fill_date_of_birth()
    registration_page.fill_subject('History')
    registration_page.fill_hobby()
    registration_page.upload_picture()
    registration_page.fill_address('Moscow, Pionovaya street, 12')
    registration_page.fill_state()
    registration_page.fill_city()
    registration_page.submit()

    # THEN
    registration_page.should_have_registered(
        'Masha Ivanova',
        'MIvanova@yandex.ru',
        'Female',
        '5648765439',
        '22 July,1980',
        'History',
        'Reading',
        'picture.jpeg',
        'Moscow, Pionovaya street, 12',
        'NCR Gurgaon',
    )
