import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AddmenberPage:
    def add_member(self):
        username = "aaaa"
        account = "aaa_dhx"
        phonenum = "13957869385"
        self.driver.find_element(By.id, "username").send_keys(username)
        self.driver.find_element(By.id, "memberAdd_acctid").send_keys(account)
        self.driver.find_element(By.id, "memberAdd_phone").send_keys(phonenum)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        return True

    def get_menber(self):
        self.driver.find_element(By.CSS_SELECTOR, " ")
