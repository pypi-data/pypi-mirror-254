# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-10-05
LastEditors:Do not edit
LastEditTime:2020-10-05
Description:
"""
from .org_noear_siteder_dao_engine_sdVewModel_TagSdViewModel import TagSdViewModel


class TagViewModel(TagSdViewModel):
    def __init__(self):
        super().__init__()
        self.currentPage = 1
