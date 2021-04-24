from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


# def find_element(driver,locator):
#     """
#         查找单个元素
#             参数：locator=("id", "123")
#             类型：w
#             ID = "id"
#             XPATH = "xpath"
#             LINK_TEXT = "link text"
#             PARTIAL_LINK_TEXT = "partial link text"
#             NAME = "name"
#             TAG_NAME = "tag name"
#             CLASS_NAME = "class name"
#             CSS_SELECTOR = "css selector"
#     """
#     element = WebDriverWait(driver, 10).until(lambda s: s.find_element(*locator))  # 实现元素的动态定位
#     return element
# def is_element_exist(driver,locator):
#     try:
#         WebDriverWait(driver, 10).until(lambda s: s.find_element(*locator))  # 实现元素的动态定位
#         return True
#     except:
#         return False

class BaseApi():
    def __init__(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

    # self.driver.get("https://work.weixin.qq.com/api/doc")
    def find_element(self, locater):
        element: WebElement = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locater))
        return element
