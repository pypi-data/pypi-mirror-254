# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-06-05
LastEditors:Do not edit
LastEditTime:2020-10-06
Description:
"""


class Session:
    @classmethod
    def trySetAlias(cls):
        pass

    @classmethod
    def clear(cls):
        Session.userID = 0
        Session.nickname = ""
        Session.icon = ""
        Session.sign = ""
        Session.city = ""
        Session.level = 0
        Session.sex = 0
        Session.isVip = 0
        Session.dayNum = 0
        Session.vipTimeout = ""
        Session.save()
        Session.isAccountChange = True

    @classmethod
    def save(cls):
        pass

    #
    # ------------------
    #
    @classmethod
    def udid(cls):
        return Session._uuid


Session.userID = 0
Session.nickname = ""
Session.icon = ""
Session.sex = 0
Session.isVip = 0
Session.level = 0
Session.city = ""
Session.sign = ""
Session.dayNum = 0
Session.vipTimeout = ""
Session.userInfoGetCount = 0
Session.isAccountChange = False
if Session.userID > 0:
    Session.trySetAlias()

Session._uuid = None
