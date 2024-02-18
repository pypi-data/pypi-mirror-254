# -*- coding: UTF-8 -*-
"""
Author:wistn
since:Do not edit
LastEditors:Do not edit
LastEditTime:2021-03-04
Description:
"""
from .org_noear_siteder_models_BookSearchModel import BookSearchModel
from .org_noear_siteder_viewModels_ViewModelBase import ViewModelBase
from .noear_snacks_ONode import ONode


class SearchSdViewModel(ViewModelBase):
    # @Override
    def loadByConfig(self, c):
        config = c

        if self.doFilter(c.title):
            return

        b = BookSearchModel()

        cfg = config.s().search

        b._dtype = cfg.dtype()
        b.btype = cfg.btype()
        b.name = c.title
        b.url = c.url.value
        b.logo = c.logo
        b.updateTime = ""
        b.newSection = ""
        b.author = ""
        b.status = ""
        b.source = config.source.title

        self.doAddItem(b)

    # @Override
    def loadByJson(self, c, *jsons):
        # java版: (String... jsons) 表示可变长度参数列表，参数为0到多个String类型的对象，或者是一个String[]。
        if jsons == None or jsons.__len__() == 0:
            return

        config = c
        # py版: (*jsons) 表示可变参数组成的元组，要type(jsons[0])==list识别java版的多个String或者一个String[]
        if jsons.__len__() == 1 and type(jsons[0]) == list:
            jsons = jsons[0]

        for json in jsons:
            # 支持多个数据块加载
            data = ONode.tryLoad(json)
            if data.isArray():
                for n in data:
                    name = n.get("name").getString()
                    if self.doFilter(name):
                        continue
                    b = BookSearchModel()
                    b.name = name
                    b.url = n.get("url").getString()
                    b.logo = n.get("logo").getString()
                    b.updateTime = n.get("updateTime").getString()
                    b.newSection = n.get("newSection").getString()
                    b.author = n.get("author").getString()
                    b.status = n.get("status").getString()
                    b.source = config.source.title
                    b.btag = n.get("btag").getString()
                    cfg = config.s().book(b.url)  # 类型DdNode
                    b._dtype = cfg.dtype()
                    b.btype = cfg.btype()
                    self.doAddItem(b)

    def doFilter(self, name):
        pass

    def doAddItem(self, item):
        pass

    def clear(self):
        pass

    def total(self):
        pass

