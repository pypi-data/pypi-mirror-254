# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-09-11
LastEditors:Do not edit
LastEditTime:2021-09-21
Description:
"""
__version__ = "1.4.2"
# 配置说明：1. 多多猫缓存中的文本缓存sited文件夹在本引擎也默认对应生成（运行插件后在files文件夹下出现，注意有时插件节点没返回数据时可以删除这个文件夹看看）。开启缓存后，异步请求的网页在有效期内再次请求才是同步。如要禁止缓存，可对下行注释，作用于 lib/org_noear_sited___FileCache.py;
enableFileCache = 1
# 2. SiteD插件容器/多多猫安卓版设置中有开发者模式开关，控制运行插件后在files文件夹里是否生成 sited_log.txt, sited_error.txt, sited_print.txt文件。多多猫里默认为关闭，本引擎默认为0即不生成。如要开启生成，下行改为1值，作用于 lib/org_noear_siteder_dao_Setting.py;
isDeveloperModel = 1
# 3. 上面1项为1（生成）的前提下，SiteD插件文件中开头的debug参数(1/0)，会控制本引擎files文件夹里生成的sited_log.txt中是否显示各节点parse解析后返回的数据，为0时只显示节点parse/parseUrl所要解析的网址，不影响sited_error.txt, sited_print.txt文件。
# 4. Log模块( lib/android_util_Log.py)是本引擎模仿安卓logcat功能转储消息日志，生成到 files/logcat_stdout.txt，显示消息日志过程会比 files文件夹里其他日志文件更加丰富。默认不生成，如要开启生成，下行改为1值，作用于 lib/android_util_Log.py。
logcatDump = 0
# 5. 上面1项为1（生成）的前提下，其中VERBOSE类型日志消息写入logcat_stdout文件时，如要同时console.log打印（每条消息开头部分）到运行本引擎的控制台，取消以下VERBOSE_log注释。也可以取消 files/VERBOSE_trace的注释来打印堆栈跟踪。
# VERBOSE_log = 1
# VERBOSE_trace = 1
