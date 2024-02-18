# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2021-03-02
LastEditors:Do not edit
LastEditTime:2021-03-04
Description:
"""


class OObject:
    def __init__(self):
        self.members = dict()

    def set(self, key, value):
        self.members[key] = value

    def get(self, key):
        return self.members.get(key)

    def contains(self, key):
        return key in self.members

    def count(self):
        return self.members.__len__()

    def clear(self):
        pass

