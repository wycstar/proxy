#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import zlib
import base64
from Crypto.Cipher import AES

UA = {'Connection': 'Keep-Alive',
      'Accept': 'text/html, application/xhtml+xml, */*',
      'Accept-Language': 'zh-CN,zh;q=0.8',
      'Accept-Encoding': 'gzip,deflate,sdch',
      'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}

AES_KEY = '0134596354aghjktyuol4571'
AES_IV = 'g4vhFIR1KncRIyKO'

def getHtmlContent(url):
    r = requests.get(url,
                     timeout=5,
                     headers=UA)
    html = r.content
    return (zlib.compress(html), r.encoding)

def encryptHtml(content):
    handle = AES.new(AES_KEY, AES.MODE_CFB, AES_IV)
    pad = 16 - len(content) % 16
    content = content + '\0' * pad
    secret = handle.encrypt(content)
    return secret

def decryptHtml(secret):
    handle = AES.new(AES_KEY, AES.MODE_CFB, AES_IV)
    p = handle.decrypt(secret).decode('UTF-8', 'ignore')
    return p

if __name__ == "__main__":
    t = getHtmlContent('http://www.163.com')
    s = encryptHtml(zlib.decompress(t[0]).decode(t[1], 'ignore'))
    c = decryptHtml(s)
    print(c)