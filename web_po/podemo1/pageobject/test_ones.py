from web_po.podemo1.pageobject.mainpage import MainOfPage


class TestWx:
    def setup(self):
        self.main = MainOfPage()

    def test_register(self):
        assert self.index.register().register()

    def test_wx(self):
        gotoaddmenber = self.main.goto_addmenber()
        print(gotoaddmenber)
