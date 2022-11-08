from selenium import webdriver
class Uimethod:


    def __init__(self, setup):
        self.driver=setup
        self.driver.find_element_by_id()..

    def click_by_xpath(self, locator):
        return self.driver.find_element_by_id(locator).click()

    def click_by_id(self, locator):
        return self.driver.find_element_by_id(locator).click()

    def click_by_class_name(self, locator):
        return self.driver.find_element_by_class_name(locator).click()

    def click_by_css_selector(self, locator):
        return self.driver.find_element_by_css_selector(locator).click()

    def send_key_id(self,locator,input):
        return self.driver.find_element_by_id(locator).send_keys(input)

    def send_key_xpath(self, locator, input):
        return self.driver.find_element_by_xpath(locator).send_keys(input)

    def send_key_class_name(self, locator, input):
        return self.driver.find_element_by_class_name(locator).send_keys(input)

    def send_key_css_selector(self, locator, input):
        return self.driver.find_element_by_css_selector(locator).send_keys(input)


