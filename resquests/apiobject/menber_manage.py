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

    def create_menber(self):
        self.userid = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 10))
        self.moblie = "139" + ''.join(random.sample("1234567890", 8))

        print(self.userid, self.moblie)
        data = {"url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
                "method": "post",
                "params": {"access_token": self.token},
                "json": {
                    "userid": self.userid,
                    "name": "张三",
                    "department": [1],
                    "mobile": "+86 " + self.moblie

                }}
        return self.send(data)
