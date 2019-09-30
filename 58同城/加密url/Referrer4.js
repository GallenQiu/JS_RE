(function(J) {
    var c = J
      , h = document
      , p = c.location
      , D = c.performance;
    if (!c.TJ58) {
        c.TJ58 = !0;
        null == c.String.prototype.trim && (c.String.prototype.trim = function() {
            return this.replace(/^\s\s*/, "").replace(/\s\s*$/, "")
        }
        );
        c.TJ58Obj = {};
        var e = {
            curURL: p.href,
            referrer: h.referrer,
            protocol: p.protocol,
            window_size: h.documentElement.clientWidth + "x" + h.documentElement.clientHeight,
            screen_size: c.screen.width + "," + c.screen.height,
            domain: function() {
                var b = p.host.toLowerCase()
                  , a = /.*?([^\.]+\.(com|org|net|biz|edu|cc)(\.[^\.]+)?)/;
                return a.test(b) ? "." + b.replace(a, "$1") : ""
            }(),
            navigation_type: function() {
                var b = "-1";
                try {
                    D && D.navigation && (b = D.navigation.type)
                } catch (a) {
                    return "-1"
                }
                return b
            }(),
            setCookie: function() {
                if (!h.cookie)
                    return !1;
                var b = new Date;
                2 < arguments.length ? b.setTime(b.getTime() + 864E5 * arguments[2]) : b.setTime(b.getTime() + 18E5);
                2 <= arguments.length && (h.cookie = arguments[0] + "=" + escape(arguments[1]) + "; expires=" + b.toGMTString() + "; domain=" + e.domain + "; path=/")
            },
            getCookie: function(b) {
                if (!h.cookie)
                    return "";
                var a;
                return (a = h.cookie.match(RegExp("(^| )" + b + "=([^;]*)(;|$)"))) ? unescape(a[2]) : ""
            },
            ajaxsend: function(b) {
                (new Image).src = b
            },
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
            },
            setLocalStorage: function(b, a) {
                try {
                    c.localStorage && c.localStorage.setItem(b, a)
                } catch (d) {}
            },
            getLocalStorage: function(b) {
                try {
                    return c.localStorage ? c.localStorage.getItem(b) : ""
                } catch (a) {
                    return ""
                }
            },
            getUUID: function(b) {
                var a = "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function(a) {
                    var b = 16 * c.Math.random() | 0;
                    return ("x" == a ? b : b & 3 | 8).toString(16)
                })
                  , a = this.getCookie(b) || this.getLocalStorage(b) || a;
                this.setCookie(b, a, 365);
                this.setLocalStorage(b, a);
                return a
            },
            getRandom: function() {
                return c.Math.random()
            },
            bindElem: function(b, a, d, e, m) {
                if (c.$ && "string" == typeof b && "string" == typeof a && "function" == typeof d)
                    if ("function" === typeof $(h).on)
                        $(h).on(a, b, d);
                    else
                        "function" === typeof $(h).delegate ? $(h).delegate(b, a, d) : "function" === typeof $(b).bind && $(b).bind(a, d)
            },
            loadScript: function(b, a) {
                try {
                    var d = h.createElement("script");
                    d.type = "text/javascript";
                    d.readyState ? d.onreadystatechange = function() {
                        if ("loaded" == d.readyState || "complete" == d.readyState)
                            d.onreadystatechange = null,
                            a && a()
                    }
                    : d.onload = function() {
                        a && a()
                    }
                    ;
                    d.src = b;
                    h.body.appendChild(d)
                } catch (c) {}
            },
            xxzlLoadJs: function(b) {
                function a() {
                    var a = h.createElement("script");
                    a.src = b;
                    h.body.appendChild(a)
                }
                c.addEventListener ? c.addEventListener("load", a, !1) : c.attachEvent ? c.attachEvent("onload", a) : c.onload = a
            }
        }
          , f = {
            config: {
                trackLog: {
                    server: "tracklog.58.com/pc/empty.js.gif",
                    allParams: "site_name tag referrer post_count _trackParams userid smsc window_size _ga_utma trackURL rand_id".split(" "),
                    uniqParams: ["tag", "rand_id"]
                },
                listShowLog: {
                    server: "tracklog.58.com/PCv1/listshow/empty.js.gif",
                    allParams: "tag bangbangid referrer site_name info_data trackURL rand_id".split(" "),
                    uniqParams: ["tag", "info_data", "rand_id"]
                },
                listClickLog: {
                    server: "tracklog.58.com/PCv1/listclick/empty.js.gif",
                    allParams: "tag bangbangid referrer site_name info_data trackURL ClickID rand_id".split(" "),
                    uniqParams: ["tag", "info_data", "rand_id"]
                },
                clickLog: {
                    server: "tracklog.58.com/pc/click/empty.js.gif",
                    allParams: "site_name tag from trackURL ClickID bangbangid referrer rand".split(" "),
                    uniqParams: ["tag", "from", "rand"]
                },
                diaTrackLog: {
                    server: "dialog.58.com/transfer",
                    allParams: "DIATag tag referrer post_count _trackParams userid smsc window_size _ga_utma trackURL rand_id".split(" "),
                    uniqParams: ["DIATag", "tag", "rand_id"]
                },
                diaClickLog: {
                    server: "dialog.58.com/transfer",
                    allParams: "DIATag from trackURL ClickID bangbangid referrer rand".split(" "),
                    uniqParams: ["DIATag", "from", "rand"]
                },
                diaShowLog: {
                    server: "dialog.58.com/transfer",
                    allParams: "DIATag trackURL ClickID bangbangid referrer rand".split(" "),
                    uniqParams: ["DIATag", "rand"]
                },
                gdtTrackLog: {
                    server: "gdt.cm.58.com/gdtcm",
                    allParams: ["city", "cate", "key", "plat"],
                    uniqParams: ["city", "key", "plat"]
                },
                gdtTrackLog2: {
                    server: "gdtcm.58.com/gdtcm",
                    allParams: ["city", "cate", "key", "plat"],
                    uniqParams: ["city", "key", "plat"]
                },
                actionLog: {
                    server: "tracklog.58.com/PCv1/action/empty.js.gif",
                    allParams: "site_name tag window_size action_data trackURL referrer rand_id".split(" "),
                    uniqParams: ["tag", "action_data", "rand_id"]
                }
            },
            filterList: function(b) {
                var a = ".58.com.cn portal.58.com faw-vw-dasweltauto.58.com 5858.com lieche.58.com dict.58.com/xiaoqu about.58.com m.58.com/city.html lieche.m.58.com".split(" "), d;
                for (d in a)
                    if (-1 !== b.indexOf(a[d]))
                        return "YES";
                return "NO"
            },
            getBaseInfo: function() {
                var b = c.site_name || "58"
                  , a = c.encodeURIComponent(e.referrer)
                  , d = e.curURL
                  , k = e.getUUID("58tj_uuid")
                  , m = e.getCookie("bangbangid")
                  , r = e.window_size
                  , g = e.navigation_type
                  , s = e.screen_size
                  , q = c.____json4fe ? c.____json4fe : {}
                  , f = q._trackPagetype || ""
                  , h = q._trackURL || ""
                  , n = q._trackParams || []
                  , l = q.GA_pageview || ""
                  , p = q.infoid || ""
                  , D = q.userid || ""
                  , O = q.smsc || ""
                  , q = q.sid || ""
                  , x = c._trackURL || h || "NA"
                  , u = {};
                try {
                    u = "NA" === x ? {} : eval("(" + x + ")")
                } catch (T) {
                    u = {}
                }
                var f = u.pagetype || f || c.page_type || "NA"
                  , h = u.post_count || c.post_count || -1
                  , l = u.Ga_pageview || l || ""
                  , y = u.cate || ""
                  , P = "" === y ? "" : y.split(",")[0]
                  , Q = "" === y && -1 === y.indexOf(",") ? "" : y.split(",")[1]
                  , G = u.area || ""
                  , M = "" === G ? "" : G.split(",")[0]
                  , N = e.getGTID(f, y, G)
                  , R = u.ROI || ""
                  , u = u.teemo || ""
                  , t = c._trackParams || n || []
                  , z = []
                  , n = "";
                if (t instanceof Array) {
                    for (var n = 0, K = t.length; n < K; n++)
                        t[n] && t[n].I && t[n].V && "string" === typeof t[n].V && z.push(t[n].I + ":" + t[n].V.replace(/\|/g, "*"));
                    n = encodeURIComponent(z.join("@@"))
                }
                var z = (t = e.curURL.match(/[\?&]iuType=[a-z]*_[0-9]*/)) ? t[0].split("=")[1].split("_") : ["", ""], t = z[0], z = z[1], K = e.getCookie("als"), E = e.getCookie("utm_source"), S = e.getCookie("utm_campaign"), F = e.getCookie("spm"), A, C, H;
                "" != e.getCookie("new_session") ? (A = e.getCookie("init_refer"),
                C = "0") : (A = c.encodeURIComponent(e.referrer),
                C = "1");
                H = "" != e.getCookie("new_uv") ? parseInt(e.getCookie("new_uv")) + ("0" == C ? 0 : 1) : 1;
                e.setCookie("new_session", C);
                e.setCookie("new_uv", H, 365);
                var B = e.referrer.split("/")[2] || ""
                  , v = this.getValByUrl(e.curURL, "utm_source")
                  , w = this.getValByUrl(e.curURL, "spm");
                if (!e.referrer && ("NA" != v || "NA" != w))
                    A = "",
                    E = "NA" === v ? "" : v,
                    F = "NA" === w ? "" : w;
                else if (!e.referrer && "NA" == v && "NA" == w && "1" === C)
                    F = E = A = "";
                else if (B) {
                    var L = !1;
                    "cast.58.com" == B ? L = !0 : -1 === B.indexOf(".58.com") && -1 === B.indexOf(".5858.com") && -1 === B.indexOf(".58cdn.com.cn") && (L = !0);
                    L && (A = J.encodeURIComponent(e.referrer),
                    E = "NA" === v ? "" : v,
                    F = "NA" === w ? "" : w)
                }
                e.setCookie("utm_source", E);
                e.setCookie("spm", F);
                e.setCookie("init_refer", A);
                var B = "1.1.1.1.1." + H, v = [], w = x.indexOf("{"), g = {
                    GTID: N,
                    infoid: p,
                    infotype: t,
                    usertype: z,
                    als: K,
                    utm_source: E,
                    utm_campaign: S,
                    spm: F,
                    new_session: C,
                    init_refer: A,
                    new_uv: H,
                    UUID: k,
                    bangbangid: m,
                    navtype: g,
                    sc: s,
                    sid: q
                }, I;
                for (I in g)
                    g.hasOwnProperty(I) && v.push("'" + I + "':'" + g[I] + "'");
                v.join(",");
                x = "NA" !== x && -1 !== w ? x.substring(0, w + 1) + v + "," + x.substring(w + 1) : "{" + v + "}";
                return {
                    site_name: b,
                    referrer: a,
                    UUID: k,
                    bangbangid: m,
                    pagetype: f,
                    post_count: h,
                    cate: y,
                    cate1: P,
                    cate2: Q,
                    area: G,
                    area1: M,
                    city: M,
                    GTID: N,
                    ClickID: 1,
                    ROI: R,
                    curURL: d,
                    _trackParams: n,
                    userid: D,
                    smsc: O,
                    window_size: r,
                    trackURL: x,
                    Ga_pageview: l,
                    _ga_utma: B,
                    ClickIDPlus: function() {
                        this.ClickID += 1
                    },
                    teemo: u
                }
            },
            getValByUrl: function(b, a) {
                var d;
                d = b.match(RegExp("[&?]" + a + "=([^&|^#]*)"));
                return d instanceof Array ? d[1] : "NA"
            },
            sendLog: function(b, a) {
                var d = this.baseInfo
                  , c = this.config[b];
                if (b && c && a && "object" === typeof a) {
                    for (var m = [], r = c.allParams, g = 0, s = r.length; g < s; g++)
                        m.push(r[g] + "=" + (a[r[g]] || d[r[g]] || ""));
                    e.ajaxsend(e.protocol + "//" + c.server + "?" + m.join("&"))
                }
            },
            trackLog: function() {
                var b = this.baseInfo;
                this.sendLog("trackLog", {
                    tag: "pvstatall",
                    rand_id: e.getRandom()
                });
                if ("list" === b.pagetype || "detail" === b.pagetype) {
                    var a = b.Ga_pageview.indexOf("?key=")
                      , a = -1 !== a ? b.Ga_pageview.substring(a + 5) : "";
                    "https:" == e.protocol ? this.sendLog("gdtTrackLog2", {
                        city: b.area,
                        key: a,
                        plat: "PC"
                    }) : this.sendLog("gdtTrackLog", {
                        city: b.area,
                        key: a,
                        plat: "PC"
                    })
                }
            },
            clickLog: function(b) {
                var a = ""
                  , a = null != b && "from=" === b.substring(0, 5) ? b.replace("from=", "") : "default&" + b;
                this.sendLog("clickLog", {
                    tag: "pvsiters",
                    from: a,
                    rand: e.getRandom()
                });
                setTimeout("GCIDPlus()", 300)
            },
            listClickLog: function() {
                var b = this
                  , a = this.baseInfo;
                if (c.$ && "NA" !== a.pagetype && "NA" !== a.trackURL) {
                    var d = {
                        list: 1,
                        jianli_list: 1,
                        xiaoqu: 1,
                        qijiandian: 1,
                        item: 1,
                        xinchong: 1
                    }
                      , k = function() {
                        if ("function" == typeof $(this).parents) {
                            var d = ""
                              , d = $(this).parents("[logr]")
                              , g = []
                              , c = ""
                              , k = d.attr("logr").split("_")
                              , m = d.attr("_pos")
                              , f = d.attr("sortid")
                              , h = d.attr("infoproperty")
                              , l = k[k.length - 1];
                            g.push(k[0], k[1], k[2], k[3]);
                            l && (l = l.replace("ses^", "ses:"),
                            c += l);
                            l = "";
                            l = "function" == typeof $("[logr]").index ? $("[logr]").index(d) + 1 : d.attr("pos");
                            c = c + (f ? "@sortid:" + f : "") + (l ? "@pos:" + l : "");
                            c += m ? "@npos:" + m : "";
                            c += h ? "@infoproperty:" + h : "";
                            "" != c && (0 === c.indexOf("@") && (c = c.substring(1)),
                            g.push(c));
                            d = g.join("_");
                            "NO" == b.filterList(a.curURL) && -1 != a.curURL.indexOf(".58.com") && (g = $(this).attr("href") || "#",
                            -1 != g.indexOf("javascript:") || "#" == g.substring(0, 1) || "NO" != b.filterList(g) || "/" != g.substring(0, 1) && -1 == g.indexOf(".58.com") || g.match(/[\?&]iuType=/) || $(this).attr("href", g.trim() + (-1 == g.indexOf("?") ? "?" : "&") + "iuType=" + k[0] + "_" + k[1]));
                            b.sendLog("listClickLog", {
                                tag: "pclistclick",
                                info_data: d,
                                rand_id: e.getRandom()
                            });
                            setTimeout("GCIDPlus()", 300)
                        }
                    }
                      , m = $("[tongji_label=listclick]");
                    m && 0 < m.length ? $("[logr] [tongji_label=listclick]").bind("click", k) : 1 === d[a.pagetype] ? ($("[logr] a.t").bind("click", k),
                    "12" === a.cate2 ? ($("[logr] a.jjh_img").bind("click", k),
                    $("[logr] .img a").bind("click", k)) : "187" === a.cate1 || "42270" === a.cate1 ? $("[logr]").find("a:first").bind("click", k) : "9225" === a.cate1 || "13952" === a.cate1 ? $("[logr] a.fl").bind("click", k) : $("[logr] .img a").bind("click", k)) : "chexing" === a.pagetype && ($("[logr] a.at").bind("click", k),
                    $("[logr] .tdimg a").bind("click", k))
                }
            },
            listShowLog: function() {
                var b = this.baseInfo;
                if (c.$ && "list" === b.pagetype) {
                    for (var a = [], d = $("[logr]"), b = b.trackURL.length + b.referrer.length, k = 0, m = d.length; k < m; k++)
                        if ($(d[k]).attr("logr") && "function" == typeof $(d[k]).attr) {
                            var f = []
                              , g = ""
                              , s = $(d[k]).attr("logr").split("_")
                              , q = $(d[k]).attr("_pos")
                              , h = k + 1
                              , p = $(d[k]).attr("sortid")
                              , n = $(d[k]).attr("infoproperty")
                              , l = s[s.length - 1];
                            f.push(s[0], s[1], s[2], s[3]);
                            l && (l = l.replace("ses^", "ses:"),
                            g += l);
                            g += p ? "@sortid:" + p : "";
                            g += h ? "@pos:" + h : "";
                            g += q ? "@npos:" + q : "";
                            g += n ? "@infoproperty:" + n : "";
                            "" != g && (0 === g.indexOf("@") && (g = g.substring(1)),
                            f.push(g));
                            f = f.join("_");
                            curLogrLen = f.length;
                            g = a.join(",");
                            4096 < b + curLogrLen + g.length && (this.sendLog("listShowLog", {
                                tag: "pclistshow",
                                info_data: g,
                                rand_id: e.getRandom()
                            }),
                            a = []);
                            a.push(f)
                        }
                    0 != a.length && this.sendLog("listShowLog", {
                        tag: "pclistshow",
                        info_data: a.join(","),
                        rand_id: e.getRandom()
                    })
                }
            },
            bindTongji_tag: function() {
                if (c.$) {
                    var b = this;
                    e.bindElem("[tongji_tag]", "click", function() {
                        var a = $(this).attr("tongji_tag")
                          , d = $(this).text().trim();
                        b.clickLog("from=" + a + "&text=" + encodeURIComponent(d) + "&tongji_type=tongji_tag")
                    }, b)
                }
            },
            bindTongji_id: function() {
                if (c.$) {
                    var b = this;
                    e.bindElem("[tongji_id]", "click", function(a) {
                        var d = a.srcElement ? a.srcElement : a.target;
                        "A" == d.tagName.toUpperCase() && (a = $(d).attr("href") || "#",
                        d = $(d).text(),
                        -1 == a.indexOf("javascript:") && "#" != a.substring(0, 1) && b.clickLog("from=" + $(this).attr("tongji_id") + "&text=" + encodeURIComponent(d) + "&to=" + encodeURIComponent(a) + "&tongji_type=tongji_id"))
                    }, b)
                }
            },
            diaShowLog: function(b) {},
            bindAlsTag: function() {
                if (!e.getCookie("als") && c.$ && "function" === typeof $("body").one)
                    $("body").one("mouseover", function() {
                        e.setCookie("als", "0", 365)
                    });
                e.getCookie("isSpider") && e.setCookie("isSpider", "", 0)
            },
            bindHomeHeatMap: function() {
                var b = this
                  , a = this.baseInfo;
                c.$ && "home" === a.pagetype && e.bindElem("[href]", "click", function(a) {
                    var c = $(this).attr("href")
                      , e = $(this).text().trim()
                      , f = $(this).attr("tongji_tag") || "NA"
                      , g = $(this).offset().top
                      , s = $(this).offset().left
                      , h = a.pageX;
                    a = a.pageY;
                    b.clickLog("from=heatmap:" + encodeURIComponent(c) + "&tagX=" + s + "&tagY=" + g + "&mouseX=" + h + "&mouseY=" + a + "&text=" + encodeURIComponent(e) + "&tongji_tag=" + f)
                }, b)
            },
            insertMiGuan: function() {
                try {
                    var b = "default";
                    switch (this.baseInfo.cate1) {
                    case "9224":
                    case "9225":
                    case "13941":
                    case "13952":
                        b = "yewu";
                        break;
                    case "1":
                        b = "ershoufang";
                        break;
                    case "5":
                        b = "shouji";
                        break;
                    case "832":
                        b = "dog";
                        break;
                    case "4":
                        b = "ershouche";
                        break;
                    default:
                        b = "shenghuo"
                    }
                    var a = Math.ceil(1E14 * Math.random())
                      , d = document.getElementsByTagName("body")[0]
                      , c = document.createElement("div");
                    c.id = "addInfo";
                    c.style.display = "none";
                    var f = document.createElement("a");
                    f.href = e.protocol + "//tracklog.58.com/detail/pc/" + b + "/" + a + "x.shtml";
                    f.text = "\u63a8\u8350\u4fe1\u606f";
                    c.appendChild(f);
                    d.appendChild(c)
                } catch (h) {}
            },
            bindAddGTIDtoURL: function() {
                var b = this
                  , a = this.baseInfo;
                c.$ && e.bindElem("a", "click", function(c) {
                    if ("NO" == b.filterList(a.curURL) && -1 != a.curURL.indexOf(".58.com") && (c = $(this).attr("href") || "#",
                    -1 == c.indexOf("javascript:") && "#" != c.substring(0, 1) && "NO" == b.filterList(c) && ("/" == c.substring(0, 1) || -1 != c.indexOf(".58.com"))))
                        if (c.match(/[\?&]ClickID=\d*/))
                            $(this).attr("href", c.replace(/ClickID=\d*/, "ClickID=" + a.ClickID));
                        else {
                            var e = c.indexOf("?");
                            -1 != e && -1 != c.substring(e).indexOf("statmark=t") && -1 != c.substring(e).indexOf("#") ? (e = c.indexOf("statmark=t"),
                            $(this).attr("href", c.substring(0, e + 10) + "&PGTID=" + a.GTID + "&ClickID=" + a.ClickID + c.substring(e + 10))) : $(this).attr("href", c.trim() + (-1 == e ? "?" : "&") + "PGTID=" + a.GTID + "&ClickID=" + a.ClickID)
                        }
                }, b, a)
            },
            ActionObj: {
                data: []
            },
            actionFilter: function() {
                pagetypeArr = "home index list special jianli_index jianli_list reg PC_regist_sj".split(" ");
                var b = this.baseInfo, a = !1, c;
                for (c in pagetypeArr)
                    if (b.pagetype == pagetypeArr[c]) {
                        a = !0;
                        break
                    }
                return a ? !0 : !1
            },
            actionLog: function() {
                var b = this;
                b.actionFilter() && (e.bindElem("body", "click", function(a) {
                    var d = b.ActionObj.data
                      , k = h.body.scrollWidth || ""
                      , m = h.body.scrollHeight || "";
                    a = a || c.event;
                    var r = h.documentElement.scrollLeft || h.body.scrollLeft
                      , g = h.documentElement.scrollTop || h.body.scrollTop
                      , r = a.pageX || a.clientX + r || "-1";
                    a = a.pageY || a.clientY + g || "-1";
                    r = Math.floor(r);
                    a = Math.floor(a);
                    d.push("CLICK_" + k + "_" + m + "_" + r + "_" + a);
                    d instanceof Array && 5 <= d.length && (d = d.join(","),
                    f.ActionObj.data = [],
                    b.sendLog("actionLog", {
                        tag: "pcaction",
                        action_data: d,
                        rand_id: e.getRandom()
                    }))
                }),
                c.$ && $(c).unload(function() {
                    var a = b.ActionObj;
                    (a = a ? a.data : "") && a instanceof Array && 0 < a.length && (a = a.join(","),
                    f.ActionObj.data = [],
                    b.sendLog("actionLog", {
                        tag: "pcaction",
                        action_data: a,
                        rand_id: e.getRandom()
                    }))
                }))
            },
            performanceLog: function() {
                var b = this.baseInfo, a = !1, d = "home index list special post detail".split(" "), e;
                for (e in d)
                    if (b.pagetype == d[e]) {
                        a = !0;
                        break
                    }
                a && c.$ && c.performance && c.performance.timing && $(function() {
                    function a(b, c, d) {
                        return "number" === typeof b && "number" === typeof c ? (b -= c,
                        b = Math.floor(0 > b ? -1 : b),
                        -1 == b && d ? d : b) : -1
                    }
                    function b(d) {
                        var e = c.performance.timing
                          , e = {
                            loadPage: 0 == e.navigationStart ? a(e.loadEventEnd, e.fetchStart, d) : a(e.loadEventEnd, e.navigationStart, d),
                            domReady: a(e.domComplete, e.responseEnd, d),
                            redirect: a(e.redirectEnd, e.redirectStart, d),
                            lookupDomain: a(e.domainLookupEnd, e.domainLookupStart, d),
                            ttfb: 0 == e.navigationStart ? a(e.responseStart, e.fetchStart, d) : a(e.responseStart, e.navigationStart, d),
                            request: a(e.responseEnd, e.requestStart, d),
                            loadEvent: a(e.loadEventEnd, e.loadEventStart, d),
                            appcache: a(e.domainLookupStart, e.fetchStart, d),
                            unloadEvent: a(e.unloadEventEnd, e.unloadEventStart, d),
                            connect: a(e.connectEnd, e.connectStart, d),
                            DOMContentLoaded: a(e.domContentLoadedEventEnd, e.fetchStart, d)
                        };
                        d = [];
                        for (var f in e)
                            e.hasOwnProperty(f) && d.push("'" + f + "':'" + e[f] + "'");
                        d.join(",");
                        f = getTrackURL();
                        e = f.indexOf("{");
                        f = "NA" !== f && -1 !== e ? f.substring(0, e + 1) + d + "," + f.substring(e + 1) : "{" + d + "}";
                        d = [];
                        d.push("site_name=58");
                        d.push("tag=performance");
                        d.push("referrer=" + J.encodeURIComponent(document.referrer));
                        d.push("trackURL=" + f);
                        d.push("rand_id=" + c.Math.random());
                        d = p.protocol + "//tracklog.58.com/PCv1/performance/empty.js.gif?" + d.join("&");
                        (new Image).src = d;
                        c.TJ58Obj.send = !0;
                        clearInterval(c.TJ58Obj.PFORMINTERVAL)
                    }
                    c.TJ58Obj.PFORMCOUNT = -1;
                    c.TJ58Obj.send = !1;
                    $(c).unload(function() {
                        c.TJ58Obj.send || b("close_" + Math.floor(c.performance.now()))
                    });
                    c.TJ58Obj.PFORMINTERVAL = setInterval(function() {
                        c.TJ58Obj.PFORMCOUNT++;
                        6 < c.TJ58Obj.PFORMCOUNT && clearInterval(c.TJ58Obj.PFORMINTERVAL);
                        try {
                            0 < c.performance.timing.loadEventEnd ? b() : 6 <= c.TJ58Obj.PFORMCOUNT && b("TIMEOUT_" + Math.floor(c.performance.now()))
                        } catch (a) {
                            clearInterval(c.TJ58Obj.PFORMINTERVAL)
                        }
                    }, 500)
                })
            },
            DMloadByTag: function() {
                try {
                    var b = this.getValByUrl(e.curURL, "dm-statistic-detect")
                      , a = e.getCookie("dm-statistic-detect");
                    if (b = ("NA" == b ? "" : b) || a || "")
                        if (c.TJ58ecdata = {},
                        c.TJ58ecdata.platform = "58PC",
                        "https:" != p.protocol)
                            switch (b) {
                            case "2":
                                e.loadScript(p.protocol + "//stat.58corp.com/static/js/referrer_alert.js");
                                break;
                            case "3":
                                e.loadScript(p.protocol + "//stat.58corp.com/static/js/referrer_visual.js")
                            }
                } catch (d) {}
            },
            xxzlLoadFn: function() {
                try {
                    if ("t" == this.baseInfo.teemo) {
                        var b = (new Date).getTime();
                        e.xxzlLoadJs(p.protocol + "//j1.58cdn.com.cn/git/xxzl/teemo/teemo_init.js?dt=" + b + "&appkey=16c5ada45e84f37e6pc")
                    }
                } catch (a) {}
            }
        };
        f.baseInfo = f.getBaseInfo();
        f.trackLog();
        f.listShowLog();
        f.listClickLog();
        f.bindAlsTag();
        f.bindTongji_tag();
        f.bindTongji_id();
        f.bindHomeHeatMap();
        f.bindAddGTIDtoURL();
        f.insertMiGuan();
        f.actionLog();
        c.clickLog = function(b) {
            f.clickLog(b)
        }
        ;
        c.showLog = function(b) {
            f.diaShowLog(b)
        }
        ;
        c.GCIDPlus = function() {
            f.baseInfo.ClickIDPlus()
        }
        ;
        c.ajaxlogr = function(b) {}
        ;
        c.getGTID = function() {
            return f.baseInfo.GTID
        }
        ;
        c.getTrackURL = function() {
            return f.baseInfo.trackURL
        }
        ;
        c._gaq = c._gaq || [];
        f.performanceLog();
        f.xxzlLoadFn();
        f.DMloadByTag()
    }
}
)(window);
function parse() {


}