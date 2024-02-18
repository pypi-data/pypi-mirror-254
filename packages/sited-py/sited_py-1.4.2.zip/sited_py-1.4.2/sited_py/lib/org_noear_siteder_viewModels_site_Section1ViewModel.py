# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-10-05
LastEditors:Do not edit
LastEditTime:2021-03-04
Description:
"""
from .org_noear_siteder_dao_engine_sdVewModel_PictureSdViewModel import (
    PictureSdViewModel,
)
from .org_noear_siteder_utils_StateTag import StateTag
from .org_noear_siteder_models_SectionModel import SectionModel


class Section1ViewModel(PictureSdViewModel):
    def __init__(self):
        super().__init__()
        self.newItems = []  # 新增项#用于记录当前加载新项的项目
        self.currentIndex = 0
        self.isSectionsAsc = False
        self.currentSection = None
        self.fromSection = None

    def invertedIndex(self, index):
        return self.total() - 1 - index

    def invertedItem(self, index):
        return self.get(self.invertedIndex(index))

    # @Override
    def clear(self):
        self.items = []
        self.newItems = []

    def isNext(self):
        if (
            self.fromSection != None
            and self.fromSection.orgIndex > self.currentSection.orgIndex
        ):
            # 现在比之前的后面些
            # py版注：但我觉得是之前比现在的后面些
            val = True
        else:
            val = False

        if self.isSectionsAsc:
            return not val
        else:
            return val

    def isPrve(self):
        if (
            self.fromSection != None
            and self.fromSection.orgIndex < self.currentSection.orgIndex
        ):
            # 现在比之前的后面些
            val = True
        else:
            val = False
        if self.isSectionsAsc:
            return not val
        else:
            return val

    # @Override
    def loadByJson(self, config, *jsons):
        # java版: (String... jsons) 表示可变长度参数列表，参数为0到多个String类型的对象，或者是一个String[]。

        if jsons == None or jsons.__len__() == 0:
            return
        # py版: (*jsons) 表示可变参数组成的元组，要type(jsons[0])==list识别java版的多个String或者一个String[]
        if jsons.__len__() == 1 and type(jsons[0]) == list:
            jsons = jsons[0]

        if self.currentSection.total == 0:
            # 阅读时
            self.newItems = []
            state = StateTag()
            state.isOk = self.isPrve()  # isOk = isBef

            for json in jsons:
                self.loadByJsonData(config, json, state)

            self.currentSection.total = state.value

            if state.isOk:
                # 重新算位置 //isOk = isBef
                self.currentIndex = state.value  # 保持原位

    # @Override
    def doAddItem(self, pic, state):
        if state.isOk:
            # isOk = isBef
            self.items.insert(state.value, pic)
        else:
            self.items.append(pic)

        self.newItems.append(pic)

    # @Override
    def section(self):
        return self.currentSection

    def addItems(self, items):
        self.items.extend(items)
