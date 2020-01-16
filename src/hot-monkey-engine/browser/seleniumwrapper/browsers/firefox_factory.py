from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FireFoxDriverFactory:
    def __init__(self):
        pass

    def create_driver(self):
        return webdriver.Firefox()