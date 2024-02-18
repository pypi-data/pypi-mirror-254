# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-19
LastEditors:Do not edit
LastEditTime:2020-09-25
Description:
"""
from .mytool import TextUtils


class SdValue:
    def __init__(self, *arguments):
        self.value = None  # 静态值
        self.build = None  # 动态构建函数
        len = arguments.__len__()
        if len == 1:
            value = arguments[0]
            self.__init__(value, None)
        elif len == 2:
            value = arguments[0]
            def_ = arguments[1]
            self.value = value
            if value != None and value.startswith("js:"):
                self.build = value[3:]
                self.value = def_

    def isEmpty(self):
        return TextUtils.isEmpty(self.value) and TextUtils.isEmpty(self.build)

    def isEmptyValue(self):
        return TextUtils.isEmpty(self.value)

    def isEmptyBuild(self):
        return TextUtils.isEmpty(self.build)

    # ============================================================
    #
    #
    def getValue(self, def_):
        if self.value == None:
            return def_
        else:
            return self.value

    def find(self, str):
        if self.value == None:
            return -1
        else:
            return self.value.find(str)

    # ============================================================
    #
    #
    def run(self, *arguments):
        len = arguments.__len__()
        if len == 2:
            sd = arguments[0]
            args = arguments[1]
            return self.run(sd, args, self.value)
        elif len == 3:
            sd = arguments[0]
            args = arguments[1]
            defValue = arguments[2]
            if TextUtils.isEmpty(self.build):
                return defValue
            else:
                return sd.js.callJs(self.build, args)
