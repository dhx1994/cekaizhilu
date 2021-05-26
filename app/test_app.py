from appium import webdriver
from appium.webdriver import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Testcase():
    def setup_class(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".common.MainActivity"
        # noReset 保留缓存， 比如登录状态
        caps["noReset"] = "True"
        # 不停止应用，直接运行测试用例
        caps["dontStopAppOnReset"] = "True"
        caps['skipDeviceInitialization'] = 'True'
        caps['skipServerInstallation'] = 'True'
        caps["automationName"] = "UiAutomator1"
        # caps["settings[waitForIdleTimeout]"] = 0
        # 关键  localhost:4723  本机ip:server端口
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    def ec(self, locater):
        element: WebElement = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locater))
        return element

    def test_login(self):
        self.ec(("xpath",
                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[4]/android.widget.ImageView")).click()
