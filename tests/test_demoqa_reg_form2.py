import time
import os
from demoqa_tests.model.page.registration_page import RegistrationPage
from selene_in_action_py13.conditions import match
from selene import browser
from selene.support.shared import browser


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # ---------------

    registration_page.type_first_name('Lucy')


    registration_page.type_last_name('Bechtel')


    registration_page.type_user_email('aslavret87@gmail.com')


    registration_page.select_gender('[for=gender-radio-2]')


    registration_page.type_user_number('0123456789')


    # ---------------

    registration_page.select_date_of_birth('[value = "6"]', '[value = "2005"]')

    # ---------------

    registration_page.type_subjects('Arts', 'En' )


    registration_page.select_hobbies('[for=hobbies-checkbox-2]')

    # ---------------

    registration_page.upload_picture('resources/original.jpg')

    # ----------------

    registration_page.type_current_address('426 Jordy Lodge Cartwrightshire, SC 88120-6700')


    registration_page.select_state('Haryana')


    registration_page.select_city('Panipat')


    # ---------------

    registration_page.submit_button_click()


    # ---------------

    registration_page.should_have_registered(
        [
        'Student Name Lucy Bechtel',
        'Student Email aslavret87@gmail.com',
        'Gender Female',
        'Mobile 0123456789',
        'Date of Birth 20 July,2005',
        'Subjects Arts, English',
        'Hobbies Reading',
        'Picture original.jpg',
        'Address 426 Jordy Lodge Cartwrightshire, SC 88120-6700',
        'State and City Haryana Panipat'
        ]
    )

    registration_page.close_button_click()
