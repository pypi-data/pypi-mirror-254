# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-02
LastEditors:Do not edit
LastEditTime:2021-03-16
Description:
"""
import os
import json
from .org_noear_sited_SdAdapter import SdAdapter
from .org_noear_siteder_dao_engine_DdNodeLogin import DdNodeLogin
from .org_noear_siteder_dao_engine_DdNodeAbout import DdNodeAbout
from .org_noear_siteder_dao_engine_DdNode import DdNode
from .org_noear_siteder_dao_engine_DdNodeSet import DdNodeSet
from .org_noear_siteder_utils_LogWriter import LogWriter
from .me_noear_utils_EncryptUtil import EncryptUtil
from .org_noear_siteder_dao_Setting import Setting


class DdAdapter(SdAdapter):
    # @Override
    def createNode(self, source, tagName):
        if "login" == tagName:
            return DdNodeLogin(source)
        elif "reward" == tagName or "about" == tagName:
            return DdNodeAbout(source)
        else:
            return DdNode(source)

    # @Override
    def createNodeSet(self, source, tagName):
        return DdNodeSet(source)

    # --------------------------------
    def __init__(self):
        super().__init__()
        self._root = None

    # @Override
    def cacheRoot(self):
        if self._root == None:
            self._root = os.path.join(
                os.path.dirname(os.path.realpath(__file__)), "..", "files"
            )
        return self._root

    # --------------------------------
    # @Override
    def log(self, source, tag, msg, tr):
        if msg == None:
            msg = "None"
        if Setting.isDeveloperModel():
            LogWriter.tryInit()
            LogWriter.loger.print(tag, msg, tr)
            if "JsEngine.print" == tag:
                # ok
                print(
                    "安卓版界面print消息："
                    + (
                        "（完整内容在sited_print.txt）" + msg[0:350]
                        if msg.__len__() > 350
                        else msg
                    )
                )
                LogWriter.jsprint.print(tag, msg, tr)
            if tr != None:
                LogWriter.error.print(source.url + "::\r\n" + tag, msg, None)

    # @Override
    def get(self, source, key):
        if "g_location" == key:
            n = {}
            #  模拟 noear.snacks.ONode
            return json.dumps(n)
        newKey = EncryptUtil.md5(source.url_md5 + "::" + key)
        return DdAdapter.mSets.getString(newKey, "")

    # @Override
    def set(self, source, key, val):
        newKey = EncryptUtil.md5(source.url_md5 + "::" + key)
        DdAdapter.mSets.putString(newKey, val)

    # @Override
    def buildHttpHeader(self, cfg, url, header):
        # HttpHeaderHandler header实际为callback
        if cfg == None:
            return
        if cfg.isInCookie():
            self.doBuildCookie(cfg, url, header)
        if cfg.isInReferer():
            self.doBuildRererer(cfg, url, header)
        if cfg.isEmptyHeader() == False:
            s = cfg.source
            if s.engine < 34:
                for kv in cfg.getHeader(url).split(";"):
                    idx = kv.find("=")
                    if idx > 0:
                        k = kv[0:idx].strip()
                        v = kv[idx + 1 :].strip()
                        header(k, v)
                    else:
                        if kv == "cookie":
                            self.doBuildCookie(cfg, url, header)
                        if kv == "referer":
                            self.doBuildRererer(cfg, url, header)
            else:
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


#  static SharedPreferences mSets = App.getSettings("sited", Context.MODE_PRIVATE);
class SharedPreferences:
    def __init__(self):
        self._items = {}

    def getString(self, key, def_):
        if key in self._items:
            return self._items.get(key)
        else:
            return def_

    def putString(self, key, val):
        self._items[key] = val


DdAdapter.mSets = SharedPreferences()
