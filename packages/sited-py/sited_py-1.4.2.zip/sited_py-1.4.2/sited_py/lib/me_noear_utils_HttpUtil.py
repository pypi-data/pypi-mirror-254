# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-06-05
LastEditors:Do not edit
LastEditTime:2021-01-20
Description:
"""
import re
import urllib.parse
import aiohttp


class HttpUtil:
    #  发起get请求，并返回String结果
    @classmethod
    async def get(cls, *arguments):
        len = arguments.__len__()
        if len == 2:
            url = arguments[0]
            callback = arguments[1]
            cls.get(url, None, callback)
        elif len == 3:
            url = arguments[0]
            params = arguments[1]
            callback = arguments[2]
            cls.get(None, url, params, callback)
        elif len == 4:
            header = arguments[0]
            url = arguments[1]
            params = arguments[2]
            callback = arguments[3]
            getData = []
            if params != None:
                for [k, v] in params.items():
                    getData.append(
                        urllib.parse.quote(k, "-._~!")
                        + "="
                        + urllib.parse.quote(v, "-._~!")
                    )
                url = re.sub(r"\?$", "", url) + "?" + "&".join(getData)

            options = {"allow_redirects": True, "ssl": False}
            if header != None and header.__len__() > 0:
                for key in header.keys():
                    options["headers"][key] = header.get(key)

            # java版 AsyncHttpClient.get的null是android.content.Context
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    urllib.parse.quote(url, "-._~:/?#[]@!$&'()*+,;="), **options
                ) as resp:
                    if resp.status < 200 or resp.status > 299:
                        callback(-2, None)
                    else:
                        s = await resp.text("utf8")
                        if s == None:
                            callback(-1, s)
                        else:
                            callback(1, s)

    # 发起post请求，并返回String结果
    @classmethod
    async def post(cls, url, params, callback):
        postData = {}
        for [key, value] in params.items():
            postData[urllib.parse.quote(key, "-._~!")] = urllib.parse.quote(
                value, "-._~!"
            )
        options = {"allow_redirects": True, "ssl": False}
        # java版 AsyncHttpClient.post的null是android.content.Context
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=postData, **options) as resp:
                if resp.status < 200 or resp.status > 299:
                    callback(-2, None)
                else:
                    s = await resp.text("utf8")
                    if s == None:
                        callback(-1, s)
                    else:
                        callback(1, s)
