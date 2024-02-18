# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-23
LastEditors:Do not edit
LastEditTime:2020-05-23
Description:
"""
from .org_noear_sited_SdNode import SdNode


class DdNodeAbout(SdNode):
    def s(self):
        return self.source

    def __init__(self, source):
        super().__init__(source)
        self.mail = None

    # @Override
    def OnDidInit(self):
        self.mail = self.attrs.getString("mail")

    # 是否内部WEB运行
    def isWebrun(self):
        run = self.attrs.getString("run")
        if run == None:
            return False
        return run.find("web") >= 0
