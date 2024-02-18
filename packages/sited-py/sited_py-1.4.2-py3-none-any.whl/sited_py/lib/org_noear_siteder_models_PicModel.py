# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-10-05
LastEditors:Do not edit
LastEditTime:2020-10-05
Description:
"""
from .org_noear_siteder_models_ModelBase import ModelBase

class PicModel(ModelBase):
    # public DdSource source
    def __init__(self, *arguments):
        super().__init__()
        self.referer = None
        self.url = None
        self.time = 0
        self.secIndex = 0
        self.section = None
        self.cacheID = 0
        self.orgWidth = 0
        self.orgHeight = 0
        self.tmpWidth = 0
        self.tmpHeight = 0
        self.isPicLoaded = False
        len = arguments.__len__()
        if len == 2:
            referer = arguments[0]
            url = arguments[1]
            self.referer = referer
            self.section = None
            self.secIndex = 0
            self.url = url
            self.time = 0
        elif len == 4:
            section = arguments[0]
            url = arguments[1]
            time = arguments[2]
            secIndex = arguments[3]
            self.referer = section.url
            self.section = section
            self.secIndex = secIndex
            self.url = url
            self.time = time

