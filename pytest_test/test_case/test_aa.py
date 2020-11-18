from selenium import webdriver
import pytest


class Testcass():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")

    def teardown(self):
        self.driver.quit()

    def test_click(self):
        self.driver.find_element_by_xpath()
