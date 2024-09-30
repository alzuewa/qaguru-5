from os import path

from selene import be, browser, command, have


def test_fill_in_practice_form(driver):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

    browser.element('#firstName').type('Tom')
    browser.element('#lastName').type('Brown')
    browser.element('#userEmail').type('tombrown@test.test')
    browser.all('[name="gender"]').element_by(have.attribute('value', 'Male')).element('../label').click()
    browser.element('#userNumber').type('1234567890')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="8"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1970"]').click()
    browser.element('.react-datepicker__day--001').click()

    browser.element('#subjectsInput').type('e')
    browser.element('.subjects-auto-complete__menu-list').element('//*[text()="English"]').click()
    browser.element('#subjectsInput').type('a')
    browser.element('.subjects-auto-complete__menu-list').element('//*[text()="Arts"]').perform(
        command.js.scroll_into_view).click()

    browser.element('//label[text()="Sports"]').click()

    browser.element('#uploadPicture').set_value(
        path.abspath(path.join('../resources/image.jpg'))
    )

    browser.element('#currentAddress').type('Any random place here')
    browser.element('#state').click()
    browser.element('//*[text()="Uttar Pradesh"]').click()
    browser.element('#city').click()
    browser.element('//*[text()="Lucknow"]').click()

    browser.element('#dateOfBirthInput').should(have.attribute('value', '01 Sep 1970'))
    browser.all('.subjects-auto-complete__multi-value__label').should(have.exact_texts('English', 'Arts'))
    browser.element('.subjects-auto-complete__multi-value__remove').should(be.visible)
    browser.all('[type="checkbox"]').first.should(have.attribute('value', '1'))

    browser.element('button#submit').click()

    browser.element('table').should(be.visible)
    browser.element('//table//td[text()="Student Name"]/../td[2]').should(have.exact_text('Tom Brown'))
    browser.element('//table//td[text()="Student Email"]/../td[2]').should(have.exact_text('tombrown@test.test'))
    browser.element('//table//td[text()="Gender"]/../td[2]').should(have.exact_text('Male'))
    browser.element('//table//td[text()="Mobile"]/../td[2]').should(have.exact_text('1234567890'))
    browser.element('//table//td[text()="Date of Birth"]/../td[2]').should(have.exact_text('01 September,1970'))
    browser.element('//table//td[text()="Subjects"]/../td[2]').should(have.exact_text('English, Arts'))
    browser.element('//table//td[text()="Hobbies"]/../td[2]').should(have.exact_text('Sports'))
    browser.element('//table//td[text()="Picture"]/../td[2]').should(have.exact_text('image.jpg'))
    browser.element('//table//td[text()="Address"]/../td[2]').should(have.exact_text('Any random place here'))
    browser.element('//table//td[text()="State and City"]/../td[2]').should(have.exact_text('Uttar Pradesh Lucknow'))
