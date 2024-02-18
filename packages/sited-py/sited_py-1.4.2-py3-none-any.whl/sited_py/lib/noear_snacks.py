# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2021-03-03
LastEditors:Do not edit
LastEditTime:2021-04-04
Description:
"""
import json
from .noear_snacks_ONodeType import ONodeType
from .noear_snacks_OArray import OArray
from .noear_snacks_OValue import OValue
from .noear_snacks_OObject import OObject


class ONodeBase:
    def __init__(self, *arguments):
        self._array = None
        self._object = None
        self._value = None
        self._type = ONodeType.Null

    @classmethod
    def tryLoad(cls, ops):
        return ONodeBase.load(ops)

    @classmethod
    def load(cls, ops):
        if ops == None or ops.__len__() < 2:
            return ONode()
        if ops[0] == "<":
            # return ONodeBase.readXmlValue(XmlReader(ops))
            pass
        else:
            return ONodeBase.readJsonValue(json.loads(ops))

    def tryInitValue(self):
        if self._value == None:
            self._value = OValue()
        if self._type != ONodeType.Value:
            self._type = ONodeType.Value

    def tryInitObject(self):
        if self._object == None:
            self._object = OObject()
        if self._type != ONodeType.Object:
            self._type = ONodeType.Object

    def tryInitArray(self):
        if self._array == None:
            self._array = OArray()
        if self._type != ONodeType.Array:
            self._type = ONodeType.Array

    def isObject(self):
        return self._type == ONodeType.Object

    def isArray(self):
        return self._type == ONodeType.Array

    def asObject(self):
        self.tryInitObject()
        return self

    def asArray(self):
        self.tryInitArray()
        return self

    def setDouble(self, value):
        self.tryInitValue()
        self._value.set(value)

    def setString(self, value):
        self.tryInitValue()
        self._value.set(value)

    def setBoolean(self, value):
        self.tryInitValue()
        self._value.set(value)

    def __iter__(self):
        if self.isArray():
            return self._array.elements.__iter__()
        else:
            return None

    @classmethod
    def readJsonValue(cls, Value):
        instance = ONode()
        Token = type(Value)
        if Value == None:
            instance._type = ONodeType.Null
            return instance
        if Token == str:
            instance.setString(Value)
            return instance
        if Token == int or Token == float:
            instance.setDouble(Value)
            return instance
        if Token == bool:
            instance.setBoolean(Value)
            return instance
        if Token == list:
            instance.tryInitArray()
            for i in range(Value.__len__()):
                item = ONodeBase.readJsonValue(Value[i])
                instance.add(item)
        elif Token == dict:
            instance.tryInitObject()
            for property in Value:
                val = ONodeBase.readJsonValue(Value[property])
                instance.set(property, val)
        return instance


class ONode(ONodeBase):
    def __init__(self, *arguments):
        super().__init__()
        self._unescape = False
        len = arguments.__len__()
        if len == 0:
            pass
        elif len == 1:
            value = arguments[0]
            self.tryInitValue()
            self._value.set(value)

    def unescape(self, isUnescape):
        self._unescape = isUnescape
        return self

    def getInt(self):
        if self._value == None:
            return 0
        else:
            return self._value.getInt()

    def getString(self):
        if self._value == None:
            return ""
        else:
            if self._unescape:
                pass
                # str = self._value.getString()
                # if(str == None or str.__len__()==0):
                #     return str
                # try:
                #     StringWriter writer = StringWriter(str.__len__())
                #     ONode.unescapeUnicode(writer, str)
                #     return writer.toString()
                # except Exception as ex:
                #     return str
            else:
                return self._value.getString()

    def get(self, *arguments):
        if type(arguments[0]) == int:
            index = arguments[0]
            self.tryInitArray()
            if self._array.elements.__len__() > index:
                return self._array.elements[index].unescape(self._unescape)
            else:
                return None
        elif type(arguments[0]) == str:
            key = arguments[0]
            self.tryInitObject()
            if self._object.contains(key):
                return self._object.get(key).unescape(self._unescape)
            else:
                temp = ONode()
                self._object.set(key, temp)
                return temp

    def add(self, *arguments):
        len = arguments.__len__()
        if len == 1:
            value = arguments[0]
            # 返回自己
            if isinstance(value, ONode):
                self.tryInitArray()
                self._array.add(value)
                return self
            else:
                return self.add(ONode(value))
        elif len == 2:
            value = arguments[0]
            isOps = arguments[1]
            if isOps:
                return self.add(ONode.tryLoad(value))
            else:
                return self.add(ONode(value))
        elif len == 0:
            # 返回新节点
            n = ONode()
            self.add(n)
            return n

    def set(self, *arguments):
        len = arguments.__len__()
        # 返回自己
        if len == 2:
            key = arguments[0]
            value = arguments[1]
            if isinstance(value, ONode):
                self.tryInitObject()
                self._object.set(key, value)
                return self
            else:
                return self.set(key, ONode(value))
        elif len == 3:
            key = arguments[0]
            value = arguments[1]
            isOps = arguments[2]
            if isOps:
                return self.set(key, ONode.tryLoad(value))
            else:
                return self.set(key, ONode(value))


class FormatHanlder:
    def run(self, e):
        if e == None:
            return "None"
        else:
            return e.toString()


ONode.NULL_DEFAULT = "None"
ONode.BOOL_USE01 = False
ONode.TIME_FORMAT_ACTION = FormatHanlder()
