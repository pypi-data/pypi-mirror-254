# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-05-24
LastEditors:Do not edit
LastEditTime:2021-04-22
Description:
"""
import traceback
import ctypes
import json
from pyChakraCore import pyChakraCore
from .android_util_Log import Log
from .org_noear_sited_SdApi import SdApi
from .org_noear_sited_SdExt import SdExt


class JsEngine:
    def release(self):
        if self.engine != None:
            # engine.getLocker().release()
            self.engine = None
            self.source = None

    def __init__(self, app, sd):
        self.source = sd
        self.engine = pyChakraCore()

        def callback(
            ptr_callee,
            isConstructCall,
            ptrj_arguments,
            argumentCount,
            callbackState,
        ):
            if argumentCount > 1:
                # chakraCore虚拟机里，注册方法第一个参数都是undefined。当参数not defined 时，不会进入本原生函数，而是JsRun返回空字符串''回调用处。
                jArg1 = ctypes.c_void_p(ptrj_arguments[1])
                jsType1 = self.engine.getValueType(jArg1)
                if jsType1 == "JsString" or jsType1 == "JsNull":
                    arg1 = self.engine.jValueToNativeStr(jArg1)
                    SdApi.log(self.source, "JsEngine.print", arg1)
                    return self.engine.jUndefined.value
                else:
                    raise Exception("收到参数类型" + jsType1 + " 插件print函数要求(第一个)参数是字符串")

        ext = SdExt(sd)

        def v8Ext_get(
            ptr_callee,
            isConstructCall,
            ptrj_arguments,
            argumentCount,
            callbackState,
        ):
            jArg1 = ctypes.c_void_p(ptrj_arguments[1])
            jsType1 = self.engine.getValueType(jArg1)
            if jsType1 == "JsString" or jsType1 == "JsNull":
                key = self.engine.jValueToNativeStr(jArg1)
                val = ext.get(key)
                return self.engine.getJValue(repr(val)).value
            else:
                raise Exception("收到参数类型" + jsType1 + " 函数要求参数是字符串")

        def v8Ext_set(
            ptr_callee,
            isConstructCall,
            ptrj_arguments,
            argumentCount,
            callbackState,
        ):
            jArg1 = ctypes.c_void_p(ptrj_arguments[1])
            jArg2 = ctypes.c_void_p(ptrj_arguments[2])
            jsType1 = self.engine.getValueType(jArg1)
            jsType2 = self.engine.getValueType(jArg2)
            if (jsType1 == "JsString" or jsType1 == "JsNull") and (
                jsType2 == "JsString" or jsType2 == "JsNull"
            ):
                key = self.engine.jValueToNativeStr(jArg1)
                val = self.engine.jValueToNativeStr(jArg2)
                ext.set(key, val)
                return self.engine.jUndefined.value
            else:
                raise Exception("收到参数类型" + jsType1 + "," + jsType2 + " 函数要求参数是字符串")

        cfunctype_JsNativeFunction = ctypes.CFUNCTYPE(
            ctypes.c_void_p,
            ctypes.c_void_p,
            ctypes.c_bool,
            ctypes.POINTER(ctypes.c_void_p),
            ctypes.c_ushort,
            ctypes.py_object,
        )
        self.c_callback = cfunctype_JsNativeFunction(callback)
        self.c_v8Ext_get = cfunctype_JsNativeFunction(v8Ext_get)
        self.c_v8Ext_set = cfunctype_JsNativeFunction(v8Ext_set)
        self.engine.registerMethod(self.c_callback, "print")
        self.engine.registerMethod(self.c_v8Ext_get, "SdExt.get")
        self.engine.registerMethod(self.c_v8Ext_set, "SdExt.set")
        self.loadJs(enhanceObj)  # 插件print函数要求参数是字符串，js版引擎通过enhanceObj实现print接收任何类型对象后转换为格式化字符串打印方便了解对象属性

    def loadJs(self, code):
        try:
            self.engine.run(code)  # 预加载了批函数
            # 不用 pyexecjs 因为不保留上下文变量。
        except Exception as ex:
            print(traceback.format_exc())
            SdApi.log(self.source, "JsEngine.loadJs", ex)
            raise ex
        return self

    def callJs(self, fun, atts):
        if self.source.schema >= 2:
            return self.callJs2(fun, atts.getJson())
        else:
            return self.callJs1(fun, atts.getValues())

    # 调用函数 可能传参数
    def callJs1(self, fun, args):
        # args类型是字符串组成的数组
        try:
            jsonArgs = json.dumps(args)
            temp = self.engine.run(
                """{0}(...JSON.parse({1}))""".format(fun, repr(jsonArgs))
            )
            # temp = self.engine.callFunction(fun, *args) # 容易有 segmentation fault
            return temp
        except Exception as ex:
            print(traceback.format_exc())
            SdApi.log(self.source, "JsEngine.callJs:" + fun, ex)
            return None

    def callJs2(self, fun, json_):
        jscode = []
        jscode.append(fun)
        jscode.append("(")
        jscode.append(json_)
        jscode.append(")")
        code = "".join(jscode)
        Log.v("jscode:", code)
        try:
            temp = self.engine.run(code)
            return temp
        except Exception as ex:
            print(traceback.format_exc())
            SdApi.log(self.source, "JsEngine.callJs:" + code, ex)
            return None


# 把字符串当作代码表达式执行时需要双倍反斜杠，或者用原始字符串格式
enhanceObj = r"""
function enhanceObj() {
    'use strict';
    function pretty(obj, space) {
        if (space == null) space = 4;
        var backslashN = '\n';
        var indent = '',
            subIndents = '';
        if (typeof space == 'number') {
            for (var i = 0; i < space; i++) {
                indent += ' ';
            }
        } else if (typeof space == 'string') {
            indent = space;
        }
        function str(obj) {
            var jsType = Object.prototype.toString.call(obj);
            if (jsType.match(/object (String|Date|Function|JSON|Math|RegExp)/)) {
                return JSON.stringify(String(obj));
            } else if (jsType.match(/object (Number|Boolean|Null)/)) {
                return JSON.stringify(obj);
            } else if (jsType.match(/object Undefined/)) {
                return JSON.stringify('undefined');
            } else {
                if (jsType.match(/object (Array|Arguments|Map|Set)/)) {
                    if (jsType.match(/object (Map|Set)/)) {
                        // function and type in js es6 or above
                        obj = Array.from(obj);
                    }
                    var partial = [];
                    subIndents = subIndents + indent;
                    var len = obj.length;
                    for (var i = 0; i < len; i++) {
                        partial.push(str(obj[i]));
                    }
                    var result =
                        len == 0
                            ? '[]'
                            : indent.length
                            ? '[' +
                            backslashN +
                            subIndents +
                            partial.join(',' + backslashN + subIndents) +
                            backslashN +
                            subIndents.slice(indent.length) +
                            ']'
                            : '[' + partial.join(',') + ']';
                    subIndents = subIndents.slice(indent.length);
                    return result;
                } else if (
                    jsType.match(
                        /object (Object|Error|global|Window|HTMLDocument)/i
                    ) ||
                    obj instanceof Error
                ) {
                    var partial = [];
                    subIndents = subIndents + indent;
                    var ownProps = Object.getOwnPropertyNames(obj);
                    // Object.keys returns obj's own enumerable property names(no use for...in loop because including inherited enumerable properties from obj's prototype chain
                    // Object.getOwnPropertyNames = Object.keys + obj's own non-enumerable property names
                    var len = ownProps.length;
                    for (var i = 0; i < len; i++) {
                        partial.push(
                            str(ownProps[i]) +
                                (indent.length ? ': ' : ':') +
                                str(obj[ownProps[i]])
                        );
                    }
                    var result =
                        len == 0
                            ? '{}'
                            : indent.length
                            ? '{' +
                            backslashN +
                            subIndents +
                            partial.join(',' + backslashN + subIndents) +
                            backslashN +
                            subIndents.slice(indent.length) +
                            '}'
                            : '{' + partial.join(',') + '}';
                    subIndents = subIndents.slice(indent.length);
                    return result;
                } else {
                    return JSON.stringify(String(obj));
                }
            }
        }
        function decycle(obj) {
            // the function can solve circular structure like JSON.decycle, the return value can be decoded by JSON.retrocycle(JSON.parse())
            var arrParents = [];
            return (function derez(obj, path) {
                var jsType = Object.prototype.toString.call(obj);
                if (
                    jsType.match(
                        /object (String|Date|Function|JSON|Math|RegExp|Number|Boolean|Null|Undefined)/
                    )
                ) {
                    return obj;
                } else {
                    if (jsType.match(/object (Array|Arguments|Map|Set)/)) {
                        var len = arrParents.length;
                        for (var i = 0; i < len; i++) {
                            // arr like [obj, '$']
                            var arr = arrParents[i];
                            if (obj === arr[0]) {
                                return { $ref: arr[1] };
                            }
                        }
                        arrParents.push([obj, path]);
                        var newObj = [];
                        if (jsType.match(/object (Map|Set)/)) {
                            // function and type in js es6 or above
                            obj = Array.from(obj);
                        }
                        var length = obj.length;
                        for (var i = 0; i < length; i++) {
                            newObj[i] = derez(obj[i], path + '[' + i + ']');
                        }
                        return newObj;
                    } else {
                        var len = arrParents.length;
                        for (var i = 0; i < len; i++) {
                            // arr like [obj, '$']
                            var arr = arrParents[i];
                            if (obj === arr[0]) {
                                return { $ref: arr[1] };
                            }
                        }
                        arrParents.push([obj, path]);
                        var newObj = {};
                        var ownProps = Object.getOwnPropertyNames(obj);
                        var length = ownProps.length;
                        for (var i = 0; i < length; i++) {
                            newObj[ownProps[i]] = derez(
                                obj[ownProps[i]],
                                path + '[' + JSON.stringify(ownProps[i]) + ']'
                            );
                        }
                        return newObj;
                    }
                }
            })(obj, '$');
        }
        return str(decycle(obj));
    }
    if (typeof window == 'undefined') {
        /* 插件环境用，可在多多猫和js/py版SiteD插件引擎执行 */
        if (typeof this.WebAssembly != 'undefined') {
            delete this.WebAssembly // 删除是因为py版虚拟机ChakraCore打印this.WebAssembly有无穷循环
        }
        if (typeof pretty != 'undefined') {
            var tmp = this.print;
            var console_log = function () {
                var arr = [];
                var len = arguments.length;
                for (var i = 0; i < len; i++) {
                    arr.push(pretty(arguments[i]));
                }
                tmp(String(arr));
            };
            this.print = console_log;
        }
    }
}
enhanceObj.call(this);
"""
