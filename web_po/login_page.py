from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web_po.register_page import RegisterPage


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def scan(self):
        pass

    def register(self):
        self.driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return RegisterPage()
