# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-10-05
LastEditors:Do not edit
LastEditTime:2020-10-05
Description:
"""
from .org_noear_siteder_dao_engine_sdVewModel_MediaSdViewModel import MediaSdViewModel


class Section3ViewModel(MediaSdViewModel):
    def __init__(self):
        super().__init__()
        self.playIndex = 0
        self.currentIndex = 0

    def playItem(self):
        return self.get(self.playIndex)

    def playUrl(self):
        return self.get(self.playIndex).url
