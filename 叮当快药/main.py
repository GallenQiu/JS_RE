# -*- coding : utf-8 -*- #

__author__ = "Gallen_qiu"
import execjs,requests,json,js2py,re

codes=[
'010101,010104', #感冒用药
'010502,010503,010504,010505,010506,010507',#儿童用药
'010401,010402,010403,010404,010406,010407',#风湿骨伤
'010801,010802,010803,010804,010901,010902,010807',#两性健康
'011303,010609',#三高用药
'011501,011502,011503,011504,011505,010301,010302,010303,010305,010306,010307,011601,011602,011603,011605,010201,010202,010203,011401,011402,011403,011404,010701,010702,010703,010704,010706,010707,010709,010710,010711,011101,011106',#其他药品
'020101,020103,020105,020201,020202,020203',#名贵滋补
'020403,020404,020406,020409,020414',#药食同源
'020301,020307,020310,020311,020315',#中药饮片
'050301,050303,050305,050401,050601,050602,050604,050605,050606,050101,050106,050102',#医疗器械
'030101,030102,030103,030107,030108,030109,030110,030111,030113',#营养健康
'030201,030202,030204',#营养食品
'040101,040501,040502,040404,040201,040204',#成人用品
'060901,061103,060603,060604,060607,060609,060610,060505,060301,060302,060304,060306,060803,060804,060805,060402,060403,060201,060701,060702',#彩妆个护
'060104'#婴幼用品
]

#密码加密模块
def encode_paw(code):
    with open('Md5.js') as f:
        js_encrypt = f.read()
    ctx_encrypt = execjs.compile(js_encrypt)
    password = ctx_encrypt.call('MD5',code)#code是你的密码
    return password
#请求模块
def req():
    num = 3
    page = 2
    code=codes[num]
    f = "ddsy.product.query.orgcode.product.list.b2cmethodddsy.product.query.orgcode.product.list.b2corderTypeId0orgcode{code}pageNo{page}pageSize100platH5platformH5shopId-1t2019-9-27 19:24:16v1.0versionName3.2.06C57AB91A1308E26B797F4CD382AC79D".format(
        code=code, page=page)
    sign=encode_paw(f)
    url='http://product.ddky.com/product/queryOrgcodeProductListForB2C.htm?sign={sign}&method=ddsy.product.query.orgcode.product.list.b2c&orderTypeId=0&orgcode={code}&pageNo={page}&pageSize=100&plat=H5&platform=H5&shopId=-1&t=2019-9-27%2019:24:16&v=1.0&versionName=3.2.0&callback=jQuery111108367092262989326_1569583381437'.format(sign=sign,code=code,page=page)
    headers={
        "Referer":"http://www.ddky.com/commodity.html?ddkycache=a7b19e879d2f2f279d356f5afa6d5cff",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    }
    response=requests.get(url,headers=headers)
    i=r'jQuery.*?\((.*)\)'
    data=re.findall(i,response.text)[0]
    # print(data)
    data = json.loads(data)
    for i in data["data"]["productList"]:
        print(i["id"],i["name"],i["productSpecifications"])

if __name__ == '__main__':
    req()
