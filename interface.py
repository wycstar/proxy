#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tornado import ioloop, httpserver, web
import requests
import mimetypes

UA = {'Connection': 'Keep--Alive',
      'Accept': 'text/html, application/xhtml+xml, */*',
      'Accept-Language': 'zh-CN,zh;q=0.8',
      'Accept-Encoding': 'gzip,deflate,sdch',
      'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}

MIME_TYPE = ('application', 'audio', 'image', 'text', 'video', 'x-world', 'multipart')

class MainHandler(web.RequestHandler):
    def get(self):
        '''
        isBinary = False
        mimeType = self.request.headers['Accept']
        print(mimeType)
        if(mimeType is not None):
            mimeType = mimeType[:mimeType.find('/')]
            if(mimeType != 'text'):
                isBinary = True
        print(isBinary)
        print(mimeType)
        '''
        isBinary = False
        r = requests.get(self.request.uri,
                         timeout=5,
                         headers=UA)
        print(r.headers)
        mimeType = r.headers.get('Content-Type')
        if(mimeType is None):
            mimeType = mimetypes.guess_type(self.request.uri)[0]
            if(mimeType is None):
                mimeType = self.request.headers['Accept']
            mimeType = mimeType[:mimeType.find('/')]
        else:
            mimeType = mimeType[:mimeType.find('/')]
        print(mimeType)
        if(mimeType != 'text'):
            isBinary = True
        html = r.content.decode(r.encoding, 'ignore') if not isBinary else r.content
        # print(r.headers)
        # html = r.content.decode(r.encoding, 'ignore')
        # html = r.content
        # print(type(html))
        self.write(html)

if __name__ == '__main__':
    application = web.Application([(r".*", MainHandler)])
    application.listen(9000)
    ioloop.IOLoop.instance().start()
