# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-09-23
LastEditors:Do not edit
LastEditTime:2020-09-24
Description:
"""
from .org_noear_siteder_models_ModelBase import ModelBase


class SectionModel(ModelBase):
    def __init__(self):
        super().__init__()
        self.index = 0
        self.orgIndex = 0
        self.url = None
        self.name = None
        self.bookName = None
        self.bookUrl = None
        self.total = 0
        self._code = 0
        self.downTotal = 0
        self.downProgress = 0
        self._cfg = None
        # 由外部传值
        self._config = None

    # public boolean isGroup #是否为分组
    # pic total
    # 	public Boolean isLooking
    # 	public Boolean isSectionCache
    # 	public Boolean isDowning
    #
    # 	public int barMaximum
    # 	public int barValue
    def code(self):
        if self._code == 0 and self.url != None:
            self._code = self.url.__hash__()
        return self._code

    def cfg(self, source):
        if self._cfg == None:
            self._cfg = source.section(self.url)
        return self._cfg

