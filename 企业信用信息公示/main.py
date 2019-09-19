# -*- coding : utf-8 -*- #

__author__ = "Gallen_qiu"
import requests

def req():
    url='http://www.gsxt.gov.cn/affiche-query-area-info-paperall.html'
    headers={
           "Accept": "application/json,text/javascript,*/*;q=0.01",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh,zh-CN;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": "24",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Host": "www.gsxt.gov.cn",
        "Origin": "http://www.gsxt.gov.cn",
        "Referer": "http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
        "X-Requested-With": "XMLHttpRequest",
        'Pragma':"no-cache"

          }
    data={
        'draw': '1',
        'start': '0',
        'length': '10'
    }
    cookies={
        '__jsl_clearance': '1568713454.642|0|wfFJhoBc2bGCPLK0vGeEgfTTJGM=',
        '__jsluid_h': '535efb1285bd1d737fcaa06e519756d0',
        'CNZZDATA1261033118': '1134334638-1568713316-http%3A%2F%2Fwww.gsxt.gov.cn%2F|1568713316',
        'JSESSIONID': 'E9203C4CB5C66D114611A71B2F350071-n1:1',
        'SECTOKEN': '6936359956272382852',
        'tlb_cookie': 'S172.16.12.130',
        'UM_distinctid': '16d3e9bc0049-093e82c07dd703-4c312373-fa000-16d3e9bc0059d'
    }

    querystring = {"noticeType":"11","areaid":"100000","noticeTitle":"","regOrg":""}
    payload = "draw=1&start=0&length=10"
    response=requests.post(url,headers=headers,data=payload, params=querystring,cookies=cookies)
    print(response.text)
    
if __name__ == '__main__':
    req()