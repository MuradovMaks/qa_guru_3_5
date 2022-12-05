import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture

def open_browser():
    width = browser.config.window_width = 1920
    height = browser.config.window_height = 1080
    print("Тренажер открыт")
    yield width,height
    browser.quit()
    print("Тренажер закрыт")



