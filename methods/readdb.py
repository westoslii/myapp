# -*- coding: utf-8 -*-
'''


@author: li.yongtao
'''

from db import *

def select_info(table, column, condition, value):
    
    sql = "select " + column + " from " + table + " where " + condition + "='" + value + "'"
    
    print sql
    
    cur.execute(sql)
    lines = cur.fetchall()
    '''
    line value ((2L, u'admin', u'admin'),)
    '''
    return lines
'''
if __name__ == '__main__':
    line = select_info("info", "*", "name", "admin")
    print line
'''    
    
    