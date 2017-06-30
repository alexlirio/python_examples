#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bd.dao import CompanyDAO


if __name__ == '__main__':
    __companydao = CompanyDAO()
    print(__companydao.getCompanies())
    