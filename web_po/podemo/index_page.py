from selenium import webdriver
from selenium.webdriver.common.by import By

from web_po.podemo.login_page import LoginPage
from web_po.podemo.register_page import RegisterPage


class IndexPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    def sign_in(self):
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return LoginPage(self.driver)

    def register(self):
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return RegisterPage(self.driver)
