# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-23
LastEditors:Do not edit
LastEditTime:2020-10-06
Description:
"""
from .org_noear_sited_SdNode import SdNode
from .mytool import TextUtils
from .org_noear_sited_SdAttributeList import SdAttributeList


class DdNodeLogin(SdNode):
    def s(self):
        return self.source

    def __init__(self, source):
        super().__init__(source)
        # 只应用于login节点
        self.onCheck = None
        self.isAutoCheck = True

    # @Override
    def OnDidInit(self):
        self.onCheck = self.attrs.getString2("onCheck", "check")  # 控制外部浏览器的打开
        self.isAutoCheck = self.attrs.getInt("auto") > 0  # 返回布尔值

    # 是否内部WEB运行
    def isWebrun(self):
        run = self.attrs.getString("run")
        if run == None:
            return False
        return run.find("web") >= 0

    def doCheck(self, url, cookies, isFromAuto):
        if TextUtils.isEmpty(self.onCheck):
            return True
        else:
            if url == None or cookies == None:
                return False
            attrs = SdAttributeList()
            attrs.set("url", url)
            attrs.set("cookies", "" if cookies == None else cookies)
            if isFromAuto:
                if self.isAutoCheck:
                    temp = self.source.callJs(self.onCheck, attrs)
                    return temp == "1"
                else:
                    return True  # 如果不支持自动,则总是返回ok
            else:
                temp = self.source.callJs(self.onCheck, attrs)
                return "1" == temp
