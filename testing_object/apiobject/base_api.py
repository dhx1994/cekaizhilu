# 基本类
import requests
import yaml


class BaseApi():
    def __init__(self):
        self.token = self.get_token().json()["data"][0]["token"]
        with open("../data/data.yml", encoding="utf-8") as f:
            self.data1 = yaml.safe_load(f.read())
        self.url = self.data1["env"]["test"]
        self.api = self.data1["data"]

    def get_token(self):
        r = requests.post(url="http://118.24.255.132:8088/manage/systemAccount/login",
                          json={
                              "account": "admin",
                              "password": "123456"
                          })
        r.status_code == 200
        r.json()["code"] == "0"
        return r

    def send(self, data):
        r = requests.request(**data)
        return r
