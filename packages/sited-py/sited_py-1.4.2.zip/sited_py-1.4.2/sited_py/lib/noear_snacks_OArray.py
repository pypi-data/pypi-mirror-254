# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2021-03-02
LastEditors:Do not edit
LastEditTime:2021-03-04
Description:
"""


class OArray:
    def __init__(self):
        self.elements = []

    def add(self, *arguments):
        len = arguments.__len__()
        if len == 1:
            value = arguments[0]
            self.elements.append(value)
        elif len == 2:
            index = arguments[0]
            value = arguments[1]
            self.elements.insert(index, value)

    def get(self, index):
        return self.elements[index]

    def count(self):
        return self.elements.__len__()

    def clear(self):
        self.elements = []
