# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-10-05
LastEditors:Do not edit
LastEditTime:2020-10-06
Description:
"""
from .org_noear_siteder_models_TxtModel import TxtModel
from .org_noear_siteder_dao_engine_sdVewModel_TextSdViewModel import TextSdViewModel
from .mytool import TextUtils


class Book8ViewModel(TextSdViewModel):
    def addTitleItem(self, d, isB):
        txt = TxtModel(self.referer, d, 1, isB)
        self.items.append(txt)

    def __init__(self, s, n):
        super().__init__(n.url)
        self.source = s
        self.node = n

    # @Override
    def loadByJson(self, config, *jsons):
        super().loadByJson(config, *jsons)
        # -----------
        if TextUtils.isEmpty(self.logo) == False:
            self.node.logo = self.logo
        else:
            if TextUtils.isEmpty(self.logo):
                self.logo = self.node.logo
        if TextUtils.isEmpty(self.name) == False:
            self.node.name = self.name
        else:
            if TextUtils.isEmpty(self.name):
                self.name = self.node.name
