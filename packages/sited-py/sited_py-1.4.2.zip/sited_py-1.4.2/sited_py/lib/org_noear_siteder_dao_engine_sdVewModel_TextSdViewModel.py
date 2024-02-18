# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-10-05
LastEditors:Do not edit
LastEditTime:2021-03-04
Description:
"""
from .org_noear_siteder_models_TxtModel import TxtModel
from .org_noear_siteder_viewModels_ViewModelBase import ViewModelBase
from .mytool import TextUtils
from .noear_snacks_ONode import ONode


class TextSdViewModel(ViewModelBase):
    def __init__(self, referer):
        super().__init__()
        self.items = []
        # 从网页过来时，需要name,logo
        self.name = None
        self.logo = None
        self.referer = referer

    def clear(self):
        self.items = []

    def total(self):
        return self.items.__len__()

    def get(self, index):
        if index >= 0 and index < self.total():
            return self.items[index]
        else:
            return None

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
        list = None
        obj = ONode.tryLoad(json)
        if obj.isObject():
            list = obj.get("list").asArray()
            if TextUtils.isEmpty(self.name):
                self.name = obj.get("name").getString()
                self.logo = obj.get("logo").getString()
        else:
            list = obj
        idx = 0  # 一段段的插入开头
        for n in list:
            txt = TxtModel(
                self.referer,
                n.get("d").getString(),
                n.get("t").getInt(),
                n.get("c").getString(),
                n.get("b").getInt() > 0,
                n.get("i").getInt() > 0,
                n.get("u").getInt() > 0,
                n.get("w").getInt(),
                n.get("h").getInt(),
                n.get("url").getString(),
                n.get("ss").getInt() > 0,
            )
            if config.update == 2:
                self.items.insert(idx, txt)
                idx += 1
            else:
                self.items.append(txt)
