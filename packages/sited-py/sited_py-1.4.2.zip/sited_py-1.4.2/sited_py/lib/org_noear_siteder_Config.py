# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-06-11
LastEditors:Do not edit
LastEditTime:2020-10-06
Description:
"""


class Config:
    @classmethod
    def isPhone(cls):
        if Config._isPhone < 0:
            Config._isPhone = 0 if Config.isTablet() else 1
            cmd = 1001
            if cmd == 1001:
                Config._isPhone = 1
            if cmd == 1002:
                Config._isPhone = 0

        return Config._isPhone == 1

    @classmethod
    def isTablet(cls):
        return 0


Config._isPhone = -1
