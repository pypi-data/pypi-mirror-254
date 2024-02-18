# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-10-05
LastEditors:Do not edit
LastEditTime:2020-10-06
Description:
"""
from .org_noear_siteder_models_ModelBase import ModelBase


class MediaModel(ModelBase):
    def __init__(self, *arguments):
        super().__init__()
        self.url = None
        self.type = None  # 用于下载
        self.mime = None  # 用于下载
        self.logo = None  # 用于下载
        len = arguments.__len__()
        if len == 1:
            url = arguments[0]
            self.url = url
        elif len == 4:
            url = arguments[0]
            type = arguments[1]
            mime = arguments[2]
            logo = arguments[3]
            self.url = url
            self.type = type
            self.mime = mime
            self.logo = logo

    def getUri(self):
        return self.url

    # 用于下载
    def fileFullName(self, fileName):
        return fileName + self.type

