# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-10-05
LastEditors:Do not edit
LastEditTime:2021-01-21
Description:
"""
from .org_noear_siteder_models_TxtModel import TxtModel
from .org_noear_siteder_dao_engine_sdVewModel_TextSdViewModel import TextSdViewModel


class Section2ViewModel(TextSdViewModel):
    def addTitleItem(self, d, isB):
        txt = TxtModel(self.referer, d, 1, isB)
        self.items.append(txt)

    def addToolItem(self):
        txt = TxtModel(self.referer, "", 99, False)
        self.items.append(txt)

    def __init__(self, section):
        # 参数类型是SectionModel
        super().__init__(section.url)
        self.currentIndex = 0
        self.section = section
