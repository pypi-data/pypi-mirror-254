# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-09-23
LastEditors:Do not edit
LastEditTime:2021-03-04
Description:
"""
from .org_noear_siteder_dao_engine_DdSource import DdSource
from .mytool import TextUtils
from .android_util_Log import Log
from .org_noear_siteder_viewModels_ViewModelBase import ViewModelBase
from .org_noear_siteder_models_SectionModel import SectionModel
from .noear_snacks_ONode import ONode


class BookSdViewModel(ViewModelBase):
    def __init__(self, url):
        super().__init__()
        self.sections = []
        self.name = None
        self.author = None
        self.intro = None
        self.logo = None
        self.updateTime = None
        self.isSectionsAsc = False  # 输出的section是不是顺排的
        self.bookUrl = url

    # @Override
    def loadByConfig(self, config):
        pass

    # @Override
    def loadByJson(self, config, *jsons):
        # java版: (String... jsons) 表示可变长度参数列表，参数为0到多个String类型的对象，或者是一个String[]。
        if jsons == None or jsons.__len__() == 0:
            return
        # py版: (*jsons) 表示可变参数组成的元组，要type(jsons[0])==list识别java版的多个String或者一个String[]
        if jsons.__len__() == 1 and type(jsons[0]) == list:
            jsons = jsons[0]
        for json in jsons:
            self.loadByJsonData(config, json)

    def loadByJsonData(self, config, json):
        data = ONode.tryLoad(json)
        # 注意：java版ViewModel都是自定义类ONode,JsonReader。对于输出须要有转义符的文本插件（比较小众）和py版json.loads有不同效果
        if DdSource.isBook(config):
            if TextUtils.isEmpty(self.name):
                self.name = data.get("name").getString()
                self.author = data.get("author").getString()
                self.intro = data.get("intro").getString()
                self.logo = data.get("logo").getString()
                self.updateTime = data.get("updateTime").getString()
                self.isSectionsAsc = data.get("isSectionsAsc").getInt() > 0
                # 默认为倒排
        sl = data.get("sections").asArray()
        for n in sl:
            sec = SectionModel()
            sec.name = n.get("name").getString()
            sec.url = n.get("url").getString()
            sec.orgIndex = self.total()
            self.sections.append(sec)
            self.onAddItem(sec)
        Log.v("loadByJsonData:", json)

    # --------------
    def clear(self):
        self.sections = []

    def total(self):
        return self.sections.__len__()

    def get(self, idx):
        if self.sections == None:
            return None
        len = self.sections.__len__()
        if idx >= len or idx < 0:
            return None
        else:
            return self.sections[idx]

    def onAddItem(self, sec):
        pass
