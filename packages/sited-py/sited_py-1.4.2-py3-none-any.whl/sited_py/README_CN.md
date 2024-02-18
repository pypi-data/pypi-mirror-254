# sited_py

SiteD 引擎 Python 版。

[ [README-EN](README_EN.md)]

---

## 特性

-   支持 `schema0/1/2`
-   支持运行 `buildUrl`, `parseUrl(CALL::)`, `parse(get/post/@null)`, `require(含网络 js 库)`
-   支持 `header(cookie/referer)`, `ua` 配置
-   支持 `hots`, `updates`, `tags`, `tag(subtag)`, `search`, `book[12345678](sections)`, `section[123]` 节点

---

### [ [特性](#特性)|[配置](#配置)|[依赖](#依赖)|[待办](#待办)|[致谢](#致谢)|[友链](#友链)|[CHANGELOG.md](CHANGELOG.md)]


## 配置

-   控制本 README_CN 文件旁边的'files'文件夹里的 sited_log.txt/sited_error.txt/sited_print.txt 和 sited(缓存文件夹) 的生成的配置，见 conf.py 文件

---

## 依赖

-   [Python](https://www.python.org/) 3.7 或以上，为了 asyncio.run

-   [pyChakraCore](https://github.com/wistn/pyChakraCore) 一个运行 SiteD 插件 js 代码的虚拟机，是由我开发的 python 包

---

## 待办

-   支持 login 节点

---

## 致谢

### 里面 'lib' 库（不含 main_res_raw_xx.js）是我将 Noear 开源的 [SiteD 引擎](https://github.com/noear/SiteD) v35 容器大部分 JAVA 代码翻译成的 Python 语言。感谢！

## 友链

-   [SiteD plugin center](http://sited.noear.org/) SiteD 插件中心官方版

-   [ddcat_plugin_develop](https://www.kancloud.cn/magicdmer/ddcat_plugin_develop) 多多猫插件开发指南，关于多多猫插件开发相关知识

-   [DDCat SiteD](https://github.com/Yinr/DDCa-SiteD.vscode-ext) VS Code 扩展插件，对 .sited 和 .sited.xml 文件识别为 SiteD 语言，提供语法高亮

-   [generators-sited-plugin](https://github.com/htynkn/generators-sited-plugin) Yeoman 生成器快速初始化项目

-   [sited_js](https://github.com/wistn/sited_js) SiteD 引擎 Node.js 版
