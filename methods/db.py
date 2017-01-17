# -*- coding: utf-8
'''
Created on 2017��1��17��

@author: li.yongtao
'''
import MySQLdb

#conn = MySQLdb.connect(host="10.218.139.81", user="root", passwd="westos", db="myapp", port=3306, charset="utf8")   #连接对象
conn = MySQLdb.connect(host="localhost", user="root", passwd="westos", db="westos", port=3306, charset="utf8")
cur = conn.cursor()    #游标对象


