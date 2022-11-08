import json
from conftest import setup

class Home_page:
    with open('./../test_data/data.json',"r") as f1:
        f2= f1.read()
    data=json.loads(f2)
    home_button=data["home_button_xpath"]
    search_bar=data["search_bar_class"]
    search_button=data["search_button_xpath"]

    def __init__(self):
        self.driver=setup()

    def search(self):
        self.driver.find_element_by_xpath(self.home_button).click()
        self.driver.find_element_by_class_name(self.search_bar).send_keys("Men shirts")
        self.driver.find_element_by_xpath(self.search_button).click()









