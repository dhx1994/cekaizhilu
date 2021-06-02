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
        r = self.menber.create_menber()
        assert r.json()["errcode"] == 0
        assert r.json()["errmsg"] == "created"
        print(r.json())
