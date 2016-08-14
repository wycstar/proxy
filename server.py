#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests

UA = {'Connection': 'Keep-Alive',
      'Accept': 'text/html, application/xhtml+xml, */*',
      'Accept-Language': 'zh-CN,zh;q=0.8',
      'Accept-Encoding': 'gzip,deflate,sdch',
      'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}

def getHtmlContent(url):
    html = requests.get(url,
                        timeout=5,
                        headers=UA).content.decode('utf-8', 'ignore')
    return html

if __name__ == "__main__":
    print(getHtmlContent('http://www.baidu.com'))