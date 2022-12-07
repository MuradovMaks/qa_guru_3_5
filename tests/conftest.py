import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture

def open_browser():
    browser.config.timeout = 6.0
    print("Тренажер открыт")
    yield
    browser.quit()
    print("Тренажер закрыт")



