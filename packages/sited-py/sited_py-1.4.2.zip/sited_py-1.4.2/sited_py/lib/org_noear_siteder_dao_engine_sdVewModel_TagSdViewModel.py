# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-10-05
LastEditors:Do not edit
LastEditTime:2021-03-04
Description:
"""
from .org_noear_siteder_viewModels_ViewModelBase import ViewModelBase
from .org_noear_siteder_models_BookUpdateModel import BookUpdateModel
from .noear_snacks_ONode import ONode


class TagSdViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.list = []

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
            # 支持多个数据块加载
            data = ONode.tryLoad(json)
            if data.isArray():
                for n in data:
                    name = n.get("name").getString()
                    b = BookUpdateModel()
                    b.name = name
                    b.url = n.get("url").getString()
                    b.logo = n.get("logo").getString()
                    b.author = n.get("author").getString()
                    b.newSection = n.get("newSection").getString()
                    b.updateTime = n.get("updateTime").getString()
                    b.status = n.get("status").getString()
                    self.list.append(b)

    def clear(self):
        self.list = []

    def total(self):
        return self.list.__len__()

    def get(self, index):
        return self.list[index]
