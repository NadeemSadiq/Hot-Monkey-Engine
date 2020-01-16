import unittest
from hot_monkey_engine.browser.seleniumwrapper.selenium_adapter import * 


valid_url = 'https://somewebsite.com'
test_page = "Some webpage or something"

class SeleniumMock():
    def get(self, url):
        return test_page

class SeleniumRaiseErrorMock():
    def get(self, url):
        raise OSError

selenium_mock = SeleniumMock()
selenium_error_mock = SeleniumRaiseErrorMock()

class TestBrowserFunction(unittest.TestCase):
    def test_goto_website(self):
        adapter = SeleniumAdapter(selenium_mock)
        
        adapter.goto(valid_url)

        self.assertEqual(adapter.page, test_page)
    
    def test_error_when_selenium_raises_error(self):
        with self.assertRaises(BrowserError):
            adapter = SeleniumAdapter(selenium_error_mock)
        
            adapter.goto(valid_url)

    def test_type_to_page(self):
        adapter = SeleniumAdapter(selenium_error_mock)
        
        adapter.type(valid_url)

    def test_type_with_non_character_key_commands_to_page(self):
        adapter = SeleniumAdapter(selenium_error_mock)
        
        adapter.press(Key.ENTER)
        adapter.press(Key.ESC)
        adapter.press(Key.TAB)
        adapter.press(Key.ENTER, Key.CTRL)




    
