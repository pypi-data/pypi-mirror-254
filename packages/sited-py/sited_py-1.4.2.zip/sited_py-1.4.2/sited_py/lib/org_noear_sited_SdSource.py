# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-09-11 18:44:30
LastEditors:Do not edit
LastEditTime:2021-04-13
Description:
"""
import asyncio
import re
import traceback
from .android_util_Log import Log
from .org_noear_sited_Util import Util
from .org_noear_sited_SdAttributeList import SdAttributeList
from .mytool import TextUtils
from .org_noear_sited_SdApi import SdApi
from .org_noear_sited_SdNodeSet import SdNodeSet
from .org_noear_sited_SdNode import SdNode
from .org_noear_sited_JsEngine import JsEngine
from .org_noear_sited_SdJscript import SdJscript
from .org_noear_sited___AsyncTag import __AsyncTag as AsyncTag
from .org_noear_sited_DataContext import DataContext
from .org_noear_sited_HttpMessage import HttpMessage


class SdSource:
    def encode(self):
        return self._encode

    def ua(self):
        if TextUtils.isEmpty(self._ua):
            return Util.defUA
        else:
            return self._ua

    def cookies(self):
        return self._cookies

    def setCookies(self, cookies):
        self._cookies = cookies

    def delCache(self, key):
        Util.cache.delete(key)

    # --------------------------------
    async def __new__(cls, app, xml):
        asyncInstance = object.__new__(cls)
        await asyncInstance.__init__(app, xml)
        return asyncInstance

    async def __init__(self, app, xml):
        self.attrs = SdAttributeList()
        self.schema = 0
        self.isDebug = False  # 是否为调试模式
        self.engine = 0  # 引擎版本号
        self.url_md5 = None
        self.url = None  # 源首页
        self.title = None  # 标题
        self.expr = None  # 匹配源的表达式
        self._encode = None  # 编码
        self._ua = None
        self._cookies = None
        self.head = None
        self.body = None
        self.js = None  # 不能作为属性
        self.script = None
        self.root = None
        self.xmlBodyName = None
        self.xmlHeadName = None
        self.xmlScriptName = None
        if self.__class__ == SdSource:
            self.doInit(app, xml)
        self.xmlHeadName = "head"
        self.xmlBodyName = "body"
        self.xmlScriptName = "script"
        if self.__class__ == SdSource:
            await self.doLoad(app)

    def doInit(self, app, xml):
        Util.tryInitCache("app.getApplicationContext()")
        self.root = Util.getXmlroot(xml)  # root为根节点即插件里?xml的下一行。
        temp = self.root.attrib.items()
        for [key, value] in temp:
            self.attrs.set(key, value)  # 存储元素的属性
        temp = list(self.root)
        for i in range(temp.__len__()):
            p = temp[i]
            if isinstance(p.tag, str) and p.attrib.items().__len__() == 0:
                if list(p).__len__() == 0:
                    # 说明p是<title>xxx</title>这种元素类型
                    self.attrs.set(p.tag, p.text)
        self.schema = self.attrs.getInt("schema")
        self.engine = self.attrs.getInt("engine")
        self.isDebug = self.attrs.getInt("debug") > 0

    async def doLoad(self, app):
        self.xmlHeadName = self.attrs.getString("head", self.xmlHeadName)
        self.xmlBodyName = self.attrs.getString("body", self.xmlBodyName)
        self.xmlScriptName = self.attrs.getString("script", self.xmlScriptName)
        # 1.head
        self.head = SdApi.createNodeSet(self, self.xmlHeadName)
        # self.head = SdNodeSet(self)
        # 小心SdNode require循环
        self.head.buildForNode(Util.getElement(self.root, self.xmlHeadName))
        if self.schema >= 1:
            self.head.attrs.addAll(self.attrs)
        else:
            self.head.attrs = self.attrs  # 旧版本没有head，所以把当前属性让给head
        # 2.body
        self.body = SdApi.createNodeSet(self, self.xmlBodyName)
        # self.body = SdNodeSet(self) 小心require循环
        self.body.buildForNode(Util.getElement(self.root, self.xmlBodyName))
        self.title = self.head.attrs.getString("title")
        self.expr = self.head.attrs.getString("expr")
        self.url = self.head.attrs.getString("url")
        self.url_md5 = Util.md5(self.url)
        self._encode = self.head.attrs.getString("encode")
        self._ua = self.head.attrs.getString("ua")
        # ----------
        # 3.script :: 放后面
        #
        self.js = JsEngine(app, self)
        self.script = SdJscript(self, Util.getElement(self.root, self.xmlScriptName))
        await self.script.loadJs(app, self.js)
        self.root = None

    def DoCheck(self, url, cookies, isFromAuto):
        return True

    async def DoTraceUrl(self, url, args, config):
        pass

    #
    # ------------
    #
    def isMatch(self, url):
        pattern = re.compile(self.expr)
        return pattern.search(url)

    def loadJs(self, jsCode):
        self.js.loadJs(jsCode)

    def callJs(self, fun, attrs):
        return self.js.callJs(fun, attrs)

    # -------------
    def parse(self, config, url, html):
        Log.v("parse", url)
        Log.v("parse", "None" if html == None else html)
        temp = config.parse(url, html)
        if temp == None:
            Log.v("parse.rst", "None" + "\r\n\n")
        else:
            Log.v("parse.rst", temp + "\r\n\n")
        return temp

    def parseUrl(self, config, url, html):
        Log.v("parseUrl", url)
        Log.v("parseUrl", "None" if html == None else html)
        temp = config.parseUrl(url, html)
        if temp == None:
            return ""
        else:
            return temp

    #
    # ---------------------------------------
    #
    async def getNodeViewModel(self, *arguments):
        len = arguments.__len__()
        if len == 4:
            viewModel = arguments[0]
            nodeSet = arguments[1]
            isUpdate = arguments[2]
            callback = arguments[3]  # home节点
            tag = AsyncTag()
            dataContext = DataContext()
            asyncTasks = []
            for node in nodeSet.nodes():
                n = node
                asyncTasks.append(
                    asyncio.create_task(
                        self.doGetNodeViewModel2(
                            viewModel,
                            isUpdate,
                            tag,
                            n.url.value,
                            None,
                            n,
                            dataContext,
                            callback,
                        )
                    )
                )
            await asyncio.gather(*asyncTasks)  # python消息循环模型；并发home的子节点函数，回调统一返回。
            if tag.total == 0:
                await callback(1)
        elif len == 6:
            if type(arguments[3]) == int:
                viewModel = arguments[0]
                isUpdate = arguments[1]
                key = arguments[2]
                page = arguments[3]
                config = arguments[4]
                callback = arguments[5]  # search节点
                try:
                    tag = AsyncTag()
                    dataContext = DataContext()
                    await self.doGetNodeViewModel1(
                        viewModel,
                        isUpdate,
                        tag,
                        config.url.value,
                        key,
                        page,
                        config,
                        dataContext,
                        callback,
                    )
                except Exception as ex:
                    await callback(1)
            elif type(arguments[2]) == int:
                viewModel = arguments[0]
                isUpdate = arguments[1]
                page = arguments[2]
                url = arguments[3]
                config = arguments[4]
                callback = arguments[5]  # tag节点
                config.url.value = url
                tag = AsyncTag()
                dataContext = DataContext()
                await self.doGetNodeViewModel1(
                    viewModel,
                    isUpdate,
                    tag,
                    url,
                    None,
                    page,
                    config,
                    dataContext,
                    callback,
                )
            elif isinstance(arguments[3], SdNode):
                viewModel = arguments[0]
                isUpdate = arguments[1]
                url = arguments[2]
                config = arguments[3]
                args = arguments[4]
                callback = arguments[5]  # book、section节点
                # 需要对url进行转换成最新的格式（可能之前的旧的格式缓存）
                try:
                    # if (self.DoCheck(url, self.cookies(), True) == False):
                    # callback(99)
                    #     return
                    # python版说明：暂时要注释此判断，因为有login节点的插件对login.check为0的cookie判断DoCheck('', cookies, False)为假不能保存，后面self.cookies()就为None
                    tag = AsyncTag()
                    dataContext = DataContext()
                    await self.doGetNodeViewModel2(
                        viewModel,
                        isUpdate,
                        tag,
                        url,
                        args,
                        config,
                        dataContext,
                        callback,
                    )

                    if tag.total == 0:
                        await callback(1)
                except Exception as ex:
                    print(traceback.format_exc())
                    await callback(1)
        elif len == 5:
            viewModel = arguments[0]
            isUpdate = arguments[1]
            url = arguments[2]
            config = arguments[3]
            callback = arguments[4]  # book、section节点
            await self.getNodeViewModel(
                viewModel, isUpdate, url, config, None, callback
            )

    async def doGetNodeViewModel1(
        self, viewModel, isUpdate, tag, url, key, page, config, dataContext, callback
    ):
        # 适用于search/tag/subtag节点
        asyncTasks_doGetNodeViewModel1 = []
        msg = HttpMessage()
        page += config.addPage  # 加上增减量
        if key != None and TextUtils.isEmpty(config.addKey) == False:
            # 如果有补充关键字
            key = key + " " + config.addKey
        msg.url = config.getUrl(url, key, page)
        if TextUtils.isEmpty(msg.url) and config.hasAdds() == False:
            await callback(-3)
            return
        if TextUtils.isEmpty(msg.url) == False:
            msg.rebuild(config)
            if "post" == config.method:
                msg.rebuildForm(page, key)
            else:
                msg.url = msg.url.replace("@page", str(page))
                if key != None:
                    # 此时表示是get请求的search节点，只有它才有@key
                    msg.url = msg.url.replace("@key", Util.urlEncode(key, config))
            pageX = page
            keyX = key

            async def HttpCallback(code, sender, text, url302):
                asyncTasks = []
                tag.value += 1
                if code == 1:
                    if TextUtils.isEmpty(url302):
                        url302 = sender.url
                    if TextUtils.isEmpty(config.onParseUrl) == False:
                        # url需要解析出来(多个用;隔开)
                        # 当tag节点有parseUrl时，运行 doParseUrl_Aft 实现parse步骤直接return callback到本类的caller，否则运行 doParse_noAddin 实现parse步骤后回到本方法callback到本类的caller
                        newUrls = []
                        rstUrls = self.parseUrl(config, url302, text).split(";")
                        for url1 in rstUrls:
                            if url1.__len__() == 0:
                                continue
                            if url1.startswith(Util.NEXT_CALL):
                                SdApi.log(self, "CALL::url=", url1)
                                msg0 = HttpMessage()
                                msg0.url = (
                                    url1.replace(Util.NEXT_CALL, "")
                                    .replace("GET::", "")
                                    .replace("POST::", "")
                                )
                                msg0.rebuild(config)
                                if url1.find("POST::") > 0:
                                    msg0.method = "post"
                                    msg0.rebuildForm(pageX, keyX)
                                else:
                                    msg0.method = "get"
                                msg0.callback = msg.callback
                                tag.total += 1
                                asyncTasks.append(
                                    asyncio.create_task(Util.http(self, isUpdate, msg0))
                                )
                            else:
                                newUrls.append(url1)
                        if newUrls.__len__() > 0:
                            asyncTasks.append(
                                asyncio.create_task(
                                    self.doParseUrl_Aft(
                                        viewModel,
                                        config,
                                        isUpdate,
                                        newUrls,
                                        sender.form,
                                        tag,
                                        dataContext,
                                        callback,
                                    )
                                )
                            )
                        await asyncio.gather(*asyncTasks)
                        if asyncTasks.__len__() == 0 and tag.total == tag.value:
                            await callback(-2)  # parseUrl函数出错时，引擎这样处理来退出
                        return
                    else:
                        self.doParse_noAddin(viewModel, config, url302, text)
                if tag.total == tag.value:
                    await callback(code)

            msg.callback = HttpCallback
            tag.total += 1
            asyncTasks_doGetNodeViewModel1.append(
                asyncio.create_task(Util.http(self, isUpdate, msg))
            )
        if config.hasAdds():
            # 2.2 获取副内容（可能有多个）
            for n1 in config.adds():
                if n1.isEmptyUrl():
                    continue
                urlA = n1.url.getValue(url)
                asyncTasks_doGetNodeViewModel1.append(
                    asyncio.create_task(
                        self.doGetNodeViewModel1(
                            viewModel,
                            isUpdate,
                            tag,
                            urlA,
                            key,
                            page,
                            n1,
                            dataContext,
                            callback,
                        )
                    )
                )
        await asyncio.gather(*asyncTasks_doGetNodeViewModel1)

    async def doGetNodeViewModel2(
        self, viewModel, isUpdate, tag, url, args, config, dataContext, callback
    ):
        # 适用于hots/updates/tags/book[1-7]/section等节点，他们的args都是None，还有book[8]，它args是开发指南说的输入框{'输入框id': '[book8]id对应输入值'}。不适用search/tag/subtag节点，
        # 需要对url进行转换成最新的格式（可能之前的旧的格式缓存）
        asyncTasks_doGetNodeViewModel2 = []
        if config.isEmpty():
            return
        if config.hasItems() and TextUtils.isEmpty(config.onParse):
            viewModel.loadByConfig(config)
        if "@null" == config.method:
            url2 = config.getUrl(url, args)
            if TextUtils.isEmpty(config.onParse):
                viewModel.loadByJson(config, url2)
            else:
                viewModel.loadByJson(
                    config, self.parse(config, url2, Util.toJson(args))
                )
            return
        if (
            TextUtils.isEmpty(config.onParse) == False
            and TextUtils.isEmpty(url) == False
        ):
            # 如果没有url 和 parse，则不处理
            msg = HttpMessage()
            # 为doParseUrl_Aft服务(要在外围)
            # Map<Integer, String> dataList = HashMap<>();#如果有多个地址，需要排序
            # 2.获取主内容
            msg.url = config.getUrl(url, args)
            # 有缓存的话，可能会变成同步了
            msg.rebuild(config)
            msg.rebuildForm(args)

            async def HttpCallback(code, sender, text, url302):
                asyncTasks = []
                tag.value += 1
                if code == 1:
                    if TextUtils.isEmpty(url302):
                        url302 = sender.url
                    if TextUtils.isEmpty(config.onParseUrl) == False:
                        # 当hots/updates/tags节点有parseUrl时，运行 doParseUrl_Aft 实现parse步骤直接return callback到本类的caller，否则运行 doParse_hasAddin 实现parse步骤后回到本方法callback到本类的caller
                        # url需要解析出来(多个用;隔开)
                        newUrls = []
                        rstUrls = self.parseUrl(config, url302, text).split(";")
                        for url1 in rstUrls:
                            if url1.__len__() == 0:
                                continue
                            if url1.startswith(Util.NEXT_CALL):
                                SdApi.log(self, "CALL::url=", url1)
                                msg0 = HttpMessage()
                                msg0.url = (
                                    url1.replace(Util.NEXT_CALL, "")
                                    .replace("GET::", "")
                                    .replace("POST::", "")
                                )
                                msg0.rebuild(config)
                                if url1.find("POST::") > 0:
                                    msg0.method = "post"
                                    msg0.rebuildForm(args)
                                else:
                                    msg0.method = "get"
                                msg0.callback = msg.callback
                                tag.total += 1
                                asyncTasks.append(
                                    asyncio.create_task(Util.http(self, isUpdate, msg0))
                                )
                            else:
                                newUrls.append(url1)
                        if newUrls.__len__() > 0:
                            asyncTasks.append(
                                asyncio.create_task(
                                    self.doParseUrl_Aft(
                                        viewModel,
                                        config,
                                        isUpdate,
                                        newUrls,
                                        args,
                                        tag,
                                        dataContext,
                                        callback,
                                    )
                                )
                            )
                        await asyncio.gather(*asyncTasks)
                        if asyncTasks.__len__() == 0 and tag.total == tag.value:
                            await callback(-2)  # parseUrl函数出错时，引擎这样处理来退出
                        return  # 下面的代码被停掉
                    else:
                        self.doParse_hasAddin(viewModel, config, url302, text)
                if tag.total == tag.value:
                    await callback(code)

            msg.callback = HttpCallback
            tag.total += 1
            asyncTasks_doGetNodeViewModel2.append(
                asyncio.create_task(Util.http(self, isUpdate, msg))
            )
        if config.hasAdds():
            # 2.2 获取副内容（可能有多个）
            for n1 in config.adds():
                if n1.isEmptyUrl():
                    continue
                urlA = n1.url.getValue(url)
                asyncTasks_doGetNodeViewModel2.append(
                    asyncio.create_task(
                        self.doGetNodeViewModel2(
                            viewModel,
                            isUpdate,
                            tag,
                            urlA,
                            args,
                            n1,
                            dataContext,
                            callback,
                        )
                    )
                )
        await asyncio.gather(*asyncTasks_doGetNodeViewModel2)

    async def doParseUrl_Aft(
        self, viewModel, config, isUpdate, newUrls, args, tag, dataContext, callback
    ):
        asyncTasks = []
        # tag.num += newUrls.__len__()
        for newUrl2 in newUrls:

            async def asyncLoopGetI(newUrl2):
                tag.total += 1
                # tag.num -= 1
                msg = HttpMessage(config, newUrl2, tag.total, args)

                async def HttpCallback(code2, sender, text2, url302):
                    tag.value += 1
                    if code2 == 1:
                        if TextUtils.isEmpty(url302):
                            url302 = newUrl2
                        self.doParse_noAddinForTmp(
                            dataContext, config, url302, text2, sender.tag
                        )
                    if tag.total == tag.value:
                        for cfg in dataContext.nodes():
                            dataList = dataContext.get(cfg)
                            jsonList = []
                            for i in range(1, tag.total + 1):
                                # 按排序加载内容！不是安
                                if dataList.has(i):
                                    jsonList.append(dataList.get(i))
                            strAry = jsonList
                            viewModel.loadByJson(cfg, strAry)
                        await callback(code2)

                msg.callback = HttpCallback
                asyncTasks.append(asyncio.create_task(Util.http(self, isUpdate, msg)))

            await asyncLoopGetI(newUrl2)
        await asyncio.gather(*asyncTasks)

    def doParse_noAddin(self, viewModel, config, url, text):
        json_ = self.parse(config, url, text)
        if self.isDebug:
            SdApi.log(self, config, url, json_, 0)
        if json_ != None:
            viewModel.loadByJson(config, json_)

    def doParse_hasAddin(self, viewModel, config, url, text):
        json_ = self.parse(config, url, text)
        if self.isDebug:
            SdApi.log(self, config, url, json_, 0)
        if json_ != None:
            viewModel.loadByJson(config, json_)
            if config.hasAdds():
                # 没有url的add
                for n2 in config.adds():
                    # 有buildUrl的sections要continue
                    if n2.isEmptyUrl() == False:
                        continue
                    json2 = self.parse(n2, url, text)
                    if self.isDebug:
                        SdApi.log(self, n2, url, json2, 0)
                    if json2 != None:
                        viewModel.loadByJson(n2, json2)

    def doParse_noAddinForTmp(self, dataContext, config, url, text, tag):
        json_ = self.parse(config, url, text)
        if self.isDebug:
            SdApi.log(self, config, url, json_, tag)
        if json_ != None:
            dataContext.add(config, tag, json_)
