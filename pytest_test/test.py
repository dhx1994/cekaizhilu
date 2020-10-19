import pytest
from selenium import webdriver


class Test_login():
    def test_login(self):
        driver = webdriver.chrome()
        driver.get("https://ceshiren.com/")
        #    driver.

    def test_ass(self):
        print("第一个测试用例")
        assert 1 == 1
