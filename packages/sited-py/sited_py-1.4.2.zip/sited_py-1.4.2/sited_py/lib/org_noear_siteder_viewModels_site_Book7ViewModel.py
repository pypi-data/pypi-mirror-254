# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-10-05
LastEditors:Do not edit
LastEditTime:2021-01-21
Description:
"""
from .org_noear_siteder_dao_engine_sdVewModel_MediaSdViewModel import MediaSdViewModel
from .mytool import TextUtils


class Book7ViewModel(MediaSdViewModel):
    def playItem(self):
        return self.get(self.playIndex)

    def playUrl(self):
        return self.get(self.playIndex).url

    # public final DdSource source
    def __init__(self, n):
        super().__init__()
        self.playIndex = 0
        self.currentIndex = 0
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
