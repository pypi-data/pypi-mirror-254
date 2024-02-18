# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-04
LastEditors:Do not edit
LastEditTime:2020-05-24
Description:
"""
from .org_noear_sited_SdNodeSet import SdNodeSet
from .mytool import TextUtils


class DdNodeSet(SdNodeSet):
    def s(self):
        return self.source

    def __init__(self, source):
        super().__init__(source)
        self.btag = None
        self.durl = None  # 数据url（url是给外面看的；durl是真实的地址）
        self.showWeb = False

    # @Override
    def OnDidInit(self):
        self.showWeb = (
            self.attrs.getInt("showWeb", (0 if self.s().isPrivate() else 1)) > 0
        )
        self.durl = self.attrs.getString("durl", self.source.url)
        self.btag = self.attrs.getString("btag")
        if TextUtils.isEmpty(self.btag):
            # 对旧格式的兼容
            self.btag = self.attrs.getString("dtag")
