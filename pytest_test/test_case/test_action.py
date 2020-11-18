from selenium import webdriver
from selenium.webdriver import ActionChains
import pytest, time


class TestAction():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_action(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        elment_click = self.driver.find_element_by_xpath('//input[@value="click me"]')
        elment_dbl_click = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        elment_right_click = self.driver.find_element_by_xpath('//input[@value="right click me"]')
        action = ActionChains(self.driver)
        # 点击
        action.click(elment_click)
        # 双击
        action.double_click(elment_dbl_click)
        # 鼠标右击
        action.context_click(elment_right_click)
        action.perform()

    def test_move_to(self):
        self.driver.get("https://www.baidu.com/")
        elment_move_to = self.driver.find_element_by_id('s-usersetting-top')
        action = ActionChains(self.driver)
        action.move_to_element(elment_move_to)
        time.sleep(3)
        action.perform()


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_action.py"])
