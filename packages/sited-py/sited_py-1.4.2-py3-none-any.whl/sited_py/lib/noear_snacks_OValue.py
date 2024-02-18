# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2021-03-02
LastEditors:Do not edit
LastEditTime:2021-03-04
Description:
"""

from .noear_snacks_OValueType import OValueType


class OValue:
    def __init__(self):
        self._int = 0
        self._long = 0
        self._double = 0
        self._string = None
        self._bool = False
        self._date = 0
        self.type = 0

    def set(self, value):
        if type(value) == int or type(value) == float:
            self._double = value
            self.type = OValueType.Double
        elif type(value) == str:
            self._string = value
            self.type = OValueType.String
        elif type(value) == bool:
            self._bool = value
            self.type = OValueType.Boolean

    def getInt(self):
        if self.type == OValueType.Int:
            return self._int
        elif self.type == OValueType.Long:
            return self._long
        elif self.type == OValueType.Double:
            return int(self._double)
        elif self.type == OValueType.String:
            if self._string == None or self._string.__len__() == 0:
                return 0
            else:
                return int(self._string)

        elif self.type == OValueType.Boolean:
            return 1 if self._bool else 0
        elif self.type == OValueType.DateTime:
            return 0
        else:
            return 0

    def getString(self):
        if self.type == OValueType.Int:
            return str(self._int)
        elif self.type == OValueType.Long:
            return str(self._long)
        elif self.type == OValueType.Double:
            return str(self._double)
        elif self.type == OValueType.String:
            return self._string
        elif self.type == OValueType.Boolean:
            return str(self._bool)
        elif self.type == OValueType.DateTime:
            return str(self._date)
        else:
            return ""

