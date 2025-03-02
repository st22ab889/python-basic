
# 本教程来自 "尚硅谷Python爬虫教程小白零基础速通（含python基础+爬虫案例）" : https://www.bilibili.com/video/BV1Db4y1m7Ho

'''
文件名千万不要跟要导入的报包名一样. form  "076_尚硅谷_爬虫_解析_bs4爬取星巴克数据"  "09:00"
'''

# 052_尚硅谷_爬虫_爬虫相关概念介绍
'''
爬虫核心:
    爬取网页
    解析数据
    难点: 爬虫和反爬虫之间的博弈
爬虫的用途:
    数据分析/人工数据集
    社交如案件冷启动
    舆情分析
    竞争对手监控
'''

import urllib.request

# 053_尚硅谷_爬虫_urllib_基本使用
# 案列：使用 urllib 获取百度首页的源码(urllib 是 python 自带的库)
url = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# read 方法返回的是字节形式的二进制数据(控制台打印的是b开头的数据, 如: b'<!DOC....')，进行编码后会读出原内容
content = response.read().decode('utf-8')

# print(content)


# 054_尚硅谷_爬虫_urllib_1个类型和6个方法

# response 类型是 <class 'http.client.HTTPResponse'>
print(type(response))

# 对于整个内容, read 是一个字节一个字节读. 如果写为 read(5) 表示只读5这个文档的前5个字节
content = response.read()

# 读取一行
content = response.readline()

# 每行依次读，直到读完
content = response.readlines()

# 拿 http 状态码
response.getcode()

# 拿 url 地址
response.geturl()

# get header
response.getheaders()


# 055_尚硅谷_爬虫_urllib_下载
url_page = 'http://www.baidu.com/s?wd=beauty'
# 直接写文件名"baidu.html", 文件将保存在此python文件同样的目录下
# urllib.request.urlretrieve(url_page, 'baidu.html')  # 也可以写为 urllib.request.urlretrieve(url = url_page, 'baidu.html')
# 加上相对路径或绝对路径可以保存在指定的目录下
# urllib.request.urlretrieve(url_page, './055_urlretrieve/baidu.html')

# 056_尚硅谷_爬虫_urllib_请求对象的定制
# url的组成: 协议 + 主机地址(域名) + 端口号 + 路径 + 参数 + 锚点(比如用在百度检索)
url = 'https://www.baidu.com'
response = urllib.request.urlopen(url)
content = response.read().decode('utf8')
# 这里打印出来的内容很少，因为网站反爬
# print(content)
'''
反爬手段一: UA(User-Agent)
User-Agent 请求头使服务器能够识别客户端的操作系统及版本、CPU类型、浏览器版本、浏览器内核、浏览器渲染引擎、浏览器语言、浏览器插件等
网上搜 UA 大全可以搜索到很多，也可以从浏览器的http请求的header中看到
'''
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
# print(response.read().decode('utf8'))



# 057_尚硅谷_爬虫_urllib_get请求的quote方法
'''
ASCII🐎 : 127个字符, 包含大小写英文字母、数字和其它一些符号, 占1个字节
GB2312: 中国制定的, 占两个字节
Unicode: 苏哦有的语言统一到一套编码中，解决乱码问题。现在操作系统和大多数编程语言都直接支持 Unicode
'''
# "%E7%89%8C%E7%A5%9E" 就是 "牌神" 的 Unicode 码, 这里只检索 Unicode 码， 如果直接写中文，运行程序的时候会报错
url = "https://www.baidu.com/s?wd=%E7%89%8C%E7%A5%9E"

import  urllib.parse
url_base = "https://www.baidu.com/s?wd="
param = urllib.parse.quote("牌神")
url_base += param
print(url_base)


# 058_尚硅谷_爬虫_urllib_get请求的urlencode方法

data = {
    'language': '牌神',
    'do': '爬虫'
}
# urlencode 适合多参数一起转Unicode
result = urllib.parse.urlencode(data)
# print(result)


# 059_尚硅谷_爬虫_urllib_post请求百度翻译
url = 'https://fanyi.baidu.com/sug'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'
}

data = {
    'kw': '编程语言'
}

# 直接使用这个 form_data 会报错"TypeError: POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str."
form_data = urllib.parse.urlencode(data)
# print(type(form_data))        # 结果是:   <class 'str'>
# print(form_data)              # 结果是:  kw=%E7%89%8C%E7%A5%9E
form_data = urllib.parse.urlencode(data).encode('utf-8')
# print(form_data)              # 结果是:  b'kw=%E7%89%8C%E7%A5%9E'

request = urllib.request.Request(url, form_data, headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

import json
obj = json.loads(content)
print(obj)

'''
post 请求的参数必须进行 urlencode 编码, 然后再进行 encode 编码
'''


# 060_尚硅谷_爬虫_urllib_post请求百度翻译之详细编译

# 此案例没有成功，因为最新的接口加入了反爬机制
url = 'https://fanyi.baidu.com/ait/text/translate'

headers = {
    # 在写爬虫的时候一定要注意: 接收的编码类型一定要为"utf-8"
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Acs-Token': '1740110795800_1740155349937_ID6y/ZrAC/F/OvvO7oRLEEMbQBTmwPxbp7nNlE9kmDCwpIRIM/trR6cVGx54soEANYlQ+M+nHI1/mqtCCh9dQQesTxmGzN5R5Ihb3Q+Bbpq2TQ3gPqEAgHLgK1Cd3QDc6iKxbR0BPP/WcTXuE2QsY92EKRHP8V1RWpb3cU7SrEsLGr3b4r8j3o1D95kjBr4wHd5cSN6XyvWBw6jmzqG188a7zc/vVvnhdZ7dglW0Ruq5NxXqwLrQ7szQ0Eg/PyB2e38u/CEW6TBuC0/Fst1myTezYl0yOGkv4nujwP6o3wtZsiwxOSJp5x8tpIK/ZvaxfrU+kHVQ9Wc4H7ZPj9JgN3pluRhfiB4EkSnDib3oyb6+RXL1wKGMMSAr1ZovwkSDnWoNdjg4X35lk6EU/yzN9nvGad3AKfNkwkHqIqVchmExZqMb7wrJ86cgOLNFADC0s4Pgg7Hj3MHbt1jDQ4JdicCbAm7vDwi6V6MF+Tjgqnw=',
    'Connection': 'keep-alive',
    'Content-Length': '159',
    'Content-Type': 'application/json',
    # 很多网站使用 Cookie 来作为反爬虫的 header, 但也可能添加其它header来反爬虫
    'Cookie': 'BIDUPSID=1BB0DE7D95079F542F5446FBFAB04B99; PSTM=1721828140; BAIDUID=6C9457CD722A89C1FE19A05843F36A73:FG=1; H_WISE_SIDS_BFESS=60277_61027_61668_61986_62055_62062_61880; MAWEBCUID=web_wiwLDoGvEpPhrKTyPLqoFjxfqyFMjGCYdUsylalWRHuLmEDXzJ; H_WISE_SIDS=60277_61027_61668_61986_62055_62062_61880_62114; ZFY=KKIEV9kYCpBofnOPGRn9dRe5OfcI:A1AJA3YOZ20SLws:C; BAIDUID_BFESS=6C9457CD722A89C1FE19A05843F36A73:FG=1; BA_HECTOR=2g818120a10h2lal8005a00kbosg0c1jrh9e91v; PSINO=6; delPer=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BCLID=2329470737958916562; BCLID_BFESS=2329470737958916562; BDSFRCVID=V_8OJexroGWIeXOJxWzeEHtYoFweG7bTDYrEOwXPsp3LGJLVvqHuEG0Pts1-dEu-S2OOogKK3gOTH4eX_gt26qgfED4ZSjabVyQatf8g0M5; BDSFRCVID_BFESS=V_8OJexroGWIeXOJxWzeEHtYoFweG7bTDYrEOwXPsp3LGJLVvqHuEG0Pts1-dEu-S2OOogKK3gOTH4eX_gt26qgfED4ZSjabVyQatf8g0M5; H_BDCLCKID_SF=tRAOoC_-tDvDqTrP-trf5DCShUFsLq4OB2Q-XPoO3M3zefnOyR7R24LkyhOk2M5f5mkf3fbgy4op8P3y0bb2DUA1y4vp-Jo7bmTxoUJ2-KDVeh5Gqq-KXU4ebPRiJ-b9Qg-J0xn75--KM4jTbxoUjhI9MxQaLJcIK6nhVn0MBCK0HPonHj_-ej3b3f; H_BDCLCKID_SF_BFESS=tRAOoC_-tDvDqTrP-trf5DCShUFsLq4OB2Q-XPoO3M3zefnOyR7R24LkyhOk2M5f5mkf3fbgy4op8P3y0bb2DUA1y4vp-Jo7bmTxoUJ2-KDVeh5Gqq-KXU4ebPRiJ-b9Qg-J0xn75--KM4jTbxoUjhI9MxQaLJcIK6nhVn0MBCK0HPonHj_-ej3b3f; ab_sr=1.0.1_ZmMxMWY4NjMzMjFlOWEzZGYxMzhlYjg3ZGU5MzZjYTM2ZTk0MjQxOWYwNzA2ODM4NWFhNDNlODRhNjlkMTFhNWUzNjlhMmUyMWRjNDRlNmZhYjM5NTI4ODkyOWNmMzMyMDViOTY3NTRlZDg5OTMyZTIwMGNjMWM3NTNlNWU3YmNiOTg1NTk2NzczNzRhYmQ5Y2ViMjkyOGU2M2VjMTM5ZDZkMjkyNzc4ZTAyZGU5ZjUwYzBkYTA2NzFhZWFmYjhiZTFkMDM5NDQ1MzA0ZGEyMDAxMTc5OGIyOGQ0MTMwYzQ=; H_PS_PSSID=60277_61027_61668_62114_62131_62156_62167_62177_62185_62186_62182_62195_62236_62230_62262; RT="z=1&dm=baidu.com&si=b66e3cad-d2c8-414c-875b-05e7b9e11ae4&ss=m7eyyc36&sl=6&tt=4sz&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=l64n"',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/mtpe-individual/multimodal?query=this%20is%20a%20bad%20%0Agood%0Abook&lang=en2zh&ext_channel=Aldtype',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'accept': 'text/event-stream',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

payload = {
    "query": "this is a nice book",
    "from": "en",
    "to": "zh",
    "reference": "",
    "corpusIds": [],
    "needPhonetic": True,
    "domain": "common"
}

payload = urllib.parse.urlencode(payload).encode('utf-8')
request = urllib.request.Request(url, payload, headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)

'''
参考 deepseek 的回答：
    提问: 没有登录到百度，也有  Acs-Token 这个header，并且每访问一次，这个值都会变化
    回答: 如果未登录百度，但请求头中仍然包含 Acs-Token，并且每次访问时该值都会变化，那么 Acs-Token 很可能是百度用于 反爬虫机制 或 会话跟踪 的动态令牌。以下是可能的原因和解决方法：
          ......
'''
