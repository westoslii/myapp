# -*- coding: utf-8 -*-
<<<<<<< HEAD
=======
'''
Created on 2017��1��17��

@author: li.yongtao
'''

>>>>>>> cd7a926a0570b22c5f8c17d25a5dee53f5de3f11
"""
the url structure of website
"""

<<<<<<< HEAD
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from handlers.index import IndexHandler
=======
import sys     #utf-8
reload(sys)
#sys.setdefaultencoding("utf-8")

from handlers.index import IndexHandler    
>>>>>>> cd7a926a0570b22c5f8c17d25a5dee53f5de3f11

url = [
    (r'/', IndexHandler),
]