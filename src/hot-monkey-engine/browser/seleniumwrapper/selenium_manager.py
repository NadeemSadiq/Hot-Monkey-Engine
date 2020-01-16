from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SeleniumCreate:
    def __init__(self):
        pass

    def create_driver(self):
        return webdriver.Chrome()