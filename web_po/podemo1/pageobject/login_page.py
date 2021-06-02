from selenium.webdriver.common.by import By

from web_po.podemo.po.register_page import RegisterPage


class LoginPage:
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    def scan(self):
        pass

    def go_to_register(self):
        self.driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return RegisterPage()
