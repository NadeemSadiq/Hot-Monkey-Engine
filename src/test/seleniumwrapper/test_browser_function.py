import unittest
from hot_monkey_engine.browser.seleniumwrapper.selenium_adapter import SeleniumAdapter 

default_config = {
    'driver' : 'chrome',
    'location' : "/path/to/driver",
}

valid_url = 'https://somewebsite.com'
test_page = "Some webpage or something"

class TestBrowserFunction(unittest.TestCase):

    def test_create_new_browser_with_config(self):
        adapter = SeleniumAdapter(**default_config)
        
        self.assertIsNotNone(adapter, 'An error with creating an adapter')

    def test_errors_when_missing_config(self):
        with self.assertRaises(TypeError):
            SeleniumAdapter()

    def test_wrong_driver_setup(self):
        with self.assertRaises(TypeError):
            SeleniumAdapter(driver='doesnotexist', location='/does/not/exist')

    def test_goto_website(self):
        adapter = SeleniumAdapter(**default_config)
        
        adapter.goto(valid_url)

        self.assertEqual(adapter.page, test_page)



    
