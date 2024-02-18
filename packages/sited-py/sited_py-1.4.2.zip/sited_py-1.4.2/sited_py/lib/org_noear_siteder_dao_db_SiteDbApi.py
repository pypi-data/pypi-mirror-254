# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-29
LastEditors:Do not edit
LastEditTime:2020-10-06
Description:
"""
from datetime import datetime
from .me_noear_db_DbContext import DbContext
from .me_noear_utils_EncryptUtil import EncryptUtil
from .android_util_Log import Log


class SiteDbApi:
    class SiteDbContext(DbContext):
        def __init__(self, context):
            super().__init__(context, "sitedb", 11)

    @classmethod
    def setSourceCookies(cls, sd):
        pass

    @classmethod
    def setSourceUsetime(cls, sd):
        SiteDbApi.db.updateSQL(
            "UPDATE  sites SET logTime=? WHERE key=? ",
            datetime.now().timestamp(),
            sd.url_md5,
        )

    @classmethod
    def getSourceCookies(cls, sd):
        temp = cls.getSourceByKey(sd.url_md5)
        if temp == None:
            return None
        else:
            return temp.cookies

    @classmethod
    def getSourceByKey(cls, key):
        pass


SiteDbApi.db = None
if SiteDbApi.db == None:
    SiteDbApi.db = SiteDbApi.SiteDbContext("App.getContext()")
