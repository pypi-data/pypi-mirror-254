# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-12
LastEditors:Do not edit
LastEditTime:2021-03-16
Description:
"""
import traceback
import os
from datetime import datetime
from .org_noear_sited_SdApi import SdApi
from .org_noear_sited___CacheBlock import __CacheBlock as CacheBlock


class __FileCache:
    def __init__(self, context, block):
        _root = SdApi.cacheRoot()  # None
        #         if (_root == None) :
        #             _root = context.getExternalFilesDir(None)
        #         if (_root == None) :
        #             _root = context.getFilesDir()
        if _root == None:
            _root = os.path.join(
                os.path.dirname(os.path.realpath(__file__)), "..", "files"
            )
        if not os.path.exists(_root):
            os.mkdir(_root)
        self.dir = os.path.join(_root, block)  # java版是file文件（夹），python改为文件（夹）路径
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)

    def getFile(self, key):
        key_md5 = Util.md5(key)
        String_path = key_md5[0:2]
        dir2 = os.path.join(self.dir, String_path)
        if os.path.exists(dir2) == False:
            os.mkdir(dir2)
        return os.path.join(dir2, key_md5)  # java版是返回文件对象，py版返回文件路径

    def save(self, key, data):
        if not getattr(sited_py.conf, "enableFileCache", False):
            return  # 参数在sited_py/conf.py设置
        file = self.getFile(key)
        try:
            with open(file, "w", encoding="utf-8") as fs:
                fs.write(data)
        except Exception as ex:
            print(traceback.format_exc())

    def get(self, key):
        file = self.getFile(key)  # java版是返回文件对象，py版返回文件路径
        if os.path.exists(file) == False:
            return None
        else:
            try:
                block = CacheBlock()
                block.value = self.toString(file)
                block.time = datetime.fromtimestamp(os.stat(file).st_mtime)
                return block
            except Exception as ex:
                print(traceback.format_exc())
                return None

    def delete(self, key):
        file = self.getFile(key)
        if os.path.exists(file):
            os.remove(file)  # 只能删除文件。

    def isCached(self, key):
        file = self.getFile(key)
        return os.path.exists(file)

    # --------
    @classmethod
    def toString(cls, file_is):
        read_in = open(file_is, "r", encoding="utf-8")
        return cls.doToString(read_in)

    @classmethod
    def doToString(cls, read_in):
        buffer = []
        for line in read_in:
            buffer.append(line.splitlines()[0] if line.splitlines() else "")
            buffer.append("\r\n")
        read_in.close()
        return "".join(buffer)


from .org_noear_sited_Util import Util
import sited_py.conf
