# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-04-28
LastEditors:Do not edit
LastEditTime:2021-06-11
Description:
"""

import os
import sys
import traceback
from datetime import datetime
import sited_py.conf


class Log:

    # 模仿安卓 logcat 转储消息日志，每条截取前几百个字符
    @classmethod
    def v(cls, tag, msg):
        if getattr(sited_py.conf, "logcatDump", False):
            with open(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)),
                    "..",
                    "files",
                    "logcat_stdout.txt",
                ),
                "a",
                encoding="utf-8",
            ) as fs:
                fs.write(
                    datetime.now().strftime("%I:%M:%S %p")
                    + " VERBOSE/"
                    + tag
                    + ": "
                    + (msg[0:150] + " ..." if msg else "")
                    + "\r\n"
                )
            # 参数在sited_py/conf.py设置
            if getattr(sited_py.conf, "VERBOSE_log", False):
                print("VERBOSE/" + tag + ": " + (msg[0:150] + " ..." if msg else ""))
            elif getattr(sited_py.conf, "VERBOSE_trace", False):
                print(
                    "VERBOSE/"
                    + tag
                    + ": "
                    + (msg[0:150] + " ..." if msg else "")
                    + "\n"
                    + "".join(traceback.format_stack()[::-1])
                )

    @classmethod
    def i(cls, tag, msg):
        if getattr(sited_py.conf, "logcatDump", False):
            with open(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)),
                    "..",
                    "files",
                    "logcat_stdout.txt",
                ),
                "a",
                encoding="utf-8",
            ) as fs:
                fs.write(
                    datetime.now().strftime("%I:%M:%S %p")
                    + " INFO/"
                    + tag
                    + ": "
                    + msg
                    + "\r\n"
                )
            # print('INFO/' + tag + ': ' + msg+ '\n' + ''.join(traceback.format_stack()[::-1]))

    @classmethod
    def e(cls, tag, msg):
        if getattr(sited_py.conf, "logcatDump", False):
            with open(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)),
                    "..",
                    "files",
                    "logcat_stdout.txt",
                ),
                "a",
                encoding="utf-8",
            ) as fs:
                fs.write(
                    datetime.now().strftime("%I:%M:%S %p")
                    + " ERROR/"
                    + tag
                    + ": "
                    + msg
                    + "\r\n"
                )

            print(
                "ERROR/" + tag + ": " + msg + "\n" + "".join(traceback.format_stack()[::-1])
            )

    @classmethod
    def w(cls, tag, msg):
        if getattr(sited_py.conf, "logcatDump", False):
            with open(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)),
                    "..",
                    "files",
                    "logcat_stdout.txt",
                ),
                "a",
                encoding="utf-8",
            ) as fs:
                fs.write(
                    datetime.now().strftime("%I:%M:%S %p")
                    + " WARN/"
                    + tag
                    + ": "
                    + msg
                    + "\r\n"
                )

            print(
                "WARN/" + tag + ": " + msg + "\n" + "".join(traceback.format_stack()[::-1])
            )

    @classmethod
    def d(cls, tag, msg):
        if getattr(sited_py.conf, "logcatDump", False):
            with open(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)),
                    "..",
                    "files",
                    "logcat_stdout.txt",
                ),
                "a",
                encoding="utf-8",
            ) as fs:
                fs.write(
                    datetime.now().strftime("%I:%M:%S %p")
                    + " DEBUG/"
                    + tag
                    + ": "
                    + msg
                    + "\r\n"
                )

            print(
                "DEBUG/" + tag + ": " + msg + "\n" + "".join(traceback.format_stack()[::-1])
            )

