from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def test_register(self):
        self.driver.find_element(By.ID, "corp_name").send_keys("test")
        self.driver.find_element(By.ID, "manager_name").send_keys("job")
        self.driver.find_element(By.ID, "submit_btn").click()
