# -*- coding: UTF-8 -*-
"""
Author:wistn
asince:2020-05-11
LastEditors:Do not edit
LastEditTime:2020-10-06
Description:
"""
from .org_noear_sited_DataBlock import DataBlock


class Map(dict):
    def has(self, key):
        return key in self

    def set(self, key, value):
        self[key] = value


class DataContext:
    def __init__(self):
        self._data = Map()

    def add(self, node, tag, text):
        if self._data.has(node):
            self._data.get(node).set(tag, text)
        else:
            dt = DataBlock()
            dt.set(tag, text)
            self._data.set(node, dt)

    def nodes(self):
        return self._data.keys()

    def get(self, node):
        return self._data.get(node)
