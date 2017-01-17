<<<<<<< HEAD
# -*- coding: utf-8 -*-

import MySQLdb

conn = MySQLdb.connect(host="localhost", user="root", passwd="westos", db="westos", port=3306, charset="utf8")    #连接对象

cur = conn.cursor()
=======
# -*- coding: utf-8
'''
Created on 2017��1��17��

@author: li.yongtao
'''
import MySQLdb

conn = MySQLdb.connect(host="10.218.139.81", user="root", passwd="westos", db="myapp", port=3306, charset="utf8")   #连接对象

cur = conn.cursor()    #游标对象


>>>>>>> cd7a926a0570b22c5f8c17d25a5dee53f5de3f11
