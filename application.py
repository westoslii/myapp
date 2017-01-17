# -*- coding: utf-8 -*-

<<<<<<< HEAD
=======
'''
Created on 2017��1��17��

@author: li.yongtao
'''
>>>>>>> cd7a926a0570b22c5f8c17d25a5dee53f5de3f11
from url import url

import tornado.web
import os

settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
<<<<<<< HEAD
    static_path = os.path.join(os.path.dirname(__file__), "statics"),
    debug = True
)
=======
    static_path = os.path.join(os.path.dirname(__file__), "statics")
    
    )
>>>>>>> cd7a926a0570b22c5f8c17d25a5dee53f5de3f11

application = tornado.web.Application(
    handlers = url,
    **settings
<<<<<<< HEAD
)
=======
    )
>>>>>>> cd7a926a0570b22c5f8c17d25a5dee53f5de3f11
