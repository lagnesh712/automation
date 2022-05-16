import pytest
from selenium import webdriver



@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path='/home/lagnesh/Downloads/chromedriver_linux64/chromedriver')
    driver.get("https://www.amazon.in")
    driver.maximize_window()
    return driver