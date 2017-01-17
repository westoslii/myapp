# -*- coding: utf-8 -*-

'''
Created on 2017��1��17��

@author: li.yongtao
'''

import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
    
    
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        
        self.write(username)
       