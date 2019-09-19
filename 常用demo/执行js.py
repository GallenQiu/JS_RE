# -*- coding : utf-8 -*- #

__author__ = "Gallen_qiu"
import execjs
with open('加密.js') as f:
    js_encrypt = f.read()
ctx_encrypt = execjs.compile(js_encrypt)
password = ctx_encrypt.call('function_name',args)
print(password)