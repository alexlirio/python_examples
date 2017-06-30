# -*- coding: utf-8 -*-
from bd.util import util


class CompanyDAO(object):
    __db = None;

    def __init__(self):
        self.__db = util()

    def getCompanies(self):
        return self.__db.query("SELECT * FROM company", None).fetchall();
    