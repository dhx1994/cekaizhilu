import pytest
import yaml

from testing_object.apiobject.system_and_sass import SassNoiceController
from testing_object.apiobject.system_and_sass import SassVersionController
from testing_object.apiobject.system_and_sass import SystemAccountController


class TestAccount():
    def setup_class(self):
        self.account = SystemAccountController()
        self.sassversion = SassVersionController()
        self.sassnotice = SassNoiceController()

    def test_get_messagecode(self):
        r = self.account.get_message_code()
        assert r.status_code == 200
        assert r.json()["code"] == 0

    def test_logout(self):
        r = self.account.log_out()
        assert r.status_code == 200
        assert r.json()["code"] == 1

    @pytest.mark.parametrize("account", yaml.safe_load(open("../data/data.yml", encoding="UTF-8"))["data"][
        "/manage/systemAccount/login"]["account"])
    @pytest.mark.parametrize("password", yaml.safe_load(open("../data/data.yml", encoding="UTF-8"))["data"][
        "/manage/systemAccount/login"]["password"])
    def test_log_in(self, account, password):
        r = self.account.log_in(account, password)
        assert r.status_code == 200
        if account == "admin" and password == "123456":
            assert r.json()["code"] == 1
            assert r.json()["msg"] == "登录成功"
        else:
            assert r.json()["code"] == 0
            assert r.json()["msg"] == "账号密码不匹配或已被禁用，"

    def test_version_sassListVersion(self):
        r = self.sassversion.version_sassListVersion()
        r.status_code == 200
        r.json()["code"] == 1

    def test_version_updateVersionStatus(self):
        r = self.sassversion.version_updateVersionStatus()
        r.status_code == 200
        r.json()["code"] == 1

    def test_version_createNewVersion(self):
        r = self.sassversion.version_createNewVersion()
        r.status_code == 200
        r.json()["code"] == 1

    def test_notice_sassListNoice(self):
        r = self.sassnotice.notice_sassListNoice()
        r.status_code == 200
        r.json()["code"] == 1

    def test_notice_sassListNoice(self):
        r = self.sassnotice.notice_updateNoticeStatus()
        r.status_code == 200
        r.json()["code"] == 1
