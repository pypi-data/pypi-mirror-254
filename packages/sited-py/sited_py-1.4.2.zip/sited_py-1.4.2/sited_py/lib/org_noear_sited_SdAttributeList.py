# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-19
LastEditors:Do not edit
LastEditTime:2020-09-25
Description:
"""


class SdAttributeList:
    def __init__(self):
        self._items = {}
        self._values = []

    def getValues(self):
        return self._values

    def getJson(self):
        return Util.toJson(self._items)

    def count(self):
        return self._items.__len__()

    def clear(self):
        self._items.clear()

    def contains(self, key):
        return key in self._items

    def set(self, key, val):
        self._items[key] = val
        self._values.append(val)

    def getValue(self, *arguments):
        len = arguments.__len__()
        if len == 1:
            key = arguments[0]
            return self.getValue(key, None)
        elif len == 2:
            key = arguments[0]
            def_ = arguments[1]
            val = self.getString(key)
            return SdValue(val, def_)

    def getString2(self, key, key2):
        if self.contains(key):
            return self.getString(key, None)
        else:
            return self.getString(key2, None)

    def getString(self, *arguments):
        len = arguments.__len__()
        if len == 1:
            key = arguments[0]
            return self.getString(key, None)
        elif len == 2:
            key = arguments[0]
            def_ = arguments[1]
            if self.contains(key):
                return self._items.get(key)
            else:
                return def_

    def getInt(self, *arguments):
        len = arguments.__len__()
        if len == 1:
            key = arguments[0]
            return self.getInt(key, 0)

        elif len == 2:
            key = arguments[0]
            def_ = arguments[1]
            if self.contains(key):
                return int(self._items.get(key))
            else:
                return def_

    def getLong(self, *arguments):
        len = arguments.__len__()
        if len == 1:
            key = arguments[0]
            return self.getLong(key, 0)
        elif len == 2:
            key = arguments[0]
            def_ = arguments[1]
            if self.contains(key):
                return int(self._items.get(key))
            else:
                return def_

    def addAll(self, attrs):
        # 浅拷贝（引用对象）对应java上HashMap.putAll
        for [key, value] in attrs._items.items():
            self._items[key] = value


from .org_noear_sited_SdValue import SdValue
from .org_noear_sited_Util import Util

# 不能先引用，不然有循环依赖
