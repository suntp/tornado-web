#!/bin/env python

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import time

import motor
import tornado.gen
import tornado.concurrent
import json

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)

class SleepHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        # time.sleep(5)
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield tornado.gen.Task(client.fetch, "http://hq.sinajs.cn/list=sh601006")
        #body = json.loads(response.body)
        info = str(response.code) + str(response.body) + str(response.request_time)
        self.write(info)

class JustNowHandler(tornado.web.RequestHandler):

    def get(self):

        self.write("i hope just now see you")

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
                    handlers=[
                        (r"/sleep", SleepHandler), 
                        (r"/justnow", JustNowHandler)
                    ]
                )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()