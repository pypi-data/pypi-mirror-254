# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-06-11
LastEditors:Do not edit
LastEditTime:2020-08-06
Description:
"""
from .org_noear_siteder_models_ModelBase import ModelBase
from .me_noear_utils_EncryptUtil import EncryptUtil
from .org_noear_siteder_dao_db_DbApi import DbApi


class BookNode(ModelBase):
    def __init__(self, *arguments):
        super().__init__()
        self.name = None
        self.url = None
        self.logo = None
        self.author = ""
        self._bKey = None
        self._bID = 0
        self._cfg = None
        self._obj = None
        self._cover = None
        len = arguments.__len__()
        if len == 0:
            pass
        elif len == 1:
            url = arguments[0]
            self.url = url

    # -----------
    def bID(self):
        self.tryInitBookNode()
        return self._bID

    def bKey(self):
        self.tryInitBookNode()
        return self._bKey

    def tryInitBookNode(self):
        if self._bID == 0 and self.url != None:
            self._bKey = EncryptUtil.md5(self.url)
            DbApi.logBID("", self._bKey, self.url)
            self._bID = DbApi.getBID(self._bKey)

    # ----------
    def cfg(self, source):
        if self._cfg == None:
            self._cfg = source.book(self.url)
        return self._cfg

    def obj(self, source):
        if self._obj == None:
            self._obj = source.objectExt(self.url)
        return self._obj

    def cover(self, source):
        if self._cover == None and source != None:
            self._cover = source.cover(self.url)
        return self._cover

    def dtype(self, source):
        return self.cfg(source).dtype()

    def webUrl(self, source):
        if source == None:
            return self.url
        else:
            return self.cfg(source).getWebUrl(self.url)
