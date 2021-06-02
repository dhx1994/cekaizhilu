from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from web_po.podemo.po.login_page import LoginPage
from web_po.podemo.po.register_page import RegisterPage


class IndexPage:
    def __init__(self):
        options = Options()
        options.debugger_address("127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=options)

    def sign_in(self):
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return LoginPage(self.driver)

    def register(self):
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return RegisterPage(self.driver)
