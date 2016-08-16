#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.httpserver

HTTP_SERVER = tornado.httpserver.HTTPServer(handle_request)

def handle_request(request):
    message = "You requested %s\n" % request.uri
    request.write("HTTP/1.1 200 OK\r\nContent-Length: %d\r\n\r\n%s" % (len(message), message))
    request.finish()

if __name__ == '__main__':
    HTTP_SERVER.bind(9000)
    HTTP_SERVER.start()