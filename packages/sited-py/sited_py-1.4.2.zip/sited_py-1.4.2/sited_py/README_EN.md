# sited_py

SiteD Engine for Python version.

[ [中文说明](README_CN.md)]

---

## Features

-   Support `schema0/1/2`
-   Support running `buildUrl`, `parseUrl(CALL::)`, `parse(get/post/@null)`, `require(include online js library)`
-   Support `header(cookie/referer)`, `ua` configurations
-   Support `hots`, `updates`, `tags`, `tag(subtag)`, `search`, `book[12345678](sections)`, `section[123]` nodes

---

### [ [Features](#Features)|[Configuration](#Configuration)|[Dependencies](#Dependencies)|[Todo](#Todo)|[SpecialThanks](#SpecialThanks)|[Links](#Links)|[CHANGELOG.md](CHANGELOG.md)]

## Configuration

-   Configuration which controls making of sited_log.txt/sited_error.txt/sited_print.txt and sited (cache directory) under the 'files' dir beside this README_EN file, see in conf.py file.

---

## Dependencies

-   [Python](https://www.python.org/) 3.7 or above, for asyncio.run

-   [pyChakraCore](https://github.com/wistn/pyChakraCore) a runtime run SiteD plugin's js code, a python package developed by me

---

## Todo

-   Support login node

---

## SpecialThanks

### The 'lib' library(excludes main_res_raw_xx.js) is totally translated from big parts of Noear's open source [SiteD Engine](https://github.com/noear/SiteD) v35 APP JAVA code to Python language by me. Thank you!

## Links

-   [SiteD plugin center](http://sited.noear.org/): Official SiteD plugin center.

-   [ddcat_plugin_develop](https://www.kancloud.cn/magicdmer/ddcat_plugin_develop): Knowledge about sited plugin development.

-   [DDCat SiteD](https://github.com/Yinr/DDCa-SiteD.vscode-ext): Syntax extension for VS Code, enabled .sited and .sided.xml files in sited language, support syntax highlight.

-   [generators-sited-plugin](https://github.com/htynkn/generators-sited-plugin): Yeoman generator for sited plugin.

-   [sited_js](https://github.com/wistn/sited_js) SiteD Engine for Node JavaScript version.
