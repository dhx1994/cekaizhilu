import random

from resquests.utils.base_api import BaseApi


class ManageMenber(BaseApi):
    def read_menber(self):
        data = {"url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
                "method": "get",
                "params": {"access_token": self.token,
                           "userid": "DuHengXin"
                           }

                }
        return self.send(data)

    def create_menber(self, userid):
        self.moblie = "139" + ''.join(random.sample("1234567890", 8))
        data = {"url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
                "method": "post",
                "params": {"access_token": self.token},
                "json": {
                    "userid": userid,
                    "name": "张三",
                    "department": [1],
                    "mobile": "+86 " + self.moblie

                }}
        return self.send(data)

    def update_menber(self):
        r = self.read_menber()
        gender = "1"
        if r.json()["gender"] == "1":
            gender = "2"
        data = {"url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
                "method": "post",
                "params": {"access_token": self.token},
                "json": {
                    "userid": "duhengxin",
                    "gender": gender,
                }}
        return self.send(data)

    def delete_menber(self):
        go_menber = []
        result = self.get_department_menber()
        menberlist = result.json()["userlist"]
        for i in menberlist:
            go_menber.append(menberlist["userid"])
        if "fsfsdfs" in go_menber:
            pass
        else:
            self.create_menber("fsfsdfs")
        data = {"url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
                "method": "get",
                "params": {"access_token": self.token,
                           "userid": "fsfsdfs"},
                "json": {}

                }
        return self.send(data)

    def get_department_menber(self):
        data = {"url": "https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
                "method": "post",
                "params": {"access_token": self.token,
                           "userid": "duhengxin"},
                "json": {}}
        return self.send(data)
