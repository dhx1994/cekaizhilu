from resquests.apiobject.tag import Tag


class TestApi:
    def setup_method(self):
        self.tag = Tag()

    def test_list(self):
        r = self.tag.list()
        assert r.status_code == 200
        print(r.json())

    def test_add(self):
        # name = "标签"+str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        tag = [
            {'name': '标签1'},
            {'name': '标签2'},
        ]
        group_name = 'TMP00123'
        r = self.tag.add_defect(group_name, tag)
        print(r)
        assert r

    def test_delete(self):
        r = self.tag.delete_defect(['1223'])
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    def test_update(self):
        id = 'daf'
        name = '标签'
        r = self.tag.update_defect(id, name)
        assert r
