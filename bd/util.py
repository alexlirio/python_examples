'''
Created on 8 de mar de 2017

@author: alirio
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql.cursors
import pymysql
import json
#from bd.config import config

class util:
    
    __connection = None;
    __cursor = None;
    
    def __init__(self):
        
        with open('bd/config.json') as f:
            config = json.load(f)
        
        __db_config = config['mysql'];
        self.__connection = pymysql.connect(host=__db_config['host'],
                                            user = __db_config['user'],
                                            password = __db_config['password'],
                                            db = __db_config['db'],
                                            charset = 'utf8mb4',
                                            cursorclass = pymysql.cursors.DictCursor);
        self.__cursor = self.__connection.cursor();
    def query(self, query, params):
        self.__cursor.execute(query, params)
        return self.__cursor;

    def close(self):
        self.__connection.close();