# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-09-23
LastEditors:Do not edit
LastEditTime:2020-10-06
Description:
"""
from .org_noear_siteder_dao_engine_sdVewModel_BookSdViewModel import BookSdViewModel
from .mytool import TextUtils

SettingBookisSortUp = 1


class BookViewModel(BookSdViewModel):
    def __init__(self, s, n):
        super().__init__(n.url)
        self._lastLookOrgIndex = -1
        self._lastLook = 0  # 根据url 生成 haskcode
        self.source = s
        self.node = n
        self.intro = ""
        self.isSortUp = False
        self.isDownding = False
        self.downList = None  # hashcodeList
        self._dtype = -1
        self._sectionDownList = []
        self._sectionUpList = []
        self.lastLookUrl = None
        self.lastLookUrlPage = None

    def sectionList(self):
        if self.dtype() < 4:
            self.isSortUp = SettingBookisSortUp
        return self.doSectionList()

    def dtype(self):
        if self._dtype < 0:
            self._dtype = self.node.dtype(self.source)
        return self._dtype

    def doSectionList(self):
        if self.isSortUp:
            return self._sectionUpList
        else:
            return self._sectionDownList

    def isDowned(self, item):
        hc = item.url.__hash__()
        for c in self.downList:
            if c == hc:
                return True
        return False

    # =============
    # @Override
    def clear(self):
        super().clear()
        self._sectionDownList = []
        self._sectionUpList = []

    def setLastLook(self, sectionUrl):
        if sectionUrl == None:
            return
        self.lastLookUrl = sectionUrl
        self._lastLook = sectionUrl.__hash__()
        idx = 0
        for sec in self._sectionDownList:
            if sec.code() == self._lastLook:
                self._lastLookOrgIndex = idx
                break
            idx += 1

    def lastLook(self):
        return self._lastLook

    def lastLookOrgIndex(self):
        return self._lastLookOrgIndex

    def lastLookIndex(self):
        if SettingBookisSortUp:
            return self.total() - 1 - self._lastLookOrgIndex
        else:
            return self._lastLookOrgIndex

    def sectionCount(self):
        return self.doSectionList().__len__()

    def getSectionByCode(self, code):
        for sec in self.doSectionList():
            if sec.code() == code:
                return sec
        return None

    def getSection(self, idx):
        len = self.sectionCount()
        if idx >= len or idx < 0:
            return None
        else:
            return self.doSectionList()[idx]

    # @Override
    def loadByJson(self, config, *jsons):
        super().loadByJson(config, *jsons)
        # -----------
        if TextUtils.isEmpty(self.logo) == False:
            self.node.logo = self.logo
        else:
            if TextUtils.isEmpty(self.logo):
                self.logo = self.node.logo
        if TextUtils.isEmpty(self.name) == False:
            self.node.name = self.name
        else:
            if TextUtils.isEmpty(self.name):
                self.name = self.node.name
        if TextUtils.isEmpty(self.author) == False:
            self.node.author = self.author

    # @Override
    def onAddItem(self, sec):
        sec.bookName = self.name
        sec.bookUrl = self.node.url
        sec.index = self.sectionCount()
        self._sectionDownList.append(sec)
        self._sectionUpList.insert(0, sec)

    def addItemByEx(self, sec):
        self.sections.append(sec)
        self.onAddItem(sec)

