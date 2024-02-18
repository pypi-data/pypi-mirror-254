# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-10-05
LastEditors:Do not edit
LastEditTime:2021-03-04
Description:
"""
from .org_noear_siteder_models_PicModel import PicModel
from .mytool import TextUtils
from .org_noear_siteder_dao_engine_DdSource import DdSource
from .org_noear_siteder_dao_engine_sdVewModel_ProductSdViewModel import (
    ProductSdViewModel,
)
from .noear_snacks_ONode import ONode


class Book5ViewModel(ProductSdViewModel):
    def __init__(self, s, n):
        super().__init__(n.url)
        self.source = s
        self.node = n
        self.intro = ""

    def loadByJson(self, config, *jsons):
        # java版: (String... jsons) 表示可变长度参数列表，参数为0到多个String类型的对象，或者是一个String[]。
        if jsons == None or jsons.__len__() == 0:
            return
        # py版: (*jsons) 表示可变参数组成的元组，要type(jsons[0])==list识别java版的多个String或者一个String[]
        if jsons.__len__() == 1 and type(jsons[0]) == list:
            jsons = jsons[0]
        for json in jsons:
            if json.find("shop") > 0 or json.find("pictures") > 0:
                self.loadByJsonData(config, json)
            else:
                self.loadByJsonOld(config, json)
        # -----------------
        if TextUtils.isEmpty(self.logo) == False:
            self.node.logo = self.logo
        else:
            self.logo = self.node.logo
        if TextUtils.isEmpty(self.name) == False:
            self.node.name = self.name

    def loadByJsonOld(self, config, json):
        data = ONode.tryLoad(json)
        if DdSource.isBook(config):
            if TextUtils.isEmpty(self.shop):
                self.logo = data.get("logo").getString()
                self.name = data.get("name").getString()
                self.shop = data.get("author").getString()
                self.intro = data.get("intro").getString()
                self.buyUrl = data.get("tags").getString()

        sl = data.get("sections").asArray()
        for n in sl:
            pic = PicModel(self.bookUrl, n.get("url").getString())
            self.pictures.append(pic)
