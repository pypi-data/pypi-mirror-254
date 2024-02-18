# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-06-11
LastEditors:Do not edit
LastEditTime:2020-06-11
Description:
"""
from .org_noear_siteder_models_ModelBase import ModelBase


class ViewModelBase(ModelBase):
    def __init__(self):
        super().__init__()
        self.tag = 0
