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

def getHtmlContent(url):
    r = requests.get(url,
                     timeout=5,
                     headers=UA)
    html = r.content
    return (zlib.compress(html), r.encoding)

def encryptHtml(content):
    handle = AES.new(AES_KEY, AES.MODE_CFB, 'g4vhFIR1KncRIyvO')

    pad = 16 - len(content) % 16
    print(pad)
    content = content + '\0' * pad
    print(len(content))
    secret = handle.encrypt(content)
    return secret

def decryptHtml(secret):
    handle = AES.new(AES_KEY, AES.MODE_CFB, 'g4vhFIR1KncRIyvO')
    p = handle.decrypt(secret)
    print(p.decode('GB2312', 'ignore'))
    # return p

if __name__ == "__main__":
    t = getHtmlContent('http://www.163.com')
    s = encryptHtml(zlib.decompress(t[0]).decode(t[1], 'ignore'))
    # s = encryptHtml(zlib.decompress(t[0]))
    decryptHtml(s)
    # print(t)