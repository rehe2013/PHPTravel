from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class Page(object):
    """
    Base class that all page models can inherit from
    """

    def __init__(self, selenium_driver, base_url="http://phptravels.net/"):
        # type: (object, object) -> object
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout=30


    def explicit_wait(self, time):
        return WebDriverWait(self.driver, time);


    def find_element(self, *loc):
        return self.driver.find_element(*loc)


    def open(self, url):
        full_url = self.base_url + url
        self.driver.get(full_url);
        self.driver.implicitly_wait(20)

    def open_current_url(self, current_url):
        self.driver.get(current_url);
        self.driver.implicitly_wait(20)


    def get_title(self):
        """Returns the page title"""
        return self.driver.title