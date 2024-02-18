# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-24
LastEditors:Do not edit
LastEditTime:2020-10-06
Description:
"""
from .org_noear_sited_SdApi import SdApi


class SdExt:
    def __init__(self, s):
        self.source = s

    def set(self, key, val):
        SdApi.set(self.source, key, val)

    def get(self, key):
        return SdApi.get(self.source, key)
