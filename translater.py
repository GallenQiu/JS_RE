# -*- coding : utf-8 -*- #
__author__ = "Gallen_qiu"
import requests,json

def a(sign):
    import execjs
    with open('cc.js',encoding="utf8") as f:
        js_encrypt = f.read()
    a = execjs.compile(js_encrypt)
    sign = a.call("a",sign)
    return sign

def req(query):
    url='https://fanyi.baidu.com/basetrans'
    headers={
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://fanyi.baidu.com",
        "referer": "https://fanyi.baidu.com/translate?aldtype=16047&query=%E7%99%BE%E5%BA%A6%E7%BF%BB%E8%AF%91%E6%98%AF%E5%82%BB%E9%80%BC&keyfrom=baidu&smartresult=dict&lang=auto2zh",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "x-requested-with": "XMLHttpRequest",
        'cookie':'BIDUPSID=1697F8D74A357AEA47A288AF54449C45; PSTM=1565789117; BAIDUID=1697F8D74A357AEA47A288AF54449C45:SL=0:NR=10:FG=1; MCITY=-340%3A; H_PS_PSSID=; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDUSS=VBVGp0bX5TZkoydEtwU0VwSHVyakxHakd3NnR0cWJXaDl4dVVZc0tsSlJCTkJkSVFBQUFBJCQAAAAAAAAAAAEAAACua5VLuf65~jEwNjI4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFF3qF1Rd6hdQz; delPer=0; PSINO=6; pgv_pvi=5103165440; pgv_si=s7611824128; BDRCVFR[_qWjr5NPbYn]=aeXf-1x8UdYcs; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1571325465; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1571325465; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1571325465; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1571325465; yjs_js_security_passport=41c514f804398c364a7d7868865b64d997ea5c22_1571325465_js'
    }

    data={
        "query":query,
        "from":"zh",
        "to":"en",
        "token":"a0c8240cf7d441847128a432e2e5252c",
        "sign":a(query),
          }
    response=requests.post(url,headers=headers,data=data)
    trans = json.loads(response.text)['trans']

    for tr in trans:
        print(tr["dst"])

if __name__ == '__main__':
    req("百度翻译是傻逼，大傻逼")
    # print(a("12345"))
