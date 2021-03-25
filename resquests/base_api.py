import requests


class BaseApi:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = 'wwab334528fc1fbf03'
        corpsecret = 'CsWga3FxJopT_wcNQBbMXsE2h6PXPigv4nVw-YPvvAE'
        r = requests.get(url='https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                         params={'corpid': corpid,
                                 'corpsecret': corpsecret
                                 }
                         )
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        access_token = r.json()['access_token']
        return access_token

    def send(self, kwargs):
        r = requests.request(**kwargs)
        return r
