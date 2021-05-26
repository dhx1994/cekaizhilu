import json

import requests
from resquests.utils.base_api import BaseApi


class TestNew():
    def setup_class(self):
        self.baseapi = BaseApi()

    def test_tag_list(self):
        r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
                          params={
                              'access_token': self.baseapi.token},
                          json={'tag_id': []})
        assert r.status_code == 200
        print(json.dumps(r.json(), indent=4))

    def test_new_tag(self):
        r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
                          params={'access_token': self.baseapi.token},
                          json={
                              "group_id": "",
                              "group_name": "",
                              "order": 1,
                              "tag": [{
                                  "name": "标签2",
                                  "order": 1
                              },
                                  {
                                      "name": "标签2",
                                      "order": 2
                                  }
                              ],
                              "agentid": 1000014})
        #        print(r.json())
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
