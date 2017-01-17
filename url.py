# -*- coding: utf-8 -*-
'''
Created on 2017��1��17��

@author: li.yongtao
'''

"""
the url structure of website
"""

import sys     #utf-8
reload(sys)
#sys.setdefaultencoding("utf-8")

from handlers.index import IndexHandler    

url = [
    (r'/', IndexHandler),
]