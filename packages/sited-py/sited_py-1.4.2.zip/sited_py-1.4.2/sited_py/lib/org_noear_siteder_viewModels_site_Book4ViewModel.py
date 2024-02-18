# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-10-05
LastEditors:Do not edit
LastEditTime:2021-03-04
Description:
"""
from .org_noear_siteder_dao_engine_DdSource import DdSource
from .mytool import TextUtils
from .org_noear_siteder_models_PicModel import PicModel
from .org_noear_siteder_dao_engine_sdVewModel_PictureSdViewModel import (
    PictureSdViewModel,
)
from .org_noear_siteder_models_SectionModel import SectionModel
from .org_noear_siteder_viewModels_site_Section1ViewModel import Section1ViewModel
from .org_noear_siteder_utils_StateTag import StateTag
from .noear_snacks_ONode import ONode


class Book4ViewModel(PictureSdViewModel):
    def __init__(self, source, n):
        super().__init__()
        self.currentIndex = 0  # 加载时借用
        self._section = SectionModel()
        self._section.url = n.url
        self._section.name = "全部"
        self._section.bookUrl = n.url
        self._section.bookName = "全部"
        self.bookUrl = n.url
        self.node = n

    def toSectionViewModel(self):
        vm = Section1ViewModel()
        vm.currentIndex = 0
        vm.currentSection = self._section
        vm.addItems(self.items)
        return vm

    # @Override
    def loadByJson(self, config, *jsons):
        # java版: (String... jsons) 表示可变长度参数列表，参数为0到多个String类型的对象，或者是一个String[]。
        if jsons == None or jsons.__len__() == 0:
            return
        # py版: (*jsons) 表示可变参数组成的元组，要type(jsons[0])==list识别java版的多个String或者一个String[]
        if jsons.__len__() == 1 and type(jsons[0]) == list:
            jsons = jsons[0]
        for json in jsons:
            if json.find("sections") > 0 or json.find("intro") > 0:
                self.loadByJsonForOld(config, json)
            else:
                state = StateTag()
                self.loadByJsonData(config, json, state)
        # ---------
        if TextUtils.isEmpty(self.logo) == False:
            self.node.logo = self.logo
        else:
            self.logo = self.node.logo
        if TextUtils.isEmpty(self.name) == False:
            self.node.name = self.name

    # @Override
    def doAddItem(self, pic, state):
        self.items.append(pic)

    # @Override
    def section(self):
        return self._section

    def loadByJsonForOld(self, config, json):
        data = ONode.tryLoad(json)
        if DdSource.isBook(config) and TextUtils.isEmpty(self.name):
            self.name = data.get("name").getString()
            self.logo = data.get("logo").getString()
        sl = data.get("sections").asArray()
        for n in sl:
            pic = PicModel(
                self.section(), n.get("url").getString(), 0, self.items.__len__()
            )
            self.items.append(pic)
