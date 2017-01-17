# -*- coding: utf-8 -*-

<<<<<<< HEAD
=======
'''
Created on 2017��1��17��

@author: li.yongtao
'''

>>>>>>> cd7a926a0570b22c5f8c17d25a5dee53f5de3f11
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
<<<<<<< HEAD
        self.write('welcome you')
        self.render("index.html")

    def post(self):
        self.write('welcome you to read: www.itdiffer.com')
        username = self.get_argument("username")
        password = self.get_argument("password")
        self.write(username)
=======
        self.render("index.html")
    
    
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        
        self.write(username)
       
>>>>>>> cd7a926a0570b22c5f8c17d25a5dee53f5de3f11
