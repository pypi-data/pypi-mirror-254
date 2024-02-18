# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-10-05
LastEditors:Do not edit
LastEditTime:2021-03-04
Description:
"""
from .org_noear_siteder_models_PicModel import PicModel
from .org_noear_siteder_viewModels_ViewModelBase import ViewModelBase
from .org_noear_siteder_dao_engine_DdSource import DdSource
from .mytool import TextUtils
from .noear_snacks_ONode import ONode


class ProductSdViewModel(ViewModelBase):
    def __init__(self, url):
        super().__init__()
        self.pictures = []
        self.logo = None
        self.name = None
        self.shop = None
        self.intro = None
        self.buyUrl = None
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
        if DdSource.isBook(config):
            if TextUtils.isEmpty(self.shop):
                self.logo = data.get("logo").getString()
                self.name = data.get("name").getString()
                self.shop = data.get("shop").getString()
                self.intro = data.get("intro").getString()
                self.buyUrl = data.get("buyUrl").getString()
        sl = data.get("pictures").asArray()
        for n in sl:
            pic = PicModel(self.bookUrl, n.getString())
            self.pictures.append(pic)

    # --------------
    def clear(self):
        self.pictures = []

    def total(self):
        return self.pictures.__len__()

    def get(self, index):
        return self.pictures[index]

