from resquests.utils.base_api import BaseApi


class ManageMenber(BaseApi):
    def read_menber(self):
        data = {"url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
                "method": "get",
                "params": {"access_token", self.token,
                           "userid", ""
                           },
                "json": {}

                }
        return self.send(data)

    def create_menber(self):
        data = {"url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
                "method": "post",
                "params": {"access_token": self.token},
                "json": {
                    "userid": "zhangsan",
                    "name": "张三",
                    "alias": "jackzhang",
                    "mobile": "+86 13800000000",
                    "department": [1, 2],
                    "order": [10, 40],
                    "position": "产品经理",
                    "gender": "1",
                    "email": "zhangsan@gzdev.com",
                    "is_leader_in_dept": [1, 0],
                    "enable": 1,
                    "avatar_mediaid": "2-G6nrLmr5EC3MNb_-zL1dDdzkd0p7cNliYu9V5w7o8K0",
                    "telephone": "020-123456",
                    "address": "广州市海珠区新港中路",
                    "main_department": 1,
                    "extattr": {
                        "attrs": [
                            {
                                "type": 0,
                                "name": "文本名称",
                                "text": {
                                    "value": "文本"
                                }
                            },
                            {
                                "type": 1,
                                "name": "网页名称",
                                "web": {
                                    "url": "http://www.test.com",
                                    "title": "标题"
                                }
                            }
                        ]
                    },
                    "to_invite": True,
                    "external_position": "高级产品经理",
                    "external_profile": {
                        "external_corp_name": "企业简称",
                        "external_attr": [
                            {
                                "type": 0,
                                "name": "文本名称",
                                "text": {
                                    "value": "文本"
                                }
                            },
                            {
                                "type": 1,
                                "name": "网页名称",
                                "web": {
                                    "url": "http://www.test.com",
                                    "title": "标题"
                                }
                            },
                            {
                                "type": 2,
                                "name": "测试app",
                                "miniprogram": {
                                    "appid": "wx8bd8012614784fake",
                                    "pagepath": "/index",
                                    "title": "my miniprogram"
                                }
                            }
                        ]
                    }
                }}
        return self.send(data)
