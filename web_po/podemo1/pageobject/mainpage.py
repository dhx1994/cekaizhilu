import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from web_po.podemo1.pageobject.addmenber import AddmenberPage


class MainOfPage:
    def __init__(self):
        options = Options()
        options.debugger_address("127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=options)

    def goto_addmenber(self):
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)")
        return AddmenberPage(self.driver)
