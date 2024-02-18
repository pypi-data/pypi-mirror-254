# -*- coding: UTF-8 -*-
"""
Author:wistn
since:Do not edit
LastEditors:Do not edit
LastEditTime:2020-08-06
Description:
"""
from .org_noear_siteder_dao_SourceApi import SourceApi
from .org_noear_siteder_dao_engine_sdVewModel_SearchSdViewModel import SearchSdViewModel
from .mytool import TextUtils


class SearchViewModelBase(SearchSdViewModel):
    def __init__(self):
        super().__init__()
        self.isOnlyFavs = False
        self.isFilter = False
        self.searchKey = None
        self.searchFavsCount = 0

    # @Override
    def doFilter(self, name):
        if self.isFilter:
            if SourceApi.isFilter(name):
                return True

        return False

    # @Override
    def doAddItem(self, b):
        if TextUtils.isEmpty(self.searchKey) == False:
            if (
                b.name.__len__() <= self.searchKey.__len__() * 3
                and b.name.lower().find(self.searchKey) >= 0
            ):
                self.insertItem(b)
                return
        self.addItem(b)

    def addItem(self, b):
        pass

    def insertItem(self, b):
        pass

