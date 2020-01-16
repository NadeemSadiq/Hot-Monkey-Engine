class SeleniumAdapter:
    page = None

    def __init__(self, **kwargs):
        if len(kwargs) is 0:
            raise TypeError

    def goto(self, url):
        pass
