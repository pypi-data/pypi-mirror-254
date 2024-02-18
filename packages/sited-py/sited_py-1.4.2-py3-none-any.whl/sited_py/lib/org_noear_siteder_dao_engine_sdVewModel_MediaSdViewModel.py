# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-10-05
LastEditors:Do not edit
LastEditTime:2021-03-04
Description:
"""
from .org_noear_siteder_models_MediaModel import MediaModel
from .org_noear_siteder_viewModels_ViewModelBase import ViewModelBase
from .mytool import TextUtils
from .noear_snacks_ONode import ONode


class MediaSdViewModel(ViewModelBase):
    # 从网页过来时，需要name,logo
    def __init__(self):
        super().__init__()
        self.items = []
        self.name = None
        self.logo = None

    def total(self):
        return self.items.__len__()

    def clear(self):
        self.items = []

    def get(self, index):
        return self.items[index]

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
            if json.startswith("{") or json.startswith("["):
                jList = None
                obj = ONode.tryLoad(json)
                if obj.isObject():
                    jList = obj.get("list").asArray()
                    if TextUtils.isEmpty(self.name):
                        self.name = obj.get("name").getString()
                        self.logo = obj.get("logo").getString()
                else:
                    jList = obj
                for n1 in jList:
                    self.items.append(
                        MediaModel(
                            n1.get("url").getString(),
                            n1.get("type").getString(),
                            n1.get("mime").getString(),
                            n1.get("logo").getString(),
                        )
                    )
            else:
                for url in json.split(";"):
                    if url.__len__() > 6:
                        self.items.append(MediaModel(url))
