import datetime

from resquests.base_api import BaseApi


class Tag(BaseApi):
    def find_group_id_by_name(self, group_name):
        for group in self.list().json()['tag_group']:
            if group_name in group['group_name']:
                return group["group_id"]
        print("group not in groups")
        return ""

    def is_group_id_exist(self, group_id):
        for group in self.list().json()['tag_group']:
            if group_id in group['group_id']:
                return group['group_id']
        print('不存在该标签')
        return False

    def delete_tag(self, tag_id):
        data = {'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
                'method': 'post',
                'params': {"access_token": self.token},
                'json': {'tag_id': tag_id,
                         }

                }
        return self.send(data)

    def delete_group(self, group_id):
        data = {'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
                'method': 'post',
                'params': {"access_token": self.token},
                'json': {'group_id': group_id
                         }

                }
        return self.send(data)

    def list(self):
        data = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            'method': 'post',
            'params': {"access_token": self.token},
            'json': {'tag_id': []}

        }
        return self.send(data)

    def add(self, group_name, name):
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            'params': {"access_token": self.token},
            'json': {'group_name': group_name, 'tag': name
                     }
        }
        return self.send(data)

    def add_defect(self, group_name, tag):
        r = self.add(group_name, tag)
        if r.json()['errcode'] == 40071:
            group_id = self.find_group_id_by_name(group_name)
            if not group_id:
                # 接口错误
                return ''
            self.delete_group([group_id])
            self.add(group_name, tag)
        result = self.find_group_id_by_name(group_name)
        if not result:
            print("接口错误")
        return result

    def delete_defect(self, group_ids):
        group_idss = []
        r = self.delete_group(group_ids)
        if r.json()['errcode'] == 40068:
            for group_id in group_ids:
                if not self.is_group_id_exist(group_id):
                    group_ids_tmp = self.add_defect(group_name='TMP00123', tag=
                    [{'name': '标签1'}])
                    group_idss.append(group_ids_tmp)
                else:
                    group_idss.append(group_id)
            r = self.delete_group(group_idss)
        return r

    def update(self, id, name):
        data = {'url': 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
                'method': 'post',
                'params': {"access_token": self.token},
                'json': {'id': id,
                         'name': name}

                }
        return self.send(data)

    def update_defect(self, id, name):

        r = self.add_defect(group_name='TMP00123', tag=
        [{'name': '标签1'}])

        return r
