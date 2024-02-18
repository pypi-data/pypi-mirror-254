# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-10-05
LastEditors:Do not edit
LastEditTime:2020-10-06
Description:
"""
from .org_noear_siteder_models_ModelBase import ModelBase


class TxtModel(ModelBase):
    def __init__(self, *arguments):
        super().__init__()
        self.referer = None
        self.data = None
        self.type = 0
        self.url = None
        # 样式
        self.color = None
        self.isBold = False
        self.isItalic = False
        self.isUnderline = False
        self.width = 0
        self.height = 0
        self.isSectionOpen = False
        len = arguments.__len__()
        if len == 4:
            referer = arguments[0]
            data = arguments[1]
            type = arguments[2]
            b = arguments[3]
            self.referer = referer
            self.data = data
            self.type = type
            self.isBold = b
            if self.type == 2:
                self.type = 1
                self.isBold = True
        elif len == 11:
            referer = arguments[0]
            data = arguments[1]
            type = arguments[2]
            c = arguments[3]
            b = arguments[4]
            i = arguments[5]
            u = arguments[6]
            w = arguments[7]
            h = arguments[8]
            url = arguments[9]
            ss = arguments[10]
            self.referer = referer
            self.data = data
            self.type = type
            self.url = url
            self.color = c
            self.isBold = b
            self.isItalic = i
            self.isUnderline = u
            self.width = w
            self.height = h
            self.isSectionOpen = ss
            if self.type == 2:
                self.type = 1
                self.isBold = True

