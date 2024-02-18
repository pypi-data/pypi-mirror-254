# -*- coding: UTF-8 -*-
"""
Author:wistn
since:Do not edit
LastEditors:Do not edit
LastEditTime:2020-08-06
Description:
"""
from .org_noear_siteder_viewModels_site_SearchViewModelBase import SearchViewModelBase
from .org_noear_siteder_dao_db_DbApi import DbApi


class SearchViewModel(SearchViewModelBase):
    def __init__(self):
        super().__init__()
        self.isSearchMore = False
        self.currentPage = 1
        self.list = []

    # @Override
    def clear(self):
        self.list = []
        self.currentPage = 1
        self.searchFavsCount = 0

    # @Override
    def total(self):
        return self.list.__len__()

    # @Override
    def insertItem(self, b):
        b.isFromFavs = DbApi.isFaved(b)
        self.list.insert(self.searchFavsCount, b)
        self.searchFavsCount += 1
        if b.isFromFavs:
            b.updateTime = "[已收藏]"

    # @Override
    def addItem(self, b):
        b.isFromFavs = DbApi.isFaved(b)
        if b.isFromFavs:
            b.updateTime = "[已收藏]"
            self.list.insert(self.searchFavsCount, b)
            self.searchFavsCount += 1
        else:
            self.list.append(b)

