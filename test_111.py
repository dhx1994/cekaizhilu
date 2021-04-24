from selenium.webdriver.common.by import By

from utils import BaseApi


class TestWish():
    def setup_method(self):
        self.baseapi = BaseApi()

    def test_one(self):
        self.baseapi.find_element((By.CSS_SELECTOR, ".promote_card_short:nth-child(2)")).click()
