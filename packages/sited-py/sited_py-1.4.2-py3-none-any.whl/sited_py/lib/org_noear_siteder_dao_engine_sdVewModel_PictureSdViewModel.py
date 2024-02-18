# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-10-05
LastEditors:Do not edit
LastEditTime:2021-03-04
Description:
"""
from .org_noear_siteder_models_PicModel import PicModel
from .org_noear_siteder_utils_StateTag import StateTag
from .org_noear_siteder_viewModels_ViewModelBase import ViewModelBase
from .mytool import TextUtils
from .noear_snacks_ONode import ONode


class PictureSdViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.bgUrl = None
        self.items = []
        # 从网页过来时，需要name,logo
        self.name = None
        self.logo = None

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

    """
    支持
    ["","",""]
    或
    {bg:"",list:["","",""]}
    或
    {bg:"",list:[{url:"",time:"mm::ss.xx"},{...}]}
     或
    {bg:"",logo:"",name:"",list:[{url:"",time:"mm::ss.xx"},{...}]}
    """
    # @Override
    def loadByJson(self, config, *jsons):
        # java版: (String... jsons) 表示可变长度参数列表，参数为0到多个String类型的对象，或者是一个String[]。
        if jsons == None or jsons.__len__() == 0:
            return
        # py版: (*jsons) 表示可变参数组成的元组，要type(jsons[0])==list识别java版的多个String或者一个String[]
        if jsons.__len__() == 1 and type(jsons[0]) == list:
            jsons = jsons[0]
        for json in jsons:
            state = StateTag()
            self.loadByJsonData(config, json, state)

    def loadByJsonData(self, config, json, state):
        list = None
        obj = ONode.tryLoad(json)
        if obj.isObject():
            list = obj.get("list").asArray()
            bg = obj.get("bg").getString()
            if TextUtils.isEmpty(bg) == False:
                self.bgUrl = bg
            if TextUtils.isEmpty(self.name):
                self.name = obj.get("name").getString()
                self.logo = obj.get("logo").getString()
        else:
            list = obj
        for n in list:
            pic = None
            if n.isObject():
                pic = PicModel(
                    self.section(),
                    n.get("url").getString(),
                    n.get("time").getInt(),
                    state.value,
                )
            else:
                pic = PicModel(self.section(), n.getString(), 0, state.value)
            if TextUtils.isEmpty(pic.url):
                return
            pic.cacheID = self.items.__len__()
            self.doAddItem(pic, state)
            state.value += 1

    def doAddItem(self, pic, state):
        pass

    def section(self):
        pass
