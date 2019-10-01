# 叮当快药 网址：http://www.ddky.com/

## 网站的js加密流程：

    主要是请求url中带了一个加密的参数 sign
    sign的js加密过程：
### 1、把时间戳、请求页面、药品类型的codes等拼接成字符串。
### 2、把该字符串用一个叫做"MD5"的方法加密一下
    该加密过程存在的js文件名（通过查找sign可以找到）,这里叫他 主js：http://www.ddky.com/D998449F20509FA6BC4A/js/ddkyutils.js?ddkycache=0fdfc085618a1365dea0610482de0424
    关键加密段：（在上面的js中查找sign可找到）
```
    for (var f = t.get("method") + p + r, y = MD5(f), v = e + "?sign=" + y, k = 0; k < l.length; k++)
    (t.get(l[k]) + "").indexOf("+") >= 0 || -1 != (t.get(l[k]) + "").indexOf("&") ? v += "&" + l[k] + "=" + encodeURIComponent(t.get(l[k])) : "pageUrl" == l[k] ? v += "&" + l[k] + "=" + encodeURIComponent(t.get(l[k])) : v += "&" + l[k] + "=" + t.get(l[k]);
    return v
```
            
    MD5 方法存在的js文件（上述js段点击可找到），这里叫他 MD5js

    画一下流程：1、网页及请求页面的信息 ——>2、通过 主js形成字符串，调用MD5js加密，返回sign ——> 3、主js 利用sign和请求信息生成url

## 破解思路：
    1、用python生成带请求信息的字符串 ——> 2、把MD5js 存成文件，再用execjs调用（传入字符串），返回sign ——> 3、python利用sign和其他信息生成url，请求即可！

## 总结：
    这种加密很直观，破解只要把MD5获取下来执行就行了，属于简单的js加密。
