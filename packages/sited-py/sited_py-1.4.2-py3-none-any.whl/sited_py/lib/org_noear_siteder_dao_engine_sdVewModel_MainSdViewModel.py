# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-06-11
LastEditors:Do not edit
LastEditTime:2021-03-04
Description:
"""
from .org_noear_siteder_viewModels_ViewModelBase import ViewModelBase
from .org_noear_siteder_dao_engine_DdSource import DdSource
from .org_noear_siteder_models_BookModel import BookModel
from .org_noear_siteder_models_BookUpdateModel import BookUpdateModel
from .org_noear_siteder_models_TagModel import TagModel
from .org_noear_siteder_dao_engine_DdNode import DdNode
from .org_noear_siteder_Config import Config
from .mytool import TextUtils
from .org_noear_sited_SdValue import SdValue
from .noear_snacks_ONode import ONode


class MainSdViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.tagList = []
        self.hotList = []
        self.updateList = []

    def clear(self):
        self.tagList = []
        self.hotList = []
        self.updateList = []

    def total(self):
        return (
            self.tagList.__len__() + self.hotList.__len__() + self.updateList.__len__()
        )

    # @Override
    def loadByConfig(self, config):
        if DdSource.isHots(config):
            self.hotList = []
            for t1 in config.items():
                b = BookModel()
                b.name = t1.title
                b.url = t1.url.value
                b.logo = t1.logo
                self.hotList.append(b)
            return
        if DdSource.isUpdates(config):
            self.updateList = []
            for t1 in config.items():
                b = BookUpdateModel()
                b.name = t1.title
                b.url = t1.url.value
                b.logo = t1.logo
                self.updateList.append(b)
            return
        if DdSource.isTags(config):
            self.tagList = []
            cfg = config
            for t1 in config.items():
                self.doAddTagItem(cfg, t1)
            return

    # @Override
    def loadByJson(self, config, *jsons):
        # java版: (String... jsons) 表示可变长度参数列表，参数为0到多个String类型的对象，或者是一个String[]。
        if jsons == None or jsons.__len__() == 0:
            return
        # py版: (*jsons) 表示可变参数组成的元组，要type(jsons[0])==list识别java版的多个String或者一个String[]
        if jsons.__len__() == 1 and type(jsons[0]) == list:
            jsons = jsons[0]
        # try:
        for json in jsons:
            # 支持多个数据块加载
            data = ONode.tryLoad(json).asArray()
            if DdSource.isHots(config):
                for n in data:
                    b = BookModel()
                    b.name = n.get("name").getString()
                    b.url = n.get("url").getString()
                    b.logo = n.get("logo").getString()
                    self.hotList.append(b)
                return
            if DdSource.isUpdates(config):
                for n in data:
                    b = BookUpdateModel()
                    b.name = n.get("name").getString()
                    b.url = n.get("url").getString()
                    b.logo = n.get("logo").getString()
                    b.newSection = n.get("newSection").getString()
                    b.updateTime = n.get("updateTime").getString()
                    self.updateList.append(b)
                return
            if DdSource.isTags(config):
                cfg = config
                for n in data:
                    t1 = DdNode(None)
                    t1.title = n.get("title").getString()
                    t1.url = SdValue(n.get("url").getString())
                    t1.group = n.get("group").getString()
                    t1.logo = n.get("logo").getString()
                    self.doAddTagItem(cfg, t1)

    def doAddTagItem(self, cfg, t1):
        if Config.isPhone() and TextUtils.isEmpty(cfg.showImg) == False:
            if TextUtils.isEmpty(t1.group) == False:
                self.tagList.append(TagModel(t1.group, None, 10))
            if TextUtils.isEmpty(t1.title) == False:
                self.tagList.append(TagModel(t1.title, t1.url.value, 0))
        else:
            if TextUtils.isEmpty(t1.group) == False:
                temp = self.tagList.__len__() % 3
                if temp > 0:
                    temp = 3 - temp
                while temp > 0:
                    self.tagList.append(TagModel("", None, 1))
                    temp -= 1
                self.tagList.append(TagModel("", None, 11))
                self.tagList.append(TagModel(t1.group, None, 10))
                self.tagList.append(TagModel("", None, 11))
            if TextUtils.isEmpty(t1.title) == False:
                self.tagList.append(TagModel(t1.title, t1.url.value, 0))
