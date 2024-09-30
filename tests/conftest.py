import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture
def driver():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    yield
