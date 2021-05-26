import requests

from resquests.utils.base_api import BaseApi


class Test(BaseApi):
    def test_get_token(self):
        corpid = 'wwab334528fc1fbf03'
        corpsecret = 'b9WEltef2fW2dwHSffXMzyIiRJd0qqUpHnEt921PFz0'
        r = requests.get(url='https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                         params={'corpid': corpid,
                                 'corpsecret': corpsecret
                                 }
                         )
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

        print(r.json()['access_token'])
