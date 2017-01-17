# -*- coding: utf-8 -*-

import MySQLdb

conn = MySQLdb.connect(host="localhost", user="root", passwd="westos", db="westos", port=3306, charset="utf8")    #连接对象

cur = conn.cursor()