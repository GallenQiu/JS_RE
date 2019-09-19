# -*- coding : utf-8 -*- #

__author__ = "Gallen_qiu"
import execjs,requests
#密码加密模块
def encode_paw(code):
    with open('加密.js') as f:
        js_encrypt = f.read()
    ctx_encrypt = execjs.compile(js_encrypt)
    password = ctx_encrypt.call('get_pwd',code)#code是你的密码
    return password
#登陆模块
def login():
    url='https://webapi.fenbi.com/tiku/api/users/loginV2?kav=12&app=web'
    headers={
        "Accept": "application/json,text/plain,*/*",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Origin": "https://fenbi.com",
        "Referer": "https://fenbi.com/page/home",
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/74.0.3729.169Safari/537.36",
    }
    password=encode_paw("123456")#调用加密
    data={

        "password": password,
        "persistent": "true",
        "app": "pc",
        "phone": "13712345678"
    }
    response=requests.post(url,headers=headers,data=data)
    print(response.text)
    
if __name__ == '__main__':
    login()