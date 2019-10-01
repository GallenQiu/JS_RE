# -*- coding : utf-8 -*- #

__author__ = "Gallen_qiu"
from bs4 import BeautifulSoup
from quyu import quyu
import execjs,requests
class Crawl_58:
    def __init__(self):
        #省份城市列表
        self.cityList = {
            "安徽": {
                "合肥": "hf|837", "芜湖": "wuhu|2045", "蚌埠": "bengbu|3470", "阜阳": "fy|2325", "淮南": "hn|2319",
                "安庆": "anqing|3251", "宿州": "suzhou|3359", "六安": "la|2328", "淮北": "huaibei|9357", "滁州": "chuzhou|10266",
                "马鞍山": "mas|2039", "铜陵": "tongling|10285", "宣城": "xuancheng|5633", "亳州": "bozhou|2329",
                "黄山": "huangshan|2323",
                "池州": "chizhou|10260", "巢湖": "ch|10229", "和县": "hexian|10892", "霍邱": "hq|11226",
                "桐城": "tongcheng|11296",
                "宁国": "ningguo|5645", "天长": "tianchang|10273", "东至": "dongzhi|10262", "无为": "wuweixian|10232"
            },
            "福建": {
                "福州": "fz|304", "厦门": "xm|606", "泉州": "qz|291", "莆田": "pt|2429", "漳州": "zhangzhou|710",
                "宁德": "nd|7951", "三明": "sm|2048", "南平": "np|10291", "龙岩": "ly|6752", "武夷山": "wuyishan|10761",
                "石狮": "shishi|296", "晋江": "jinjiangshi|297", "南安": "nananshi|293", "龙海": "longhai|713",
                "上杭": "shanghangxian|6757",
                "福安": "fuanshi|7969", "福鼎": "fudingshi|7970", "安溪": "anxixian|7100", "永春": "yongchunxian|7101",
                "永安": "yongan|2133",
                "漳浦": "zhangpu|717"
            },
            "广东": {
                "深圳": "sz|4", "广州": "gz|3", "东莞": "dg|413", "佛山": "fs|222", "中山": "zs|771",
                "珠海": "zh|910", "惠州": "huizhou|722", "江门": "jm|629", "汕头": "st|783", "湛江": "zhanjiang|791",
                "肇庆": "zq|901", "茂名": "mm|679", "揭阳": "jy|927", "梅州": "mz|9389", "清远": "qingyuan|7303",
                "阳江": "yj|2284", "韶关": "sg|2192", "河源": "heyuan|10467", "云浮": "yf|10485", "汕尾": "sw|9449",
                "潮州": "chaozhou|10461", "台山": "taishan|11263", "阳春": "yangchun|8566", "顺德": "sd|8716",
                "惠东": "huidong|725",
                "博罗": "boluo|726", "海丰": "haifengxian|9444", "开平": "kaipingshi|634", "陆丰": "lufengshi|9456"
            },
            "广西": {
                "南宁": "nn|845", "柳州": "liuzhou|7133", "桂林": "gl|1039", "玉林": "yulin|2337", "梧州": "wuzhou|2046",
                "北海": "bh|10536", "贵港": "gg|6770", "钦州": "qinzhou|2335", "百色": "baise|10513", "河池": "hc|2340",
                "来宾": "lb|10552", "贺州": "hezhou|10549", "防城港": "fcg|10539", "崇左": "chongzuo|10524",
                "桂平": "guipingqu|6774",
                "北流": "beiliushi|9168", "博白": "bobaixian|9173", "岑溪": "cenxi|2119"
            },
            "贵州": {
                "贵阳": "gy|2015", "遵义": "zunyi|7620", "黔东南": "qdn|9363", "黔南": "qn|10492", "六盘水": "lps|10506",
                "毕节": "bijie|10564", "铜仁": "tr|10417", "安顺": "anshun|7468", "黔西南": "qxn|10434", "仁怀": "renhuaishi|7628",
                "清镇": "qingzhen|12703"
            },
            "甘肃": {
                "兰州": "lz|952", "天水": "tianshui|8601", "白银": "by|10304", "庆阳": "qingyang|10475", "平凉": "pl|7154",
                "酒泉": "jq|10387", "张掖": "zhangye|10454", "武威": "wuwei|10448", "定西": "dx|10322", "金昌": "jinchang|7428",
                "陇南": "ln|10415", "临夏": "linxia|7112", "嘉峪关": "jyg|10362", "甘南": "gn|10343", "敦煌": "dunhuang|10390"
            },
            "海南": {
                "海口": "haikou|2053", "三亚": "sanya|2422", "五指山": "wzs|9952", "三沙": "sansha|13722", "琼海": "qh|10136",
                "文昌": "wenchang|9984", "万宁": "wanning|10022", "屯昌": "tunchang|10044", "琼中": "qiongzhong|10064",
                "陵水": "lingshui|10184",
                "东方": "df|10250", "定安": "da|10303", "澄迈": "cm|10331", "保亭": "baoting|10367", "白沙": "baish|10380",
                "儋州": "danzhou|10394"
            },
            "河南": {
                "郑州": "zz|342", "洛阳": "luoyang|556", "新乡": "xx|1016", "南阳": "ny|592", "许昌": "xc|977",
                "平顶山": "pds|1005", "安阳": "ay|1096", "焦作": "jiaozuo|3266", "商丘": "sq|1029", "开封": "kaifeng|2342",
                "濮阳": "puyang|2346", "周口": "zk|933", "信阳": "xy|8694", "驻马店": "zmd|1067", "漯河": "luohe|2347",
                "三门峡": "smx|9317", "鹤壁": "hb|2344", "济源": "jiyuan|9918", "明港": "mg|8541", "鄢陵": "yanling|9123",
                "禹州": "yuzhou|979", "长葛": "changge|9344", "灵宝": "lingbaoshi|9307", "杞县": "qixianqu|7389",
                "汝州": "ruzhou|1010",
                "项城": "xiangchengshi|935", "偃师": "yanshiqu|7121", "长垣": "changyuan|5936", "滑县": "huaxian|5405",
                "林州": "linzhou|1101",
                "沁阳": "qinyang|3268", "孟州": "mengzhou|3267", "温县": "wenxian|7312", "尉氏": "weishixian|7391",
                "兰考": "lankaoxian|7393",
                "通许": "tongxuxian|7390", "新安": "lyxinan|11217", "伊川": "yichuan|11220", "孟津": "mengjinqu|7122",
                "宜阳": "lyyiyang|11219",
                "舞钢": "wugang|1011", "永城": "yongcheng|1032", "睢县": "suixian|1038", "鹿邑": "luyi|939",
                "渑池": "yingchixian|9322",
                "沈丘": "shenqiu|942", "太康": "taikang|938", "商水": "shangshui|936", "淇县": "qixianq|9186",
                "浚县": "junxian|9185",
                "范县": "fanxian|7285", "固始": "gushixian|8698", "淮滨": "huaibinxian|8702", "邓州": "dengzhou|595",
                "新野": "xinye|603"
            },
            "黑龙江": {
                "哈尔滨": "hrb|202", "大庆": "dq|375", "齐齐哈尔": "qqhr|5853", "牡丹江": "mdj|3489", "绥化": "suihua|6718",
                "佳木斯": "jms|6776", "鸡西": "jixi|7289", "双鸭山": "sys|9837", "鹤岗": "hegang|9061", "黑河": "heihe|9862",
                "伊春": "yich|9773", "七台河": "qth|9848", "大兴安岭": "dxal|9878", "安达": "shanda|6720", "肇东": "shzhaodong|6721",
                "肇州": "zhaozhou|382"
            },
            "湖北": {
                "武汉": "wh|158", "宜昌": "yc|858", "襄阳": "xf|891", "荆州": "jingzhou|3479", "十堰": "shiyan|2032",
                "黄石": "hshi|1734", "孝感": "xiaogan|3434", "黄冈": "hg|2299", "恩施": "es|2302", "荆门": "jingmen|2296",
                "咸宁": "xianning|9617", "鄂州": "ez|9709", "随州": "suizhou|9656", "潜江": "qianjiang|9669", "天门": "tm|9517",
                "仙桃": "xiantao|9736", "神农架": "snj|9605", "宜都": "yidou|864", "汉川": "hanchuan|3439", "枣阳": "zaoyang|896",
                "武穴": "wuxueshi|7362", "钟祥": "zhongxiangshi|9119", "京山": "jingshanxian|9117", "沙洋": "shayangxian|9118",
                "松滋": "songzi|3484",
                "广水": "guangshuishi|9657", "赤壁": "chibishi|9623", "老河口": "laohekou|895", "谷城": "gucheng|899",
                "宜城": "yichengshi|897",
                "南漳": "nanzhang|898", "云梦": "yunmeng|3438", "安陆": "anlu|3442", "大悟": "dawu|3437",
                "孝昌": "xiaochang|3436",
                "当阳": "dangyang|865", "枝江": "zhijiang|866", "嘉鱼": "jiayuxian|9624", "随县": "suixia|9660"
            },
            "湖南": {
                "长沙": "cs|414", "株洲": "zhuzhou|1086", "益阳": "yiyang|10198", "常德": "changde|872", "衡阳": "hy|914",
                "湘潭": "xiangtan|2047", "岳阳": "yy|821", "郴州": "chenzhou|5695", "邵阳": "shaoyang|2303", "怀化": "hh|5756",
                "永州": "yongzhou|2307", "娄底": "ld|9481", "湘西": "xiangxi|10219", "张家界": "zjj|6788", "醴陵": "liling|1091",
                "澧县": "lixian|876", "桂阳": "czguiyang|5699", "资兴": "zixing|5698", "永兴": "yongxing|5701",
                "常宁": "changningshi|921",
                "祁东": "qidongxian|5690", "衡东": "hengdong|5693", "冷水江": "lengshuijiangshi|9470",
                "涟源": "lianyuanshi|9471",
                "双峰": "shuangfengxian|9473",
                "邵阳县": "shaoyangxian|6955", "邵东": "shaodongxian|6954", "沅江": "yuanjiangs|10201", "南县": "nanxian|10202",
                "祁阳": "qiyang|8532",
                "湘阴": "xiangyin|828", "华容": "huarong|830", "慈利": "cilixian|6791", "攸县": "zzyouxian|1095"
            },
            "河北": {
                "石家庄": "sjz|241", "保定": "bd|424", "唐山": "ts|276", "廊坊": "lf|772", "邯郸": "hd|572",
                "秦皇岛": "qhd|1078", "沧州": "cangzhou|652", "邢台": "xt|751", "衡水": "hs|993", "张家口": "zjk|3328",
                "承德": "chengde|6760", "定州": "dingzhou|8398", "馆陶": "gt|8706", "张北": "zhangbei|11201", "赵县": "zx|9048",
                "正定": "zd|3198", "迁安市": "qianan|284", "任丘": "renqiu|656", "三河": "sanhe|776", "武安": "wuan|577",
                "雄安新区": "xionganxinqu|111234", "燕郊": "lfyanjiao|12730", "涿州": "zhuozhou|428", "河间": "hejian|658",
                "黄骅": "huanghua|657",
                "沧县": "cangxian|659", "磁县": "cixian|591", "涉县": "shexian|14059", "霸州": "bazhou|775",
                "香河": "xianghe|5395",
                "固安": "lfguan|12803", "遵化市": "zunhua|283", "迁西": "qianxixian|7061", "玉田": "yutianxian|7060",
                "滦南": "luannanxian|7066",
                "沙河": "shaheshi|755"
            },
            "江苏": {
                "苏州": "su|5", "南京": "nj|172", "无锡": "wx|93", "常州": "cz|463", "徐州": "xz|471",
                "南通": "nt|394", "扬州": "yz|637", "盐城": "yancheng|613", "淮安": "ha|968", "连云港": "lyg|2049",
                "泰州": "taizhou|693", "宿迁": "suqian|2350", "镇江": "zj|645", "沭阳": "shuyang|5772", "大丰": "dafeng|11279",
                "如皋": "rugao|397", "启东": "qidong|400", "溧阳": "liyang|469", "海门": "haimen|399", "东海": "donghai|2147",
                "扬中": "yangzhong|649", "兴化": "xinghuashi|699", "新沂": "xinyishi|478", "泰兴": "taixing|696",
                "如东": "rudong|402",
                "邳州": "pizhou|477", "沛县": "xzpeixian|11349", "靖江": "jingjiang|698", "建湖": "jianhu|618",
                "海安": "haian|401",
                "东台": "dongtai|615", "丹阳": "danyang|648", "宝应县": "baoyingx|14451", "灌南": "guannan|2150",
                "灌云": "guanyun|2148",
                "姜堰": "jiangyan|697", "金坛": "jintan|468", "昆山": "szkunshan|16", "泗洪": "sihong|5958",
                "泗阳": "siyang|5959",
                "句容": "jurong|650", "射阳": "sheyang|621", "阜宁": "funingxian|620", "响水": "xiangshui|619",
                "盱眙": "xuyi|976",
                "金湖": "jinhu|975", "江阴": "jiangyins|34984"
            },
            "江西": {
                "南昌": "nc|669", "赣州": "ganzhou|2363", "九江": "jj|2247", "宜春": "yichun|5709", "吉安": "ja|2364",
                "上饶": "sr|10120", "萍乡": "px|2248", "抚州": "fuzhou|10134", "景德镇": "jdz|2360", "新余": "xinyu|10115",
                "鹰潭": "yingtan|3209", "永新": "yxx|11077", "乐平": "lepingshi|9048", "进贤": "jinxian|677",
                "分宜": "fenyi|10118",
                "丰城": "fengchengshi|5711", "樟树": "zhangshu|5713", "高安": "gaoan|5712", "余江": "yujiang|3210",
                "南城": "nanchengx|10137",
                "浮梁": "fuliangxian|9071"
            },
            "吉林": {
                "长春": "cc|319", "吉林": "jl|700", "四平": "sp|10171", "延边": "yanbian|3184", "松原": "songyuan|2315",
                "白城": "bc|5918", "通化": "th|10159", "白山": "baishan|10179", "辽源": "liaoyuan|2501",
                "公主岭": "gongzhuling|10171",
                "梅河口": "meihekou|10162", "扶余": "fuyuxian|9085", "长岭": "changlingxian|9084", "桦甸": "huadian|706",
                "磐石": "panshi|708",
                "梨树县": "lishu|10176"
            },
            "辽宁": {
                "沈阳": "sy|188", "大连": "dl|147", "鞍山": "as|523", "锦州": "jinzhou|2354", "抚顺": "fushun|5722",
                "营口": "yk|5898", "盘锦": "pj|2041", "朝阳": "cy|10106", "丹东": "dandong|3445", "辽阳": "liaoyang|2038",
                "本溪": "benxi|5845", "葫芦岛": "hld|10088", "铁岭": "tl|6729", "阜新": "fx|10097", "庄河": "pld|3306",
                "瓦房店": "wfd|3279", "灯塔": "dengta|2071", "凤城": "fengcheng|3450", "北票": "beipiao|10109",
                "开原": "kaiyuan|6733"
            },
            "宁夏": {
                "银川": "yinchuan|2054", "吴忠": "wuzhong|9962", "石嘴山": "szs|9971", "中卫": "zw|9951", "固原": "guyuan|2421"
            },
            "内蒙古": {
                "呼和浩特": "hu|811", "包头": "bt|801", "赤峰": "chifeng|6700", "鄂尔多斯": "erds|2037", "通辽": "tongliao|10015",
                "呼伦贝尔": "hlbe|10039", "巴彦淖尔市": "bycem|10070", "乌兰察布": "wlcb|9993", "锡林郭勒": "xl|2408", "兴安盟": "xam|9976",
                "乌海": "wuhai|2404", "阿拉善盟": "alsm|10083", "海拉尔": "hlr|2043"
            },
            "青海": {
                "西宁": "xn|2052", "海西": "hx|9902", "海北": "haibei|9917", "果洛": "guoluo|9936", "海东": "haidong|9909",
                "黄南": "huangnan|9896", "玉树": "ys|9888", "海南": "hainan|10574", "格尔木": "geermushi|9904"
            },
            "山东": {
                "青岛": "qd|122", "济南": "jn|265", "烟台": "yt|228", "潍坊": "wf|362", "临沂": "linyi|505",
                "淄博": "zb|385", "济宁": "jining|450", "泰安": "ta|686", "聊城": "lc|882", "威海": "weihai|518",
                "枣庄": "zaozhuang|961", "德州": "dz|728", "日照": "rizhao|3177", "东营": "dy|623", "菏泽": "heze|5632",
                "滨州": "bz|944", "莱芜": "lw|2292", "章丘": "zhangqiu|8680", "垦利": "kl|11313", "诸城": "zc|9146",
                "寿光": "shouguang|369", "龙口": "longkou|233", "曹县": "caoxian|5638", "单县": "shanxian|5636",
                "肥城": "feicheng|690",
                "高密": "gaomi|371", "广饶": "guangrao|627", "桓台": "huantaixian|7335", "莒县": "juxian|3180",
                "莱州": "laizhou|235",
                "蓬莱": "penglai|237", "青州": "qingzhou|367", "荣成": "rongcheng|522", "乳山": "rushan|520",
                "滕州": "tengzhou|967",
                "新泰": "xintai|689", "招远": "zhaoyuan|3325", "邹城": "zoucheng|455", "邹平": "zouping|946",
                "临清": "linqing|884",
                "茌平": "chiping|887", "郓城": "hzyc|5637", "博兴": "boxing|949", "东明": "dongming|5641", "巨野": "juye|5640",
                "无棣": "wudi|951", "齐河": "qihe|734", "微山": "weishan|459", "禹城": "yuchengshi|731", "临邑": "linyixianq|739",
                "乐陵": "leling|730", "莱阳": "laiyang|234", "宁津": "ningjin|733", "高唐": "gaotang|885", "莘县": "shenxian|888",
                "阳谷": "yanggu|886", "冠县": "guanxian|890", "平邑": "pingyi|514", "郯城": "tancheng|510",
                "沂源": "yiyuanxian|7334",
                "汶上": "wenshang|460", "梁山": "liangshanx|462", "利津": "lijin|628", "沂南": "yinanxian|7301",
                "栖霞": "qixia|238",
                "宁阳": "ningyang|691", "东平": "dongping|692", "昌邑": "changyishi|372", "安丘": "anqiu|370",
                "昌乐": "changle|373",
                "临朐": "linqu|374", "鄄城": "juancheng|5635"
            },
            "山西": {
                "太原": "ty|740", "临汾": "linfen|5669", "大同": "dt|6964", "运城": "yuncheng|5653", "晋中": "jz|8854",
                "长治": "changzhi|6921", "晋城": "jincheng|3350", "阳泉": "yq|8760", "吕梁": "lvliang|3222",
                "忻州": "xinzhou|3453",
                "朔州": "shuozhou|9871", "临猗": "linyixian|9193", "清徐": "qingxu|10908", "柳林": "liulin|3225",
                "高平": "gaoping|3354",
                "泽州": "zezhou|3353", "襄垣": "xiangyuanxian|6928", "孝义": "xiaoyi|3227"
            },
            "陕西": {
                "西安": "xa|483", "咸阳": "xianyang|7453", "宝鸡": "baoji|2044", "渭南": "wn|5733", "汉中": "hanzhong|3163",
                "榆林": "yl|5942", "延安": "yanan|8973", "安康": "ankang|3157", "商洛": "sl|9854", "铜川": "tc|9832",
                "神木": "shenmu|5944", "韩城": "hancheng|5735", "府谷": "fugu|5945", "靖边": "jingbian|5947",
                "定边": "dingbian|5948"
            },
            "四川": {
                "成都": "cd|102", "绵阳": "mianyang|1057", "德阳": "deyang|2373", "南充": "nanchong|2378", "宜宾": "yb|2380",
                "自贡": "zg|6745", "乐山": "ls|3237", "泸州": "luzhou|2372", "达州": "dazhou|9799", "内江": "scnj|5928",
                "遂宁": "suining|9688", "攀枝花": "panzhihua|2371", "眉山": "ms|9704", "广安": "ga|2381", "资阳": "zy|6803",
                "凉山": "liangshan|9717", "广元": "guangyuan|9749", "雅安": "ya|9687", "巴中": "bazhong|9811", "阿坝": "ab|9817",
                "甘孜": "ganzi|9764", "安岳": "anyuexian|6806", "广汉": "guanghanshi|8719", "简阳": "jianyangshi|6805",
                "仁寿": "renshouxian|9706",
                "射洪": "shehongxian|9694", "大竹": "dazu|9806", "宣汉": "xuanhan|9804", "渠县": "qux|9807",
                "长宁": "changningx|7148"
            },
            "新疆": {
                "乌鲁木齐": "xj|984", "昌吉": "changji|8582", "巴音郭楞": "bygl|9530", "伊犁": "yili|9472", "阿克苏": "aks|9499",
                "喀什": "ks|9326", "哈密": "hami|7452", "克拉玛依": "klmy|2042", "博尔塔拉": "betl|9529", "吐鲁番": "tlf|9475",
                "和田": "ht|9489", "石河子": "shz|9551", "克孜勒苏": "kzls|9519", "阿拉尔": "ale|9539", "五家渠": "wjq|9562",
                "图木舒克": "tmsk|9559", "库尔勒": "kel|7168", "阿勒泰": "alt|18837", "塔城": "tac|18845"
            },
            "西藏": {
                "拉萨": "lasa|2055", "日喀则": "rkz|9615", "山南": "sn|9576", "林芝": "linzhi|9646", "昌都": "changdu|9648",
                "那曲": "nq|9618", "阿里": "al|9678", "日土": "rituxian|9682", "改则": "gaizexian|9684"
            },
            "云南": {
                "昆明": "km|541", "曲靖": "qj|2389", "大理": "dali|2398", "红河": "honghe|2394", "玉溪": "yx|2040",
                "丽江": "lj|2392", "文山": "ws|2395", "楚雄": "cx|2393", "西双版纳": "bn|2397", "昭通": "zt|9409",
                "德宏": "dh|9437", "普洱": "pe|9444", "保山": "bs|2390", "临沧": "lincang|9422", "迪庆": "diqing|9432",
                "怒江": "nujiang|9462", "弥勒": "milexian|8892", "安宁": "anningshi|547", "宣威": "xuanwushi|7533"
            },
            "浙江": {
                "杭州": "hz|79", "宁波": "nb|135", "温州": "wz|330", "金华": "jh|531", "嘉兴": "jx|497",
                "台州": "tz|403", "绍兴": "sx|355", "湖州": "huzhou|831", "丽水": "lishui|7921", "衢州": "quzhou|6793",
                "舟山": "zhoushan|8481", "乐清": "yueqingcity|13950", "瑞安": "ruiancity|13951", "义乌": "yiwu|12291",
                "余姚": "yuyao|5333",
                "诸暨": "zhuji|357", "象山": "xiangshanxian|6738", "温岭": "wenling|408", "桐乡": "tongxiang|502",
                "慈溪": "cixi|5334",
                "长兴": "changxing|834", "嘉善": "jiashanx|14357", "海宁": "haining|500", "德清": "deqing|835",
                "东阳": "dongyang|536",
                "安吉": "anji|836", "苍南": "cangnanxian|7579", "临海": "linhai|407", "永康": "yongkang|537",
                "玉环": "yuhuan|409",
                "平湖": "pinghushi|501", "海盐": "haiyan|504", "武义县": "wuyix|14528", "嵊州": "shengzhou|359",
                "新昌": "xinchang|361",
                "江山": "jiangshanshi|6796", "平阳": "pingyangxian|7575"
            },
            "其他": {
                "香港": "hk|2050", "澳门": "am|9399", "台湾": "tw|2051"
            },
            "海外": {
                "洛杉矶": "gllosangeles", "旧金山": "glsanfrancisco", "纽约": "glnewyork", "多伦多": "gltoronto",
                "温哥华": "glvancouver",
                "伦敦": "glgreaterlondon", "莫斯科": "glmoscow", "首尔": "glseoul", "东京": "gltokyo", "新加坡": "glsingapore",
                "曼谷": "glbangkok", "清迈": "glchiangmai", "迪拜": "gldubai", "奥克兰": "glauckland", "悉尼": "glsydney",
                "墨尔本": "glmelbourne", "其他海外城市": "city"
            }
        }
        str_pname='省份列表：'
        for name in self.cityList:
            str_pname+="{}、".format(name)
        print(str_pname)
        self.province_name=input("请输入省份：")
        try:
            str_pname = '城市列表：'
            for name in self.cityList[self.province_name]:
                str_pname += "{}、".format(name)
            print(str_pname)
        except:
            print("没有该省份")

        self.city_name= input("请输入城市：")
        self.city_sx = self.cityList[self.province_name][self.city_name].split("|")[0]
        self.city_code = self.cityList[self.province_name][self.city_name].split("|")[1]

        self.quyu_dict = quyu(self.province_name, self.city_name)#这一部分是获取区域的code但并不全面，只能获取大城市的区域code，没有找到全部的接口，需要可自行去探索
        self.quyu=input("请输入区域：")
        self.quyu_code = self.quyu_dict[self.quyu][0]
        self.quyu_sx = self.quyu_dict[self.quyu][1]


        self.cate={
        "出租":("37031" ,"chuzu"),
        "整租":("8","zufang"),
        "合租":("10","hezu"),
        "二手房":(12,"ershoufang"),
        "品牌公寓":(0,"pinpaigongyu"),
        "短租":(9,"duanzu"),
        "商铺":(14,"shangpucz"),
        "写字楼":(13,"zhaozu"),
        "厂房":(15,"changfang")
        } # cate房子类型集合
        self.cate_name='出租' # cate房子类型
        self.cate_code=self.cate[self.cate_name][0]
        self.cate_sx=self.cate[self.cate_name][1]

    #GTID参数的加密模块
    def parse(self):
        f = 'list'
        y = "1,{}".format(self.cate_code) # cate房子类型code
        G = "{},{}".format(self.city_code,self.quyu_code) # area地区code

        #加密的js段
        jscode='''
        p=''
        h=''
        c=''
        
        var e = {
            
            getGTID: function(b, a, d) {
                function c(a, b, d) {
                    a = ("" + a).length < b ? (Array(b + 1).join("0") + a).slice(-b) : "" + a;
                    return -1 == d ? a : a.substring(0, d) + "-" + a.substring(d)
                }
                var e = {
                    home: "1",
                    index: "2",
                    list: "3",
                    detail: "4",
                    post: "5",
                    special: "6"
                };
                b = e[b] ? parseInt(e[b]).toString(16) : 0;
                a = a.split(",");
                a = a[a.length - 1];
                a = parseInt(a) ? parseInt(a).toString(16) : 0;
                d = d.split(",");
                d = d[d.length - 1];
                d = parseInt(d) ? parseInt(d).toString(16) : 0;
                e = (13).toString(16);
                return "llpccccc-tttt-txxx-xxxx-xxxxxxxxxxxx".replace(/x/g, function(a) {
                    return (16 * Math.random() | 0).toString(16)
                }).replace(/ccccc/, c(a, 5, -1)).replace(/tttt-t/, c(d, 5, 4)).replace(/p/, c(b, 1, -1)).replace(/ll/, c(e, 2, -1))
            }
            
         
        }'''
        js_e=execjs.compile(jscode)
        N=js_e.call("e.getGTID",f, y, G)
        print(N)
        return N

    # 请求页面模块
    def req(self):
        code=self.parse()
        url='https://sz.58.com/{}/{}/?PGTID={}'.format(self.quyu_sx,self.cate_sx,code)
        headers={}
        response=requests.get(url,headers=headers)
        # print(response.text)
        soup=BeautifulSoup(response.text,"lxml")
        box=soup.select(".list-box h2 a")
        for i in box:
            print(i.text.replace(" ",""))

if __name__ == '__main__':
    C=Crawl_58()
    C.req()
    # tt_html()