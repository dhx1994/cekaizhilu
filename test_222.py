from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestTestdemo():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

    def test_own_cookies(self):
        cookies = self.driver.get_cookies()
        print(cookies)

    def test_options(self):
        # all_handle = self.driver.window_handles
        # if self.driver.current_window_handle != 'CDwindow-4A0CC3A6ED7832EAAF3C2D20CD463003':
        #     self.driver.switch_to.window('CDwindow-4A0CC3A6ED7832EAAF3C2D20CD463003')
        # print(self.driver.title)
        self.driver.find_element_by_css_selector(
            ".index_service_cnt_itemWrap:nth-child(2) .index_service_cnt_item_title").click()
        sleep(5)
        self.driver.find_element_by_css_selector("#js_upload_file_input").send_keys(
            r"C:\Users\Administrator\Desktop\平安项目\附件4：平安科技复工安排表(3).xlsx")
        filename = self.driver.find_element_by_css_selector("#upload_file_name").text
        print(filename)
        assert filename == "附件4：平安科技复工安排表(3).xlsx"


if __name__ == "__main__":
    pytest.main("-vs", "test_222.py")
