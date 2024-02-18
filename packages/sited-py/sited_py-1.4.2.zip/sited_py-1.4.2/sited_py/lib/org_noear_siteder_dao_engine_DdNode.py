# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-22
LastEditors:Do not edit
LastEditTime:2020-10-06
Description:
"""
from .org_noear_sited_SdAttributeList import SdAttributeList
from .org_noear_sited_SdNode import SdNode
from .mytool import TextUtils


class DdNode(SdNode):
    def s(self):
        return self.source

    def __init__(self, source):
        super().__init__(source)
        # 是否支持全部下载(book[1,2,3])
        self.donwAll = True
        # 是否显示导航能力（用于：section[1,2,3]） 即上一章下一章
        self.showNav = True
        # 是否显示图片（None：默认；0：不显示；1：显示小图；2：显示大图）
        self.showImg = None
        # 是否自适应大小（基于pad 或 phone 显示不同的大小）
        self.autoSize = False
        # 是否显示S按钮
        self.showWeb = True
        # 屏幕方向（v/h）
        self.screen = None
        # 首页图片显示的宽高比例
        self.WHp = 0
        # 是否循环播放
        self.loop = False
        # 样式风格
        self.style = 0
        # 预设选项
        self.options = None
        self._web = None

    # @Override
    def OnDidInit(self):
        self.donwAll = self.attrs.getInt("donwAll", 1) > 0
        self.showNav = self.attrs.getInt("showNav", 1) > 0
        self.showImg = self.attrs.getString("showImg")
        self.autoSize = self.attrs.getInt("autoSize", 0) > 0
        self.showWeb = (
            self.attrs.getInt("showWeb", 0 if self.s().isPrivate() else 1) > 0
        )  # isPrivate时，默认不显示；否则默认显示
        self.screen = self.attrs.getString("screen")
        self.loop = self.attrs.getInt("loop", 0) > 0
        self._web = self.attrs.getValue("web")  # 控制外部浏览器的打开
        if self.source.schema < 2:
            self._web.build = self.attrs.getString("buildWeb")

        self.options = self.attrs.getString("options")
        self.style = self.attrs.getInt("style", DdNode.STYLE_VIDEO)
        if TextUtils.isEmpty(self.screen) and self.style == DdNode.STYLE_AUDIO:
            self.screen = "v"

        w = self.attrs.getString("w")
        if TextUtils.isEmpty(w) == False:
            h = self.attrs.getString("h")
            self.WHp = float(w) / float(h)

    # 是否内部WEB运行
    def isWebrun(self):
        run = self.attrs.getString("run")
        if run == None:
            return False
        return run.find("web") >= 0

    # 是否外部WEB运行
    def isOutWebrun(self):
        run = self.attrs.getString("run")
        if run == None:
            return False
        return run.find("outweb") >= 0

    def getWebUrl(self, url):
        atts = SdAttributeList()
        atts.set("url", url)
        return self._web.run(self.source, atts, url)


DdNode.STYLE_VIDEO = 11
DdNode.STYLE_AUDIO = 12
DdNode.STYLE_INWEB = 13
