# 账号管理

from testing_object.apiobject.base_api import BaseApi


class SystemAccountController(BaseApi):
    # 账号管理
    def get_message_code(self):
    # 获取验证码
        phone = self.api["/manage/systemAccount/getVerificationCode"]["phone"]
        data = {"url": self.url + "/manage/systemAccount/getVerificationCode/" + str(phone),
                "method": "post",
                "params": {}
                }
        r = self.send(data)
        return r

    def log_out(self):
        # 退出登陆
        re_userid = self.get_token()
        userid = re_userid.json()["data"][0]["userId"]
        data = {"url": self.url + "/manage/systemAccount/logout/" + str(userid),
                "method": "post",
                "params": {}

                }
        r = self.send(data)
        return r

    def log_in(self, account, password):
        #登陆
        data = {"url": self.url + "/manage/systemAccount/login",
                "method": "post",
                "json": {"account": account,
                         "password": password

                         }
                }
        r = self.send(data)
        return r


class SassVersionController(BaseApi):
    # 版本管理
    def version_sassListVersion(self):
        # 查询版本列表
        pagesize = self.api["/sass/version/sassListVersion"]["pagesize"]
        pagenum = self.api["/sass/version/sassListVersion"]["pagenum"]
        data = {"url": self.url + "/sass/version/sassListVersion/{pagesize}/{pagenum}".format(pagesize=pagesize,
                                                                                              pagenum=pagenum),
                "method": "post",
                "data": {"sassListTeamDTO": self.api["/sass/version/sassListVersion"]["sassListTeamDTO"]
                         }}
        r = self.send(data)
        return r

    def version_updateVersionStatus(self):
        # 更新版本状态
        versionid = self.api["/sass/version/updateVersionStatus"]["versionid"]
        status = self.api["/sass/version/updateVersionStatus"]["status"]
        data = {"url": self.url + "/sass/version/updateVersionStatus/{versionId}/{status}".format(versionId=versionid,
                                                                                                  status=status),
                "method": "post",
                "data": {}
                }
        r = self.send(data)
        return r

    def version_createNewVersion(self):
        # 新建版本
        data = {"url": self.url + "/sass/version/createNewVersion",
                "method": "post",
                "json": self.api["/sass/version/createNewVersion"]
                }
        r = self.send(data)
        return r


class SassNoiceController(BaseApi):
    # 公告管理
    def notice_sassListNoice(self):
        # 获取公告列表
        data = {"url": self.url + "/sass/notice/sassListNoice/{pageSize}/{pageNum}".format(
            pageSize=self.api["/sass/notice/sassListNoice"]["pagesize"],
            pageNum=self.api["/sass/notice/sassListNoice"]["pagenum"]),
                "method": "post",
                "json": {}}
        r = self.send(data)
        return r

    def notice_createNewNotice(self):
        data = {"url": self.url + "/sass/notice/createNewNotice",
                "method": "post",
                "json": {"createTeamDTO": ""}

                }
        return self.send(data)

    def notice_updateNoticeStatus(self):
        data = {"url": self.url + "/sass/notice/updateNoticeStatus/{NoticeId}/{isTrue}".format(
            NoticeId=self.api["/sass/notice/updateNoticeStatus"]["NoticeId"],
            isTrue=self.api["/sass/notice/updateNoticeStatus"]["isTrue"]),
                "method": "post",
                "json": {}
                }
        return self.send(data)
