import pytest
import yaml

from testing_object.apiobject.system_and_sass import SystemAccountController, SassVersionController


class TestAccount():
    def setup_method(self):
        self.account = SystemAccountController()
        self.sass = SassVersionController()

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
        r = self.sass.version_sassListVersion()
        print(r.text)
