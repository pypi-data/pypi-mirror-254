# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-04
LastEditors:Do not edit
LastEditTime:2020-09-22
Description:
"""


class SdNodeSet:
    def release(self):
        self._items = []

    # ---------------
    def __init__(self, s):
        self._items = []
        self.source = None
        self._dtype = 0
        # 数据类型
        self._btype = 0
        self.name = None
        self.attrs = SdAttributeList()
        self.source = s

    def OnDidInit(self):
        pass

    def dtype(self):
        if self._dtype > 0:
            return self._dtype
        else:
            return 1

    def btype(self):
        if self._btype > 0:
            return self._btype
        else:
            return self.dtype()

    def nodeType(self):
        return 2

    def nodeName(self):
        return self.name

    # @Override
    def isEmpty(self):
        return self._items.__len__() == 0

    def buildForNode(self, element):
        if element == None:
            return self
        self.name = element.tag
        self._items = []
        self.attrs.clear()
        temp = element.attrib.items()
        for key, value in temp:
            self.attrs.set(key, value)  # 存储标签元素的属性
        temp = list(element)  # Returns all direct children，包括注释不包括非注释的文本
        for i in range(temp.__len__()):
            p = temp[i]
            if isinstance(p.tag, str) and p.attrib.items().__len__() == 0:
                if list(p).__len__() == 0:
                    # 说明element的子节点p是<title>xxx</title>这种元素类型
                    self.attrs.set(p.tag, p.text)
        self._dtype = self.attrs.getInt("dtype")
        self._btype = self.attrs.getInt("btype")
        xList = list(element)  # Returns all direct children
        for i in range(xList.__len__()):
            n1 = xList[i]
            if isinstance(n1.tag, str):
                # Element是Node的真子集 Element e1 = (Element) n1
                e1 = n1
                tagName = e1.tag
                if e1.attrib.items().__len__():
                    # 说明element的子节点e1是Node类型例如<hots xxx />、<tags title=yyy><item /></tags>。temp是DdNode不用如java版向上向下转型
                    temp = SdApi.createNode(self.source, tagName).buildForNode(e1)
                    self.add(temp)
                elif list(e1).__len__() > 1 or (
                    list(e1).__len__() and (e1.text or e1[0].tail)
                ):
                    # java版e1.getChildNodes().getLength()>1，说明element的子节点e1是NodeSet类型如<home>，标签之间要有文本节点(即换行、空白)不然<book><book xxx /></book>不会大于1就不能识别为NodeSet。tags不会是NodeSet因为含有title属性占位。temp是DdNodeSet不用如java版向上向下转型
                    temp = SdApi.createNodeSet(self.source, tagName)
                    temp.buildForNode(e1)
                    self.add(temp)
        self.OnDidInit()
        return self

    def nodes(self):
        return self._items

    def get(self, name):
        for n in self._items:
            if name == n.nodeName():
                return n
        return SdApi.createNode(self.source, name).buildForNode(None)

    def nodeMatch(self, url):
        for n in self._items:
            n1 = n
            if n1.isMatch(url):
                Log.v("nodeMatch.select", n1.expr)
                return n1
        return SdApi.createNode(self.source, None).buildForNode(None)

    def add(self, node):
        self._items.append(node)


from .org_noear_sited_SdAttributeList import SdAttributeList
from .android_util_Log import Log
from .org_noear_sited_SdApi import SdApi
