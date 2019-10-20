# -*- coding : utf-8 -*- #

__author__ = "Gallen_qiu"
#这边打算用代码实现百度翻译的爬虫
#报错：原因是：缺失cookies
#原样复制参数是没有问题的，但是"换了其他的原文就会报错"
#原因是：sign这个参数是经过加密生成的，和原文是对应的关系;token是不变的，cookies和token只要粘贴过去就行
#“我觉得可以的”sign：317649.15328,  token:a0c8240cf7d441847128a432e2e5252c
#”我觉得不可以"的sign：400393.196408,token:a0c8240cf7d441847128a432e2e5252c
#现在只要把sign解出来就可以了/完全一致
import requests,json

def encodejs(query):
    #这是自己写的模板
    import execjs
    with open('encodejs.js',encoding="utf8") as f:
        js_encrypt = f.read()
    encodejs= execjs.compile(js_encrypt)
    sign=encodejs.call("a",query)
    return sign

def req(query):
    url='https://fanyi.baidu.com/basetrans'
    headers={
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://fanyi.baidu.com",
        "referer": "https://fanyi.baidu.com/?aldtype=16047",
        "user-agent": "Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/53.0.2785.143Safari/537.36MicroMessenger/7.0.4.501NetType/WIFIMiniProgramEnv/WindowsWindowsWechat",
        "x-requested-with": "XMLHttpRequest",
        "cookie":'BIDUPSID=1697F8D74A357AEA47A288AF54449C45; PSTM=1565789117; BAIDUID=1697F8D74A357AEA47A288AF54449C45:SL=0:NR=10:FG=1; BDUSS=VBVGp0bX5TZkoydEtwU0VwSHVyakxHakd3NnR0cWJXaDl4dVVZc0tsSlJCTkJkSVFBQUFBJCQAAAAAAAAAAAEAAACua5VLuf65~jEwNjI4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFF3qF1Rd6hdQz; MCITY=-340%3A; locale=zh; H_PS_PSSID=; delPer=0; PSINO=6; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[_qWjr5NPbYn]=aeXf-1x8UdYcs; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1571532307,1571532386,1571532507,1571534078; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1571534078; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1571532310,1571532342,1571532507,1571534078; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1571534078; yjs_js_security_passport=e631f57bc55fcbe6443943ff9b1b0df1b9f27f5a_1571534077_js'
    }
    data={
        "query": query,
        "from": "zh",
        "to": "en",
        "token": "a0c8240cf7d441847128a432e2e5252c",
        "sign":encodejs(query),
    }
    response=requests.post(url,headers=headers,data=data)
    # print(response.text)
    result=json.loads(response.text)["trans"][0]
    print("翻译原文：" + str(result["src"]))
    print("翻译结果："+str(result["dst"]))


if __name__ == '__main__':
    req("好的，这个小项目就做到这里，算是圆满完成，有看的不是很懂的同学欢迎来私信交流！")