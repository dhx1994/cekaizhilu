from random import random

from resquests.apiobject.menber_manage import ManageMenber


class TestMenber():
    def setup_class(self):
        self.menber = ManageMenber()

    def test_menber_list(self):
        r = self.menber.read_menber()
        print(r.json())
        assert r.json()["errcode"] == 0
        assert r.json()["errmsg"] == "ok"
        assert r.json()["userid"] == "DuHengXin"

    def test_create_menber(self):
        userid = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 10))
        r = self.menber.create_menber(userid=userid)
        assert r.json()["errcode"] == 0
        assert r.json()["errmsg"] == "created"

    def test_update_menber(self):
        r = self.menber.update_menber()
        r.status_code == 0
        r.json()["errcode"] == 0
        r.json()["errmsg"] == "updated"

    def test_delete_menber(self):
        r = self.menber.delete_menber()
        r.status_code == 200
        r.json()["errcode"] == 0
        r.json()["errmsg"] == "deleted"

    def test_get_department_menber(self):
        r = self.menber.get_department_menber()
        r.status_code == 200
        r.json()["errcode"] == 0
        r.json()["errmsg"] == "ok"
