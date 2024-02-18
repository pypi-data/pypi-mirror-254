# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-22
LastEditors:Do not edit
LastEditTime:2021-01-21
Description:
"""
import re


class SdNode:
    def __init__(self, source):
        self._dtype = 0
        self._btype = 0
        self.attrs = SdAttributeList()
        self.name = None  # 节点名称
        self.key = None  # 自定义关键字
        self.title = None  # 标题
        self.txt = None  # txt#一用于item
        self.logo = None  # logo
        self.expr = None
        self.group = None
        self.lib = None
        self.btn = None
        self.update = 0
        # 可动态构建
        self.url = None  # url
        self.args = None
        self.referer = None
        self.cookie = None
        self.header = None  # http header 头需求: cookies|accept
        self.method = None  # http method
        self._encode = None  # http 编码
        self._ua = None  # http ua
        self.cache = 1  # 单位为秒(0不缓存；1不限时间)
        # parse
        self.onParse = None  # 解析函数
        self.onParseUrl = None  # 解析出真正在请求的Url
        # build
        # protected String buildArgs
        # protected String buildUrl
        # protected String buildReferer
        # protected String buildHeader
        # add prop for search or tag
        self.addCookie = None  # 需要添加的cookie
        self.addKey = None  # 需要添加的关键字
        self.addPage = 0  # 需要添加的页数值
        # ext prop (for post)
        self._isEmpty = False
        self._items = None
        self._adds = None
        self.source = source

    def OnDidInit(self):
        pass

    def dtype(self):
        if self._dtype > 0:
            return self._dtype
        else:
            return self.source.body.dtype()

    def btype(self):
        if self._btype > 0:
            return self._btype
        else:
            return self.dtype()

    def nodeType(self):
        return 1

    def nodeName(self):
        return self.name

    def nodeMatch(self, url):
        return self

    # @Override
    def isEmpty(self):
        return self._isEmpty

    def items(self):
        return self._items

    def adds(self):
        return self._adds

    # 是否有宏定义@key,@page
    def hasMacro(self):
        if self.url == None or self.url.find("@") < 0:
            return False
        else:
            return True

    # 是否有分页
    def hasPaging(self):
        return (
            self.hasMacro() or self.url.isEmptyBuild() == False or "post" == self.method
        )

    def isMatch(self, url):
        if TextUtils.isEmpty(self.expr) == False:
            pattern = re.compile(self.expr)
            return pattern.search(url)
        else:
            return False

    def isEquals(self, node):
        if self.name == None:
            return False
        return self.name == node.name

    def isInCookie(self):
        if self.header == None:
            return False
        else:
            return self.header.find("cookie") >= 0

    def isInReferer(self):
        if self.header == None:
            return False
        else:
            return self.header.find("referer") >= 0

    def hasItems(self):
        if self._items == None or self._items.__len__() == 0:
            return False
        else:
            return True

    def hasAdds(self):
        if self._adds == None or self._adds.__len__() == 0:
            return False
        else:
            return True

    def ua(self):
        if TextUtils.isEmpty(self._ua):
            return self.source.ua()
        else:
            return self._ua

    def encode(self):
        if TextUtils.isEmpty(self._encode):
            return self.source.encode()
        else:
            return self._encode

    # 获取cookies
    def buildCookies(self, url):
        cookies = self.source.cookies()
        attrs = SdAttributeList()
        attrs.set("url", url)
        attrs.set("cookies", "" if cookies == None else cookies)
        cookies = self.cookie.run(self.source, attrs, cookies)  # sdvalue的run方法
        if TextUtils.isEmpty(self.addCookie) == False:
            if TextUtils.isEmpty(cookies):
                cookies = (
                    self.addCookie
                    + "; Path=/; Domain="
                    + re.search(r"//([^/:]+)", url).group(1)
                )  # hostname
            else:
                cookies = self.addCookie + "  " + cookies
        if cookies == None:
            Log.i("cookies", "None")
        else:
            Log.i("cookies", cookies)
        return cookies

    def buildForNode(self, cfg):
        self._isEmpty = cfg == None
        if self._isEmpty == False:
            self.name = cfg.tag  # 默认为标签名
            nnMap = cfg.attrib.items()
            for [key, value] in nnMap:
                self.attrs.set(key, value)
            self._dtype = self.attrs.getInt("dtype")
            self._btype = self.attrs.getInt("btype")
            self.key = self.attrs.getString("key")
            self.title = self.attrs.getString("title")
            self.method = self.attrs.getString("method", "get")
            self.onParse = self.attrs.getString2("onParse", "parse")
            self.onParseUrl = self.attrs.getString2("onParseUrl", "parseUrl")
            self.txt = self.attrs.getString("txt")  #
            self.lib = self.attrs.getString("lib")
            self.btn = self.attrs.getString("btn")
            self.expr = self.attrs.getString("expr")
            self.update = self.attrs.getInt("update", 0)
            self._encode = self.attrs.getString("encode")
            self._ua = self.attrs.getString("ua")
            # book,section 特有
            self.addCookie = self.attrs.getString("addCookie")
            self.addKey = self.attrs.getString("addKey")
            self.addPage = self.attrs.getInt("addPage")
            self.buildDynamicProps()
            temp = self.attrs.getString("cache")
            if TextUtils.isEmpty(temp) == False:
                len = temp.__len__()
                if len == 1:
                    self.cache = int(temp)
                elif len > 1:
                    self.cache = int(temp[0 : len - 1])
                    p = temp[len - 1 :]
                    if p == "d":
                        self.cache = self.cache * 24 * 60 * 60
                    elif p == "h":
                        self.cache = self.cache * 60 * 60
                    elif p == "m":
                        self.cache = self.cache * 60
            if list(cfg).__len__():
                self._items = []
                self._adds = []
                NodeList_list = list(cfg)  # Returns all direct children
                for i in range(NodeList_list.__len__()):
                    n1 = NodeList_list[i]
                    if isinstance(n1.tag, str):
                        e1 = n1
                        tagName = e1.tag
                        if tagName == "item":
                            temp = SdApi.createNode(self.source, tagName).buildForItem(
                                e1, self
                            )
                            # temp是DdNode不用如java版向上向下转型，下同
                            self._items.append(temp)
                        elif e1.attrib.items().__len__():
                            temp = SdApi.createNode(self.source, tagName).buildForAdd(
                                e1, self
                            )
                            self._adds.append(temp)
                        else:
                            self.attrs.set(e1.tag, e1.text)
        self.OnDidInit()
        return self

    # item(不继承父节点)
    def buildForItem(self, cfg, p):
        nnMap = cfg.attrib.items()
        for [key, value] in nnMap:
            self.attrs.set(key, value)
        self.name = p.name
        self.url = self.attrs.getValue("url")  #
        self.key = self.attrs.getString("key")
        self.title = self.attrs.getString("title")  # 可能为None
        self.group = self.attrs.getString("group")
        self.txt = self.attrs.getString("txt")  #
        self.lib = self.attrs.getString("lib")
        self.btn = self.attrs.getString("btn")
        self.expr = self.attrs.getString("expr")
        self.logo = self.attrs.getString("logo")
        self._encode = self.attrs.getString("encode")
        return self

    # add (不继承父节点)
    def buildForAdd(self, cfg, p):
        # add不能有自己独立的url #定义为同一个page的数据获取(可能需要多个ajax)
        nnMap = cfg.attrib.items()
        for [key, value] in nnMap:
            self.attrs.set(key, value)
        self._dtype = self.attrs.getInt("dtype")
        self._btype = self.attrs.getInt("btype")
        self.name = cfg.tag  # 默认为标签名
        self.title = self.attrs.getString("title")
        # 可能为None
        self.key = self.attrs.getString("key")
        self.btn = self.attrs.getString("btn")
        self.txt = self.attrs.getString("txt")  #
        self.method = self.attrs.getString("method")
        self._encode = self.attrs.getString("encode")
        self._ua = self.attrs.getString("ua")
        self.buildDynamicProps()
        # --------
        self.onParse = self.attrs.getString2("onParse", "parse")
        self.onParseUrl = self.attrs.getString2("onParseUrl", "parseUrl")
        temp = self.attrs.getString("cache")  # py版增加适配多search节点搜索的cache
        if TextUtils.isEmpty(temp) == False:
            len = temp.__len__()
            if len == 1:
                self.cache = int(temp)
            elif len > 1:
                self.cache = int(temp[0 : len - 1])
                pp = temp[len - 1 :]
                if pp == "d":
                    self.cache = self.cache * 24 * 60 * 60
                elif pp == "h":
                    self.cache = self.cache * 60 * 60
                elif pp == "m":
                    self.cache = self.cache * 60
        return self

    def buildDynamicProps(self):
        self.url = self.attrs.getValue("url")
        self.args = self.attrs.getValue("args")
        self.header = self.attrs.getValue("header", "")
        self.referer = self.attrs.getValue("referer")
        self.cookie = self.attrs.getValue("cookie")
        if self.source.schema < 2:
            self.url.build = self.attrs.getString("buildUrl")
            self.args.build = self.attrs.getString("buildArgs")
            self.header.build = self.attrs.getString("buildHeader")
            self.referer.build = self.attrs.getString2("buildReferer", "buildRef")
            self.cookie.build = self.attrs.getString("buildCookie")

    #
    # =======================================
    #
    def getArgs(self, *arguments):
        len = arguments.__len__()
        if len == 3:
            url = arguments[0]
            key = arguments[1]
            page = arguments[2]
            atts = SdAttributeList()
            atts.set("url", url)
            if key != None:
                atts.set("key", key)
            atts.set("page", str(page))
            return self.args.run(self.source, atts)
        elif len == 2:
            url = arguments[0]
            data = arguments[1]
            atts = SdAttributeList()
            atts.set("url", url)
            if data != None:
                atts.set("data", Util.toJson(data))
            return self.args.run(self.source, atts)

    def getUrl(self, *arguments):
        len = arguments.__len__()
        if len == 0:
            atts = SdAttributeList()
            return self.url.run(self.source, atts)
        elif len == 1:
            url = arguments[0]
            atts = SdAttributeList()
            atts.set("url", url)
            return self.url.run(self.source, atts, url)
        elif len == 3:
            url = arguments[0]
            key = arguments[1]
            page = arguments[2]
            atts = SdAttributeList()
            atts.set("url", url)
            if key != None:
                atts.set("key", key)
            atts.set("page", str(page))
            return self.url.run(self.source, atts, url)
        elif len == 2:
            url = arguments[0]
            data = arguments[1]
            atts = SdAttributeList()
            atts.set("url", url)
            if data != None:
                atts.set("data", Util.toJson(data))
            return self.url.run(self.source, atts, url)

    def getReferer(self, url):
        atts = SdAttributeList()
        atts.set("url", url)
        return self.referer.run(self.source, atts, url)

    def getHeader(self, url):
        atts = SdAttributeList()
        atts.set("url", url)
        return self.header.run(self.source, atts)

    def getFullHeader(self, url):
        list = {}

        def HttpHeaderHandler(key, val):
            list[key] = val

        SdApi.buildHttpHeader(self, url, HttpHeaderHandler)
        return list

    def parse(self, url, html):
        if TextUtils.isEmpty(self.onParse):
            return html
        if "@null" == self.onParse:
            # 如果是@null，说明不需要通过js解析
            return html
        else:
            atts = SdAttributeList()
            atts.set("url", url)
            atts.set("html", html)
            return self.source.js.callJs(self.onParse, atts)

    def parseUrl(self, url, html):
        atts = SdAttributeList()
        atts.set("url", url)
        atts.set("html", html)
        temp = self.source.js.callJs(self.onParseUrl, atts)
        if temp == None:
            return ""
        else:
            return temp

    def isEmptyUrl(self):
        return self.url == None or self.url.isEmpty()

    def isEmptyHeader(self):
        return self.header == None or self.header.isEmpty()


from .org_noear_sited_SdAttributeList import SdAttributeList
from .mytool import TextUtils
from .org_noear_sited_SdApi import SdApi
from .org_noear_sited_Util import Util
from .android_util_Log import Log
