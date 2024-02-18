# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2021-01-20
LastEditors:Do not edit
LastEditTime:2021-07-03
Description:
"""
from setuptools import setup, find_packages
import os
import sys
import re

# if os.path.dirname(os.path.realpath(__file__)) not in sys.path:
#     path = os.path.dirname(os.path.realpath(__file__))
#     sys.path.insert(0, path)
HERE = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(HERE, "sited_py", "conf.py"), encoding="utf-8") as fs:
    for line in fs.readlines():
        if re.search(r"__version__.+?([\"'])(.+?)\1", line, re.I):
            __version__ = re.search(r"__version__.+?([\"'])(.+?)\1", line, re.I)[2]
            break

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 7)
# This check and everything above must remain compatible with Python 2.7.
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write(
        """==========================
Unsupported Python version
==========================
This version of sited_py requires Python {}.{}, but you're trying to
install it on Python {}.{}.
This may be because you are using a version of pip that doesn't
understand the python_requires classifier. Make sure you
have pip >= 9.0 and setuptools >= 24.2, then try again:
    $ python -m pip install --upgrade pip setuptools
    $ python -m pip install sited_py
This will install the latest version of sited_py which works on your
version of Python.
""".format(
            *(REQUIRED_PYTHON + CURRENT_PYTHON)
        )
    )
    sys.exit(1)
CLASSIFIERS = """
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
Natural Language :: English
License :: OSI Approved :: Apache Software License
Operating System :: Microsoft :: Windows
Operating System :: POSIX :: Linux
Operating System :: MacOS
Programming Language :: Python :: 3
Programming Language :: Python :: 3 :: Only
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Topic :: Software Development :: Libraries :: Python Modules
"""
with open(os.path.join(HERE, "sited_py", "README_EN.md"), encoding="utf-8") as fs:
    dataArr = fs.read().splitlines()
    LONG_DESCRIPTION = (
        dataArr[2]
        + "\n\n[ [README-EN](https://github.com/wistn/sited_py/blob/main/sited_py/README_EN.md)]"
    )
# https://packaging.python.org/guides/distributing-packages-using-setuptools/
# package_dir is a dictionary with package names for keys and directories for values. An empty package name represents the “root package” — the directory in the project that contains all Python source files for the package — so in this case the src directory is designated the root package.
PACKAGE_DIR = {"sited_py": "sited_py"}  # or {"": "."}
# Set packages to a list of all packages in your project, including their subpackages, sub-subpackages, etc. Although the packages can be listed manually, setuptools.find_packages() finds them automatically. Use the include keyword argument to find only the given packages. Use the exclude keyword argument to omit packages that are not intended to be released and installed.
PACKAGES = find_packages(where=".", exclude=(), include=("*"))
# where="src" if structure like src/packageXX
PACKAGES.append("sited_py.files")
PACKAGE_DATA = {
    "sited_py": [
        "__init__.py",
        "conf.py",
        "CHANGELOG.md",
        "README_CN.*",
        "README_EN.*",
    ],
    "sited_py.files": [".gitignore",],
    "sited_py.lib": ["*.py", "*.js"],
}
EXCLUDE_PACKAGE_DATA = {}
py_modules = []
DATA_FILES = []
if __name__ == "__main__":
    metadata = dict(
        name="sited_py",
        version=__version__,
        author="wistn",
        author_email="wistn@qq.com",
        license="Apache Software License",
        description="SiteD Engine for Python version.",
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        url="https://github.com/wistn/sited_py",
        keywords=["sited", "plugin", "engine", "ddcat"],
        platforms=["Windows", "Linux", " MacOS"],
        classifiers=[_ for _ in CLASSIFIERS.splitlines() if _],
        py_modules=py_modules,
        package_dir=PACKAGE_DIR,
        packages=PACKAGES,
        # Don't include_package_data=True.
        include_package_data=False,
        exclude_package_data=EXCLUDE_PACKAGE_DATA,
        package_data=PACKAGE_DATA,
        data_files=DATA_FILES,
        python_requires=">=3." + str(REQUIRED_PYTHON[1]) + ", <4",
        # “install_requires” should be used to specify what dependencies a project minimally needs to run. When the project is installed by pip, this is the specification that is used to install its dependencies.
        install_requires=(["aiohttp>=3.7.3", "lxml>=4.5.0", "pyChakraCore>=0.2.0",],)
    )
    setup(**metadata)
