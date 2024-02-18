# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-25
LastEditors:Do not edit
LastEditTime:2021-04-13
Description:
"""
import traceback
import json
from .org_noear_sited_SdSource import SdSource
from .android_util_Log import Log
from .org_noear_siteder_dao_engine_DdApi import DdApi
from .org_noear_siteder_dao_db_SiteDbApi import SiteDbApi
from .mytool import TextUtils
from .me_noear_utils_HttpUtil import HttpUtil
from .org_noear_siteder_dao_Session import Session


class DdSource(SdSource):
    # 是否为私密型插件
    def isPrivate(self):
        return self.attrs.getInt("private") > 0

    def tag(self, url):
        Log.v("tag.selct::", url)
        return self._tag.nodeMatch(url)
        # nodeMatch(url):_tag如果为SdNodeSet/DdNodeSet,返回匹配expr的tag节点SdNode/DdNode否则用这个source做空白SdNode/DdNode返回。_tag为SdNode/DdNode时返回自己。非空白SdNode/DdNode都有url属性(类型是SdValue)。下同

    def subtag(self, url):
        Log.v("subtag.selct::", url)
        return self._subtag.nodeMatch(url)

    def book(self, url):
        Log.v("book.selct::", url)
        return self._book.nodeMatch(url)

    def section(self, url):
        Log.v("section.selct::", url)
        return self._section.nodeMatch(url)

    def objectExt(self, url):
        Log.v("object.selct::", url)
        return self._objectExt.nodeMatch(url)

    def objectSlf(self, url):
        Log.v("object.selct::", url)
        return self._objectSlf.nodeMatch(url)

    def cover(self, url):
        Log.v("cover.selct::", url)
        return self._cover.nodeMatch(url)

    async def __new__(cls, app, xml):
        asyncInstance = object.__new__(cls)
        await asyncInstance.__init__(app, xml)
        return asyncInstance

    async def __init__(self, app, xml):
        #    public String sited
        # sited = xml
        await super().__init__(app, xml)
        self.ver = 0  # 版本号
        self.sds = None  # 插件平台服务
        self.vip = 0  # 是否为私密型插件
        self.logo = None  # 图标
        self.author = None
        self.contact = None
        self.alert = None  # 提醒（打开时跳出）
        self.intro = None  # 介绍
        # ---------------------------------------------------
        self.about = None
        # ---------------------------------------------------
        self.meta = None
        self.main = None
        self.hots = None
        self.updates = None
        self.search = None
        self.tags = None
        self.home = None
        self._tag = None
        self._subtag = None
        self._book = None
        self._section = None
        self._objectSlf = None
        self._objectExt = None
        self._cover = None
        self.login = None
        self.trace_url = None
        self._FullTitle = None
        self._isAlerted = False
        self.doInit(app, xml)
        if self.schema >= 1:
            self.xmlHeadName = "meta"
            self.xmlBodyName = "main"
            self.xmlScriptName = "script"
        else:
            self.xmlHeadName = "meta"
            self.xmlBodyName = "main"
            self.xmlScriptName = "jscript"
        await self.doLoad(app)
        self.meta = self.head
        self.main = self.body

        # --------------
        self.sds = self.head.attrs.getString("sds")
        self.ver = self.head.attrs.getInt("ver")
        self.vip = self.head.attrs.getInt("vip")
        self.author = self.head.attrs.getString("author")
        self.contact = self.head.attrs.getString("contact")
        self.intro = self.head.attrs.getString("intro")
        self.logo = self.head.attrs.getString("logo")
        if self.engine > DdApi.version():
            self.alert = "此插件需要更高版本引擎支持，否则会出错。建议升级！"
            print(self.alert)
        else:
            self.alert = self.head.attrs.getString("alert")
            if self.alert:
                print("alert节点消息：" + self.alert)

        #
        # ---------------------
        #
        self.trace_url = self.main.attrs.getString("trace")
        self.home = self.main.get("home")
        self.hots = self.home.get("hots")
        self.updates = self.home.get("updates")
        self.tags = self.home.get("tags")
        self.search = self.main.get("search")
        self._tag = self.main.get("tag")
        self._subtag = self.main.get("subtag")
        self._book = self.main.get("book")
        self._section = self.main.get("section")
        self._objectSlf = self.main.get("object")
        self._objectExt = self._objectSlf
        self._cover = self.main.get("cover")
        if self._objectExt.isEmpty():
            if self._section.isEmpty():
                self._objectExt = self._book
            else:
                self._objectExt = self._section
        if self.schema >= 1:
            self.login = self.head.get("login")  # 登录
            temp = self.head.get("reward")  # 打赏
            if temp.isEmpty():
                temp = self.head.get("about")  # 打赏
            self.about = temp
        else:
            self.login = self.main.get("login")  # 登录
            temp = self.main.get("reward")  # 打赏
            if temp.isEmpty():
                temp = self.main.get("about")  # 打赏
            self.about = temp
        # -----------
        json_ = {}
        Session.clear()  # Session是app相关配置，本脚本没数据所以清空
        json_["ver"] = DdApi.version()
        json_["udid"] = Session.udid()
        json_["uid"] = Session.userID
        json_["usex"] = Session.sex
        json_["uvip"] = Session.isVip
        json_["ulevel"] = Session.level
        jsCode = (
            "SiteD=" + json.dumps(json_) + ";SiteD.get=SdExt.get;SiteD.set=SdExt.set;"
        )
        self.loadJs(jsCode)

    def fullTitle(self):
        if self._FullTitle == None:
            if self.isPrivate():
                self._FullTitle = self.title
            else:
                idx = self.url.find("?")
                if idx < 0:
                    self._FullTitle = self.title + " (" + self.url + ")"
                else:
                    self._FullTitle = self.title + " (" + self.url[0:idx] + ")"
        return self._FullTitle

    def webUrl(self):
        if TextUtils.isEmpty(self.main.durl):
            return self.url
        else:
            return self.main.durl
        #     @Override

    def setCookies(self, cookies):
        if cookies == None:
            return
        Log.v("cookies", cookies)
        if self.DoCheck("", cookies, False):
            super().setCookies(cookies)
            SiteDbApi.setSourceCookies(self)

    #     @Override
    def cookies(self):
        if TextUtils.isEmpty(self._cookies):
            self._cookies = SiteDbApi.getSourceCookies(self)
        return self._cookies

    def isLoggedIn(self, url, cookies):
        return self.DoCheck(url, cookies, False)

    #     @Override
    def DoCheck(self, url, cookies, isFromAuto):
        if self.login.isEmpty():
            return True
        else:
            return self.login.doCheck(url, cookies, isFromAuto)

    #     @Override
    async def DoTraceUrl(self, url, args, config):
        if TextUtils.isEmpty(self.trace_url) == False:
            if TextUtils.isEmpty(url) == False:
                try:
                    data = {}
                    Session.clear()  # Session是app相关配置，本脚本没数据所以清空
                    data["_uid"] = str(Session.userID)
                    data["_uname"] = Session.nickname
                    data["_days"] = str(Session.dayNum)
                    data["_vip"] = str(Session.isVip)
                    data["url"] = url
                    data["args"] = args
                    data["node"] = config.name

                    def Act2(code, text):
                        pass

                    await HttpUtil.post(self.trace_url, data, Act2)
                except Exception as ex:
                    print(traceback.format_exc())

    @classmethod
    def isHots(cls, node):
        return "hots" == node.name

    @classmethod
    def isUpdates(cls, node):
        return "updates" == node.name

    @classmethod
    def isTags(cls, node):
        return "tags" == node.name

    @classmethod
    def isBook(cls, node):
        return "book" == node.name

    #
    # --------------------------
    #
    def tryAlert(self, activity, callback):
        if TextUtils.isEmpty(self.alert):
            return False
        else:
            if self._isAlerted == False:
                return True

    def tryAbout(self, FragmentBase_from):
        pass

    def tryLogin(self, activity, forUser):
        if self.login.isEmpty():
            return
        if self.login.isWebrun():
            loginUrl = self.login.getUrl(self.login.url.value)
            # Navigation.showWebAddinLogin(activity, self, loginUrl) #界面配置脚本不加载
        else:
            pass
