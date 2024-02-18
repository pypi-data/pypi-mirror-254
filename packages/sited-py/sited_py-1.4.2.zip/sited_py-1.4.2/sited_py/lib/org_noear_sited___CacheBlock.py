# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-12
LastEditors:Do not edit
LastEditTime:2020-05-18
Description:
"""
from datetime import datetime


class __CacheBlock:
    def __init__(self):
        self.value = None
        self.time = None

    def isOuttime(self, config):
        if self.time == None or self.value == None:
            return True
        else:
            if config.cache == 1:
                return False
            else:
                seconds = datetime.now().timestamp() - self.time.timestamp()
                return seconds > config.cache
