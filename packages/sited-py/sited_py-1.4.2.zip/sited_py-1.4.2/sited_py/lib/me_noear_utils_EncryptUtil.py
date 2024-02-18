# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-04
LastEditors:Do not edit
LastEditTime:2020-05-24
Description:
"""
import hashlib
import traceback


class EncryptUtil:
    # 生成MD5值
    @classmethod
    def md5(cls, code):
        s = None
        try:
            s = hashlib.md5(code.encode(encoding="UTF-8")).hexdigest()
        except Exception as e:
            print(traceback.format_exc())
        return s

    # 生成sha1值
    @classmethod
    def sha1(cls, code):
        return None
