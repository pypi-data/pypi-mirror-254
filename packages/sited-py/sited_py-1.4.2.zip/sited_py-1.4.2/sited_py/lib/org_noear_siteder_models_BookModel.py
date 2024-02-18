# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-06-11
LastEditors:Do not edit
LastEditTime:2020-06-11
Description:
"""
from .org_noear_siteder_dao_db_BookNode import BookNode


class BookModel(BookNode):
    def __init__(self):
        super().__init__()
        self._id = None
        self._dtype = 0
        self.btype = 0
        self.btag = None
        self.index = 0
        self.source = None
