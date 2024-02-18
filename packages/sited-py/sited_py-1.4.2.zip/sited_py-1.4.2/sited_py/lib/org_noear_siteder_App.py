# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-04-28
LastEditors:Do not edit
LastEditTime:2020-10-06
Description:
"""
from .org_noear_siteder_dao_engine_DdApi import DdApi
from .org_noear_siteder_dao_engine_DdAdapter import DdAdapter


class App:
    def onCreate(self):
        App.mCurrent = self
        DdApi.tryInit(DdAdapter())

    @classmethod
    def getCurrent(cls):
        return App.mCurrent


App.mCurrent = None
