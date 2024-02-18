# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-04
LastEditors:Do not edit
LastEditTime:2021-03-02
Description:This file is about some alone functions which be required(reused) in the whole project,but not appropriate to be some alone Classes.
"""


class TextUtils:
    @classmethod
    def isEmpty(cls, str):
        return str == None or str.__len__() == 0