# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-10-05
LastEditors:Do not edit
LastEditTime:2020-10-06
Description:
"""
import base64


class Base64Util:
    @classmethod
    def encode(cls, text):
        return base64.b64encode(text.encode("UTF-8"))

    @classmethod
    def decode(cls, code):
        temp = base64.b64decode(code)
        return temp.decode("UTF-8")

