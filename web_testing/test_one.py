import shelve
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestOne():
    def setup_method(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_one(self):
        self.driver.get("http://www.baidu.com")

    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        # print(cookies)
        db = shelve.open("cookies")
        cookies = db['cookie']
        db.close()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_uploadInputMask').send_keys(
            "C:/Users/Administrator/Desktop/平安项目/新入场外包员工信息核验登记表_更新.xlsx")
        filename = self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_fileNames').text
        assert filename == "新入场外包员工信息核验登记表_更新.xlsx"
