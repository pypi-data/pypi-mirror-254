# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-06-11
LastEditors:Do not edit
LastEditTime:2020-10-06
Description:
"""
from .org_noear_siteder_models_ModelBase import ModelBase


class TagModel(ModelBase):
    def __init__(self, *arguments):
        super().__init__()
        self.name = None
        self.url = None
        self.type = 0  # 0分类；1填空  10分组；11分组填空
        len = arguments.__len__()
        if len == 3:
            name = arguments[0]
            url = arguments[1]
            type = arguments[2]
            self.name = name
            self.url = url
            self.type = type
        elif len == 2:
            name = arguments[0]
            url = arguments[1]
            self.name = name
            self.url = url
            self.type = 0
