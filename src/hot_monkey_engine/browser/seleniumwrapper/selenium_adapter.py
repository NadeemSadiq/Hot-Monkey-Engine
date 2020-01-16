class SeleniumAdapter:
    page = None

    def __init__(self, selenium):
        self.selenium = selenium

    def goto(self, url):
        try:
            self.page = self.selenium.get(url)
        except:
            raise BrowserError("Unable to goto page")

    def type(self, characters):
        pass

    def press(self, *args):
        pass


class BrowserError(Exception):
    pass

from enum import Enum

class Key(Enum):
    ENTER = 0
    SHIFT = 1
    CTRL = 2
    ESC = 3
    TAB = 4