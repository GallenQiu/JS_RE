# -*- coding : utf-8 -*- #
from fontTools.ttLib import TTFont
__author__ = "Gallen_qiu"
import requests,re,base64
from bs4 import BeautifulSoup
import xml.etree.ElementTree as et

class Font_58:
    def __init__(self):
        #解密映射字典
        self.font_dict={}

    # 请求原始页面模块
    def req(self):
        '''
        请求原始页面保存下来，并抓取base64字符串解密、保存成ttf、xml文件；
        :return:
        '''
        #这里的url可以自己换
        url='https://sz.58.com/nanshan/chuzu/?PGTID=0d3090a7-0000-445e-32c6-0979240a3ef8&ClickID=2'
        headers={}
        response=requests.get(url,headers=headers)
        i=r'src:url\(\'data:application/font-ttf;charset=utf-8;base64,(.*?)\)'
        base64_str=re.findall(i,response.text)[0] # base64字符串获取
        base64_str_decode = base64.b64decode(base64_str) # base64字符串解密
        filr_name = "58.ttf"
        with open(filr_name, 'wb') as f:
            f.write(base64_str_decode)
        font = TTFont('58.ttf')  # 打开本地的ttf文件
        font.saveXML('58.xml')  # 转换成xml
        with open('58.html','w')as f:
            f.write(response.text.split('<!--房源列表信息-->')[1].split("<!-- 列表展示 end-->")[0])

    #生成解密映射字典模块
    def make_parseDict(self):
        '''
        打开xml文件，建立索引字典，再把匹配好的映射字典放进去。
        :return:
        '''
        root = et.parse('58.xml').getroot()
        gp=root.find("glyf").findall("TTGlyph")
        g_dict={}
        for c in gp:
            try:
                g_dict[c.attrib['name']]=int(c.attrib['xMin'])+int(c.attrib['yMin'])+int(c.attrib['xMax'])+int(c.attrib['yMax'])-2650
            except:
                pass

        cmap= root.find('cmap').find('cmap_format_4').findall('map')
        self.font_dict={}
        #a是匹配好的字典：需要手动匹配一次，真实的数字对应“int(c.attrib['xMin'])+int(c.attrib['yMin'])+int(c.attrib['xMax'])+int(c.attrib['yMax'])-2650”
        a = {'0': 7,
             '-70': 5,
             '14': 6,
             '27': 4,
             '-52': 3,
             '-13': 2,
             '-7': 9,
             '12': 0,
             '-3': 8,
             '9':1
             }
        for c in cmap:
            try:
                self.font_dict['&#'+str(c.attrib['code'])[1:]+';']=a[str(g_dict[c.attrib['name']])]
            except:
                pass
        print(self.font_dict)

    # 原始页面解密数字
    def parse_html(self):
        '''
        打开保存的原始页面html，遍历解密映射字典，把密文都替换掉
        :return:
        '''
        with open('58.html','r') as f:
            html_58=f.read()
        for code in self.font_dict:
            html_58=html_58.replace(code,str(self.font_dict[code]))

        soup=BeautifulSoup(html_58,'lxml')
        des=soup.select(".des")
        t=0
        for de in des:
            title=de.select("h2")[0].text.replace(" ",'').replace("\n",'')
            room=de.select(".room")[0].text.replace(" ",'').replace("\n",'')
            money=soup.select(".money b")[t].text+'元/月'
            t+=1
            print(title,room,money)
        # print(html_58)

    #控制器
    def scheduler(self):
        self.req()
        self.make_parseDict()
        self.parse_html()


if __name__ == '__main__':
    F=Font_58()
    F.scheduler()

