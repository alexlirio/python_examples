# -*- coding: utf-8 -*-
from bd.util import Util


class CompanyDAO(object):
    __db = None

    def __init__(self):
        self.__db = Util()

    def getCompanies(self):
        return self.__db.query("SELECT * FROM company", None).fetchall()
    