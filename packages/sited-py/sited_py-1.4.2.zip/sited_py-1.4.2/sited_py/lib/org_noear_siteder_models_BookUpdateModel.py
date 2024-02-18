# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-06-11
LastEditors:Do not edit
LastEditTime:2020-10-06
Description:
"""
from .org_noear_siteder_models_BookModel import BookModel


class BookUpdateModel(BookModel):
    #    public static int CurrentIndex
    def __init__(self):
        super().__init__()
        self.newSection = None
        self.updateTime = None
        self.status = None
