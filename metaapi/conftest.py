# from selenium import webdriver
# import pytest
#
# @pytest.fixture()
# def setup():
#     driver=webdriver.Chrome(executable_path='/home/lagnesh/Downloads/chromedriver_linux64/chromedriver')
#     driver.get("https://www.facebook.com")
#     return driver

import pytest
from selenium import webdriver



@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path='/home/lagnesh/Downloads/chromedriver_linux64/chromedriver')
    driver.get("https://www.facebook.com")
    driver.maximize_window()
    return driver