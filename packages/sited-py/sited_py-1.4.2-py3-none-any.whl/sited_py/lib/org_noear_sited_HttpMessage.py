# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-25
LastEditors:Do not edit
LastEditTime:2021-01-02
Description:
"""
from .org_noear_sited_SdApi import SdApi
from .mytool import TextUtils
from .android_util_Log import Log


class HttpMessage:
    def __init__(self, *arguments):
        self.header = {}
        self.form = {}
        self.url = None
        self.tag = 0
        self.callback = None
        self.config = None

        # 可由cfg实始化
        self.encode = None
        self.ua = None
        self.method = None
        len = arguments.__len__()
        if len == 0:
            pass
        elif len == 4:
            cfg = arguments[0]
            url = arguments[1]
            tag = arguments[2]
            args = arguments[3]
            self.config = cfg
            self.url = url
            self.tag = tag
            if args != None:
                self.form = args
            self.rebuild(None)
        elif len == 2:
            cfg = arguments[0]
            url = arguments[1]
            self.config = cfg
            self.url = url
            self.rebuild(None)

    def rebuild(self, cfg):
        if cfg != None:
            self.config = cfg
        self.ua = self.config.ua()
        self.encode = self.config.encode()
        self.method = self.config.method

        def HttpHeaderHandler(key, val):
            self.header[key] = val

        SdApi.buildHttpHeader(self.config, self.url, HttpHeaderHandler)

    def rebuildForm(self, *arguments):
        len = arguments.__len__()
        if len == 1:
            data = arguments[0]
            self.doBuildForm(True, 0, None, data)
        elif len == 2:
            page = arguments[0]
            key = arguments[1]
            self.doBuildForm(False, page, key, None)

    def doBuildForm(self, isData, page, key, data):
        if "post" == self.config.method:
            _strArgs = None
            if isData == False:
                _strArgs = self.config.getArgs(self.url, key, page)
            else:
                _strArgs = self.config.getArgs(self.url, data)
            if TextUtils.isEmpty(_strArgs) == False:
                Log.v("Post.Args", _strArgs)
                for kv in _strArgs.split(";"):
                    if kv.__len__() > 3:
                        name = kv.split("=")[0]
                        value = kv.split("=")[1]
                        if value == "@key":
                            self.form[name] = key
                        elif value == "@page":
                            self.form[name] = str(page)
                        else:
                            self.form[name] = value
