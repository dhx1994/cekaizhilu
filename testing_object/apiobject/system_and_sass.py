# 账号管理
import pytest

from testing_object.apiobject.base_api import BaseApi


class SystemAccountController(BaseApi):
    # 账号管理
    def get_message_code(self):
        phone = self.api["/manage/systemAccount/getVerificationCode"]["phone"]
        data = {"url": self.url + "/manage/systemAccount/getVerificationCode/" + str(phone),
                "method": "post",
                "params": {}
                }
        r = self.send(data)
        return r

    def log_out(self):
        re_userid = self.get_token()
        userid = re_userid.json()["data"][0]["userId"]
        data = {"url": self.url + "/manage/systemAccount/logout/" + str(userid),
                "method": "post",
                "params": {}

                }
        r = self.send(data)
        return r

    def log_in(self, account, password):
        data = {"url": self.url + "/manage/systemAccount/login",
                "method": "post",
                "json": {"account": account,
                         "password": password

                         }
                }
        r = self.send(data)
        return r


class SassVersionController(BaseApi):
    # 版本管理
    def version_sassListVersion(self):
        data = {"url": self.url + "/sass/version/sassListVersion/" + str(
            self.api["/sass/version/sassListVersion"]["pagesize"]) + "/" + str(
            self.api["/sass/version/sassListVersion"]["pagenum"]),
                "method": "post",
                "json": {"sassListTeamDTO": self.api["/sass/version/sassListVersion"]["sassListteamdto"]}
                }

        print(self.api["/sass/version/sassListVersion"]["sassListteamdto"])
        r = self.send(data)
        return r
