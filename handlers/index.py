# -*- coding: utf-8 -*-

'''
Created on 2017��1��17��

@author: li.yongtao
'''

import tornado.web

from methods import readdb
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
    
    
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")

        info = readdb.select_info("myapp", "*", "username", username)

        if info:
            passwd = info[0][2]
            if password == passwd:
                self.write("welcome you: " + username)
            else:
                self.write("your password are not right")
        else:
            self.write("There is no the " + username)
        
