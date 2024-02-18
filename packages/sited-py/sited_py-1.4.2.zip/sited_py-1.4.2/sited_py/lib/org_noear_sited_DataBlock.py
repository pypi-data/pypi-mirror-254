# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-11
LastEditors:Do not edit
LastEditTime:2020-06-11
Description:
"""


class DataBlock(dict):
    def has(self, key):
        return key in self

    def set(self, key, value):
        self[key] = value
