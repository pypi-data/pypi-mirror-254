# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-02
LastEditors:Do not edit
LastEditTime:2020-05-02
Description:
"""


class SdAdapter:
    def createNode(self, source, tagName):
        return SdNode(source)

    def createNodeSet(self, source, tagName):
        return SdNodeSet(source)

    def cacheRoot(self):
        return None

    def log(self, source, tag, msg, tr):
        pass

    def set(self, source, key, val):
        pass

    def get(self, source, key):
        return ""

    def doBuildCookie(self, cfg, url, header):
        cookies = cfg.buildCookies(url)
        if cookies != None:
            header("Cookie", cookies)

    def doBuildRererer(self, cfg, url, header):
        header("Referer", cfg.getReferer(url))

    # header实际为callback
    def buildHttpHeader(self, cfg, url, header):
        if cfg == None:
            return
        if cfg.isInCookie():
            self.doBuildCookie(cfg, url, header)

        if cfg.isInReferer():
            self.doBuildRererer(cfg, url, header)

        if cfg.isEmptyHeader() == False:
            for kv in cfg.getHeader(url).split("$$"):
                idx = kv.find(":")
                if idx > 0:
                    k = kv[0:idx].strip()
                    v = kv[idx + 1 :].strip()
                    header(k, v)
                else:
                    if kv == "cookie":
                        self.doBuildCookie(cfg, url, header)
                    if kv == "referer":
                        self.doBuildRererer(cfg, url, header)


from .org_noear_sited_SdNode import SdNode
from .org_noear_sited_SdNodeSet import SdNodeSet

# 不能先引用，不然有循环依赖
