# -*- coding: utf-8 -*-
import mariadb
import json


class Util:
    
  __connection = None
  __cursor = None

  def __init__(self):

    with open('bd/config.json') as f:
        config = json.load(f)

    __db_config = config['mariadb']
    self.__connection = mariadb.connect(
      host = __db_config['host'],
      user = __db_config['user'],
      password = __db_config['password'],
      database = __db_config['db']
    )
    self.__cursor = self.__connection.cursor()
  def query(self, query, params):
    self.__cursor.execute(query, params)
    return self.__cursor

  def close(self):
    self.__connection.close()
