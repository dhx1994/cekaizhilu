from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from selenium.webdriver.common.by import By

from utils import BaseApi


class TestOptions():
    def setup_method(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()

    def test_demo(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.maximize_window()
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False,
             'value': ''},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853100945496'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853100945496'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '2685129182540853'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'rP2guBjWOU61CgzS5pYJ6S_1xuAA3gqP6RvgTmhjhfTHvA0G8UbZ41CYM8XBZkYL'},
            {'domain': '.qq.com', 'expiry': 1619338421, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.437330544.1619248143'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1619279677, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '3dcl3ss'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1646486847, 'httpOnly': False,
             'name': 'Hm_lvt_f2ba645ba13636ba52b0234381f51cbc', 'path': '/', 'secure': False, 'value': '1614950824'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 1638193183, 'httpOnly': False, 'name': 'Qs_pv_323937', 'path': '/',
             'secure': False,
             'value': '695391787282526600%2C1436511069142055400%2C3187531076268931600%2C4559509243911388000%2C3585615014028553000'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': 'e1dac2de072826cdbe502d5b6b896e01f9bdfca2dcf53f3e42cf16c7d59117fd'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1630718847, 'httpOnly': False, 'name': '__utmz', 'path': '/',
             'secure': False, 'value': '135912439.1614950824.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'},
            {'domain': '.qq.com', 'expiry': 1638193183, 'httpOnly': False, 'name': 'Qs_lvt_323937', 'path': '/',
             'secure': False, 'value': '1604409716%2C1606226959%2C1606227107%2C1606657146%2C1606657183'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1621844127, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 1682324021, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.765905365.1603605039'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1635140949, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': True, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '1075866886'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325040172423'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': True, 'value': '175596544'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'ZqGq_DBiZyVdL30NUHQpEV8iCZ33EiVTOesmBxx0ad_QqTV8J18exPGN7pvLCvExMZ7Xdq5MWPF8NMUVdSCv9rK0keeWVy65Kr461zVQuOOQsyVwmT8llJRnTIbBB_uRf86BfzskqZB2v7adTQBkVDE0Hh0auMXhtoFYelq3RCTM8aeU2HAnz37ujWctaUIdOqCD-jYARFCOBD-8Kp67wpjrRB0R-f7I8lezjxuMPc5JCJZ-5Y62PkAmA0mQi8O6keo8L-i3g2pCzM1ryj1mHw'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1650788021, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
             'value': '1618318919,1618493109,1619078274,1619248142'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1619252022'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1678022847, 'httpOnly': False, 'name': '__utma', 'path': '/',
             'secure': False, 'value': '135912439.765905365.1603605039.1614950824.1614950824.1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a8755104'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True,
             'value': 'TPAFTjA5sy'}]
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()


if __name__ == "__main__":
    pytest.main('-ws', 'test_zhuakuang.py')
