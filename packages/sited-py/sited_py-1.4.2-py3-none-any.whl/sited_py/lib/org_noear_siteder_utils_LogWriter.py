# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-16
LastEditors:Do not edit
LastEditTime:2021-03-16
Description: 保存文件编码是utf-8
"""
import os
from datetime import datetime
import traceback
import re


class LogWriter:
    def __init__(self, dir, fileName):
        self.mWriter = None
        self.df = None
        file = os.path.join(dir, fileName)  # java版是file文件（夹），python改为文件路径
        try:
            # mWriter = new BufferedWriter(new FileWriter(file, true), 2048);
            self.mWriter = open(file, "a")  # 不会自动关闭文件除非tryClose或退出程序
            self.df = type(
                "SimpleDateFormat",
                (),
                {"format": lambda d: d.strftime("[%y-%m-%d %H:%M:%S]: ")},
            )
        except Exception as ex:
            self.mWriter = None
            print(traceback.format_exc())

    @classmethod
    def tryInit(cls):
        if LogWriter.loger == None:
            # File _root = Setting.getFileRoot()
            _root = os.path.join(
                os.path.dirname(os.path.realpath(__file__)), "..", "files"
            )
            LogWriter.loger = LogWriter(_root, "sited_log.txt")
            LogWriter.error = LogWriter(_root, "sited_error.txt")
            LogWriter.jsprint = LogWriter(_root, "sited_print.txt")

    @classmethod
    def tryClose(cls):
        if LogWriter.loger != None:
            LogWriter.loger.close()
            LogWriter.error.close()
            LogWriter.jsprint.close()
            LogWriter.loger = None
            LogWriter.error = None
            LogWriter.jsprint = None

    def close(self):
        if self.mWriter == None:
            return
        try:
            self.mWriter.close()
            self.df = None
            self.mWriter = None
        except Exception as ex:
            print(traceback.format_exc())

    def print(self, tag, msg, tr):
        if self.mWriter == None:
            return
        try:
            self.mWriter.write(self.df.format(datetime.now()))
            self.mWriter.write("\r\n")
            self.mWriter.write(tag)
            self.mWriter.write("::")
            self.mWriter.write(msg)
            if tr != None:
                self.mWriter.write("\r\n")
                list = re.split(
                    r"\r?\n(?=\s+File)", re.sub(r"\n.+?\n$", "", traceback.format_exc())
                )[-1:0:-1]
                for s in list:
                    self.mWriter.write("------- : " + s.strip())
                    self.mWriter.write("\r\n")
            self.mWriter.write("\r\n\r\n\n")
        except Exception as ex:
            print(traceback.format_exc())


LogWriter.loger = None
LogWriter.error = None
LogWriter.jsprint = None
