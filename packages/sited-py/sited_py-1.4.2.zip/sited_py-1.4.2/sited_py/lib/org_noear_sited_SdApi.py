# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-04-28
LastEditors:Do not edit
LastEditTime:2021-03-02
Description:
"""
import traceback


class SdApi:
    @classmethod
    def tryInit(cls, adapter):
        SdApi._adapter = adapter

    # -------------------------------
    @classmethod
    def log(cls, *arguments):
        if arguments.__len__() == 5:
            source = arguments[0]
            node = arguments[1]
            url = arguments[2]
            json = arguments[3]
            tag = arguments[4]
            cls.log(source, node.name, "tag=" + str(tag))
            if url == None:
                cls.log(source, node.name, "url=None")
            else:
                cls.log(source, node.name, url)
            if json == None:
                cls.log(source, node.name, "json=None")
            else:
                cls.log(source, node.name, json)
        elif arguments.__len__() == 3:
            if arguments[2] == None or type(arguments[2]) == str:
                source = arguments[0]
                tag = arguments[1]
                msg = arguments[2]
                if msg == None:
                    msg = "None"
                try:
                    Log.v(tag, msg)
                    SdApi._adapter.log(source, tag, msg, None)
                except Exception as ex:
                    print(traceback.format_exc())
            elif isinstance(arguments[2], Exception):
                # java实参有声明类型让函数重载时检测，但py无，但arguments[2]一定不为None因为try后面的except(Exception)里才调用本函数。
                source = arguments[0]
                tag = arguments[1]
                tr = arguments[2]
                try:
                    msg = str(tr)
                    if msg == "":
                        msg = "None"
                    Log.v(tag, msg)
                    SdApi._adapter.log(source, tag, msg, tr)
                except Exception as ex:
                    print(traceback.format_exc())

    @classmethod
    def set(cls, source, key, val):
        Log.v("SiteD.set:", key + "=" + val)
        SdApi._adapter.set(source, key, val)

    @classmethod
    def get(cls, source, key):
        temp = SdApi._adapter.get(source, key)
        Log.v("SiteD.get:", key + "=" + temp)
        return temp

    # -------------

    @classmethod
    def cacheRoot(cls):
        return SdApi._adapter.cacheRoot()

    # -------------

    @classmethod
    def createNode(cls, source, tagName):
        return SdApi._adapter.createNode(source, tagName)

    @classmethod
    def createNodeSet(cls, source, tagName):
        return SdApi._adapter.createNodeSet(source, tagName)

    @classmethod
    def buildHttpHeader(cls, cfg, url, header):
        SdApi._adapter.buildHttpHeader(cfg, url, header)


from .android_util_Log import Log
from .org_noear_sited_SdAdapter import SdAdapter  # 不能先引用，不然有循环依赖

SdApi._adapter = SdAdapter()
