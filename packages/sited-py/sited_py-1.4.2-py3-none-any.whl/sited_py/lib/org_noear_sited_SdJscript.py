# -*- coding: UTF-8 -*-
"""
Author:wistn
since:Do not edit
LastEditors:Do not edit
LastEditTime:2021-03-16
Description:
"""
import os
import re
from .org_noear_sited_Util import Util
from .mytool import TextUtils
from .org_noear_sited_SdNode import SdNode
from .android_util_Log import Log
from .org_noear_sited_HttpMessage import HttpMessage


class SdJscript:
    def __init__(self, source, node):
        self.require = None
        self.code = None
        self.s = source
        if node == None:
            self.code = ""
            self.require = SdNode(source).buildForNode(None)
        else:
            self.code = Util.getElement(node, "code").text
            self.require = SdNode(source).buildForNode(Util.getElement(node, "require"))

    async def loadJs(self, app, js):
        if self.require.isEmpty() == False:
            for n1 in self.require.items():
                # 1.如果本地可以加载并且没有出错
                if TextUtils.isEmpty(n1.lib) == False:
                    if self.loadLib(app, js, n1.lib):
                        continue
                # 2.尝试网络加载
                Log.v("SdJscript", n1.url.value)
                if n1.cache == 0:
                    n1.cache = 1  # 长久缓存js文件 //默认长久缓存
                msg = HttpMessage(n1, n1.url.value)

                async def HttpCallback(code, sender, text, url302):
                    if code == 1:
                        js.loadJs(text)

                msg.callback = HttpCallback
                await Util.http(self.s, False, msg)
                # java版是异步请求Http，所以插件运行时第一次调用网络库失败，但后面会缓存到sited文件夹，再刷新主进程就行了因为第二次自动改为从sited文件夹缓存同步读取库代码。python版也是
        if TextUtils.isEmpty(self.code) == False:
            js.loadJs(self.code)
            # 预加载插件script/code(兼容旧格式jscript/code)节点即js代码部分

    # ---------------------
    #
    def loadLib(self, app, js, lib):
        # for debug
        # Resources asset = app.getResources()
        asset = os.path.dirname(os.path.realpath(__file__))
        if lib == "md5":
            return SdJscript.tryLoadLibItem(asset, "R.raw.md5", js)
        elif lib == "sha1":
            return SdJscript.tryLoadLibItem(asset, "R.raw.sha1", js)
        elif lib == "base64":
            return SdJscript.tryLoadLibItem(asset, "R.raw.base64", js)
        elif lib == "cheerio":
            return SdJscript.tryLoadLibItem(asset, "R.raw.cheerio", js)
        else:
            return False

    @classmethod
    def tryLoadLibItem(cls, asset, resID, js):
        try:
            file_is = os.path.join(
                asset, "main_res_raw_" + re.search(r"[^.]+$", resID).group(0) + ".js"
            )
            read_in = open(file_is, "r", encoding="utf-8")
            code = cls.doToString(read_in)
            js.loadJs(code)
            return True
        except Exception as ex:
            return False

    @classmethod
    def doToString(cls, read_in):
        buffer = []
        for line in read_in:
            buffer.append(line.splitlines()[0] if line.splitlines() else "")
            buffer.append("\r\n")
        # 要加换行符，不然库文件只有一行会被双斜杠注释破坏
        read_in.close()
        return "".join(buffer)

