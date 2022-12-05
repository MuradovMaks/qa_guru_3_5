from selene import be, have
from selene.support.shared import browser
import os
###

def test_send_document(open_browser):
    browser.open("https://demoqa.com/automation-practice-form")
    browser.element("#firstName").should(be.blank).type("Max")
    browser.element("[id=lastName]").type("Muradov")
    browser.element("[id=userEmail]").type("koreantech620@mail.ru")
    browser.element("[id=gender-radio-1]").double_click()
    browser.element("[id=userNumber]").type("0790345439")
    browser.element('#dateOfBirthInput').click()
    browser.element('[class ="react-datepicker__month-select"] >[value="3"]').click()
    browser.element('[class="react-datepicker__year-select"] >[value="2000"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--024"]').click()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[id="currentAddress"]').type("Greenwich Time")
    browser.element('[id="subjectsInput"]').type("Hindi").press_enter()
    browser.element('[id="react-select-3-input"]').type("NCR").press_enter()
    browser.element('[id="react-select-4-input"]').type("Noida").press_enter()
    browser.element('#uploadPicture').set_value(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'tests/1614256626_python_log.jpg')))
    browser.element("[id = submit]").submit()






