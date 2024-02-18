# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-06
LastEditors:Do not edit
LastEditTime:2021-09-21
Description:
"""
import re
import asyncio
import traceback
import hashlib
import urllib.parse
import aiohttp
from lxml import etree


class Util:
    @classmethod
    def tryInitCache(cls, context):
        if Util.cache == None:
            Util.cache = FileCache(context, "sited")

    @classmethod
    def getElement(cls, n, tag):
        temp = n.findall(".//" + tag)
        if temp.__len__() > 0:
            return temp[0]
        else:
            return None

    @classmethod
    def getXmlroot(cls, xml):
        root = etree.fromstring(xml.encode())
        return root

    # ----------------------------
    @classmethod
    def urlEncode(cls, str, config):
        try:
            return charset_encodeURIComponent(str, config.encode()).replace("%20", "+")
            # java版是java.net.URLEncoder.encode（可指定字符集），编码遵循application/x-www-form-urlencoded标准，会将空格编码成加号，其余字符接近用encodeURIComponent处理而不是encodeURI
        except Exception as ex:
            return ""

    @classmethod
    async def http(cls, source, isUpdate, msg):
        SdApi.log(source, "Util.http", msg.url)
        cacheKey2 = None
        args = ""
        if msg.form == None:
            cacheKey2 = msg.url
        else:
            sb = []
            sb.append(msg.url)
            for key in msg.form.keys():
                sb.extend([key, "=", msg.form.get(key), " "])

            cacheKey2 = "".join(sb)
            args = cacheKey2
        cacheKey = cacheKey2
        block = Util.cache.get(cacheKey)
        if isUpdate == False and msg.config.cache > 0:
            if block != None and block.isOuttime(msg.config) == False:
                block1 = block
                # java版用Handler().postDelayed延迟，才能满足对异步请求的回调顺序控制
                async def postDelayed():
                    SdApi.log(source, "Util.incache.url", msg.url)
                    await msg.callback(1, msg, block1.value, None)

                await asyncio.sleep(0.1)
                asyncTasks = []
                asyncTasks.append(asyncio.create_task(postDelayed()))
                await asyncio.gather(*asyncTasks)
                return

        async def HttpCallback(code, msg2, data, url302):
            if code == 1:
                Util.cache.save(cacheKey, data)
            await msg.callback(code, msg2, data, url302)

        await cls.doHttp(source, msg, block, HttpCallback)
        await source.DoTraceUrl(msg.url, args, msg.config)

    @classmethod
    async def doHttp(cls, source, msg, cache, callback):
        # java版是用 synchronized doHttp请求，python是异步请求库
        options = {
            "headers": {"User-Agent": msg.ua},
            "allow_redirects": False,
            "ssl": False,
        }
        isUrlEncodingEnabled = False
        if msg.url.find(" ") > 0:
            # java版 >0 会影响com.loopj.android.http.AsyncHttpClient类的getUrlWithQueryString(boolean shouldEncodeUrl
            isUrlEncodingEnabled = True

        for key in msg.header.keys():
            options["headers"][key] = msg.header.get(key)

        httpTag = AsyncTag()

        async def responseHandler(response):
            statusCode = response.status
            if (
                statusCode == 302
                or statusCode == 301
                or statusCode == 303
                or statusCode == 307
            ):
                lastHttpTagStr0 = httpTag.str0
                httpTag.str0 = response.headers["location"]
                if httpTag.str0.startswith("http") == False:
                    uri = {
                        "protocol": re.search(r"(^.+?)//", msg.url).group(1),
                        "hostname": re.search(r"//([^/:]+)", msg.url).group(1),
                        "pathname": re.search(r"//[^/]+(/[^?#]*)", msg.url).group(1)
                        if re.search(r"//[^/]+(/[^?#]*)", msg.url)
                        else "/",
                    }
                    if httpTag.str0.startswith("/"):
                        httpTag.str0 = (
                            uri["protocol"] + "//" + uri["hostname"] + httpTag.str0
                        )
                    else:
                        path = uri["pathname"]
                        idx = path.rfind("/")
                        if idx > 0:
                            path = path[0:idx]
                            httpTag.str0 = (
                                uri["protocol"]
                                + "//"
                                + uri["hostname"]
                                + path
                                + "/"
                                + httpTag.str0
                            )

                if options["headers"].get("Content-type"):
                    options["headers"].pop("Content-type")
                if statusCode == 302 or statusCode == 301:
                    Log.v("orgurl", msg.url)
                    Log.v("302url", httpTag.str0)
                    async with aiohttp.ClientSession() as cls.session:
                        async with cls.session.get(httpTag.str0, **options) as resp:
                            await responseHandler(resp)
                elif statusCode == 303 or statusCode == 307:
                    location = httpTag.str0
                    httpTag.str0 = lastHttpTagStr0
                    async with aiohttp.ClientSession() as cls.session:
                        async with cls.session.get(location, **options) as resp:
                            await responseHandler(resp)
            elif statusCode < 200 or statusCode > 299:
                print(
                    "http.onFailure:: "
                    + (httpTag.str0 or msg.url)
                    + " status code: "
                    + str(statusCode)
                )
                SdApi.log(
                    source,
                    "http.onFailure",
                    Exception(
                        (httpTag.str0 or msg.url) + " status code: " + str(statusCode)
                    ),
                )
                if cache == None or cache.value == None:
                    await callback(-2, msg, None, None)
                else:
                    await callback(1, msg, cache.value, httpTag.str0)
            else:
                sb = []
                if response.headers:
                    for [Name, Value] in response.headers.items():
                        if "Set-Cookie".upper() == Name.upper():
                            sb.extend([re.search(r"[^;]+", Value).group(0), ";"])
                if sb.__len__() > 0:
                    source.setCookies("".join(sb)[0:-1])  # 删除尾部分号
                data = await response.text(msg.encode)
                await callback(1, msg, data, httpTag.str0)

        try:
            idx = msg.url.find("#")  # 去除hash，即#.*
            url2 = None
            if idx > 0:
                url2 = msg.url[0:idx]
            else:
                url2 = msg.url
            if isUrlEncodingEnabled:
                try:
                    url2 = urllib.parse.unquote(url2.replace("+", " "))
                    url2 = urllib.parse.quote(url2, "-._~:/?#[]@!$&'()*+,;=")
                except Exception:
                    pass
            if "post" == msg.method:
                postData = []
                for [key, value] in msg.form.items():
                    postData.append(
                        charset_encodeURIComponent(key, msg.encode).replace("%20", "+")
                        + "="
                        + charset_encodeURIComponent(value, msg.encode).replace(
                            "%20", "+"
                        )
                    )
                    # converting a String to the application/x-www-form-urlencoded MIME format，空格转义为加号
                postData = "&".join(postData)
                print("发出post参数（x-www-form-urlencoded编码） " + postData)
                options["headers"]["Content-type"] = "application/x-www-form-urlencoded"
                async with aiohttp.ClientSession() as cls.session:
                    async with cls.session.post(url2, data=postData, **options) as resp:
                        await responseHandler(resp)
            else:
                async with aiohttp.ClientSession() as cls.session:
                    async with cls.session.get(url2, **options) as resp:
                        await responseHandler(resp)
        except Exception as ex:
            print(
                (httpTag.str0 or msg.url)
                + " 异常如下，错误消息见生成的sited_error.txt文件和sited_log.txt等"
            )
            print(traceback.format_exc().splitlines()[-1])
            SdApi.log(source, "http.onFailure", ex)
            if cache == None:
                await callback(-2, msg, None, None)
            else:
                await callback(1, msg, cache.value, None)

    # 生成MD5值
    @classmethod
    def md5(cls, code):
        s = None
        try:
            s = hashlib.md5(code.encode(encoding="UTF-8")).hexdigest()
        except Exception as e:
            print(traceback.format_exc())
        return s

    # -------------
    @classmethod
    def toJson(cls, data):
        sb = []
        if data != None:
            sb.append("{")
            for k in data.keys():
                v = data.get(k)
                sb.extend(['"', k, '"', ":"])
                if v.startswith("{"):
                    # 表示v是对象
                    sb.append(v)
                else:
                    cls._WriteValue(sb, v)
                sb.append(",")
            if sb.__len__() > 4:
                sb.pop()
            sb.append("}")
        else:
            sb.append("{}")

        return "".join(sb)

    @classmethod
    def _WriteValue(cls, _Writer, val):
        if val == None:
            _Writer.append("None")
        else:
            _Writer.append('"')
            n = val.__len__()
            for i in range(n):
                c = val[i]
                if c == "\\":
                    _Writer.append("\\\\")  # 20110809
                elif c == '"':
                    _Writer.append(
                        '\\"'
                    )  # json的key、value用双引号包裹，所以被包裹字符串里要反斜杠转义双引号，还要反斜杠之前再加反斜杠将其转义以防止eval时它被用于转义
                elif c == "\n":
                    _Writer.append("\\n")
                elif c == "\r":
                    _Writer.append("\\r")
                elif c == "\t":
                    _Writer.append("\\t")
                elif c == "\f":
                    _Writer.append("\\f")
                elif c == "\b":
                    _Writer.append("\\b")
                else:
                    _Writer.append(c)
            _Writer.append('"')


Util.NEXT_CALL = "CALL::"
Util.defUA = "Mozilla/5.0 (Windows NT 10.0  Win64  x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"
Util.cache = None
# 末尾放import，解决2个模块循环依赖问题
from .android_util_Log import Log
from .org_noear_sited_SdApi import SdApi
from .org_noear_sited___AsyncTag import __AsyncTag as AsyncTag
from .org_noear_sited___FileCache import __FileCache as FileCache


def charset_encodeURI(str, charset="utf-8"):
    return urllib.parse.quote(str, "-._~:/?#[]@!$&'()*+,;=", charset)


def charset_encodeURIComponent(str, charset="utf-8"):
    # in accordance with RFC5987
    return urllib.parse.quote(str, "-._~!", charset)


def charset_decodeURIComponent(str, charset="utf-8"):
    return urllib.parse.unquote(str, charset)

