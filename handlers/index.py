# -*- coding: utf-8 -*-

import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('welcome you')
        self.render("index.html")

    def post(self):
        self.write('welcome you to read: www.itdiffer.com')
        username = self.get_argument("username")
        password = self.get_argument("password")
        self.write(username)
