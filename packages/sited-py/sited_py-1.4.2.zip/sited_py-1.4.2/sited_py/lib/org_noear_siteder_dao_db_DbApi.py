# -*- coding: UTF-8 -*-
"""
Author:wistn
since:2020-06-11
LastEditors:Do not edit
LastEditTime:2020-10-06
Description:
"""


class DbApi:
    @classmethod
    def isFaved(cls, book):
        return False

    @classmethod
    def logBID(cls, source, bookKey, bookUrl):
        # if (
        #     db.existsSQL('SELECT * from .books WHERE bkey=?', bookKey) == False
        # ) {
        #     db.updateSQL(
        #         'INSERT INTO books(bkey,url,source) VALUES(?,?,?) ',
        #         bookKey,
        #         bookUrl,
        #         source
        #     )
        pass

    @classmethod
    def getBID(cls, bookKey):
        # let bid = 0
        # let dr = db.selectSQL('SELECT id from .books WHERE bkey=? ', bookKey)
        # if (dr.read()) {
        #     bid = dr.getInt('id')
        #         # dr.close()
        # return bid
        pass
