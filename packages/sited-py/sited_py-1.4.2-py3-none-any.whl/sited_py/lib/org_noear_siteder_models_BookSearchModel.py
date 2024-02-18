# -*- coding: UTF-8 -*-
"""
Author:wistn
since:Do not edit
LastEditors:Do not edit
LastEditTime:2020-08-06
Description:
"""
from .org_noear_siteder_models_BookUpdateModel import BookUpdateModel


class BookSearchModel(BookUpdateModel):
    def __init__(self):
        super().__init__()
        self.isFromFavs = False

