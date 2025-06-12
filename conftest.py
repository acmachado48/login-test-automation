import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options



@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver

    driver.quit()
