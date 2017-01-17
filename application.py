# -*- coding: utf-8 -*-

'''
Created on 2017��1��17��

@author: li.yongtao
'''
from url import url

import tornado.web
import os

settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "statics")
    
    )

application = tornado.web.Application(
    handlers = url,
    **settings
    )