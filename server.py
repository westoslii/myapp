# -*- coding: utf-8 -*-

<<<<<<< HEAD
=======
'''
Created on 2017��1��17��

@author: li.yongtao
'''
>>>>>>> cd7a926a0570b22c5f8c17d25a5dee53f5de3f11
import tornado.ioloop
import tornado.options
import tornado.httpserver

from application import application

from tornado.options import define, options

define("port", default = 8000, help = "run on the given port", type = int)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)

    print "Development server is running at http://127.0.0.1:%s" % options.port
    print "Quit the server with Control-C"

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()