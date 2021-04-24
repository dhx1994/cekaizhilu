from web_po.podemo.index_page import IndexPage


class TestWx:
    def setup(self):
        self.index = IndexPage()

    def teardown(self):
        self.driver.quit()

    def test_register(self):
        assert self.index.register().register()
