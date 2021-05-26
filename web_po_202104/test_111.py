from web_po_202104.PageObject import IndexPage


class TestWish():
    def setup_method(self):
        self.indexpage = IndexPage()

    def test_one(self):
        self.indexpage.options()
