
'''
jsonpath的安装以及使用:
    pip 安装:
        在'PyCharm -> Settings -> Porject:{项目名} -> python Intergreter'找到python解释器的位置.比如在"D:\JavaDevTools\JetBrains\Python\Python310\python.exe"
        安装 lxml 到“D:\JavaDevTools\JetBrains\Python\Python310\Scripts”.打开终端,进入到此目录,然后运行以下命令.
        pip install jsonpath -i https://pypi.tuna.tsinghua.edu.cn/simple
    jsonpath的使用:
        obj =  json.load(open('json文件', 'r', encoding='utf-8'))
        ret = jsonpath.jsonpath(obj, 'jsonpath语法')

只能解析本地文件，解析不了服务器响应的文件

教程衔接: https://blog.csdn.net/luxideyao/article/details/77802389
'''

import json
import jsonpath

obj = json.load(open('073_jsonpath_usage.html.json', 'r', encoding='utf-8'))

# 获取书店所有书的作者. "$"代表 "{" , "*"代表所有, 也可以根据下表取值, 如 '$.store.book[1].author'
anthor_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
print(anthor_list)

# 获取所有的 price, ".."表示忽略上下级
anthor_list = jsonpath.jsonpath(obj, '$..price')
print(anthor_list)

# store 下面所有的元素
anthor_list = jsonpath.jsonpath(obj, '$.store.*')
print(anthor_list)

# store下面所有的 price
anthor_list = jsonpath.jsonpath(obj, '$.store..price')
print(anthor_list)

# 获取第三本书
anthor_list = jsonpath.jsonpath(obj, '$..book[2]')
print(anthor_list)

# 获取最后一本书
anthor_list = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
print(anthor_list)

# 获取前两本书
anthor_list = jsonpath.jsonpath(obj, '$..book[0,1]')
print(anthor_list)
anthor_list = jsonpath.jsonpath(obj, '$..book[:2]')
print(anthor_list)

# 过滤出所有的包含 isbn 的书. 提奥健过滤需要在括号的外面加上 ? 号.
anthor_list = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
print(anthor_list)

# 哪本书超过了10块钱
anthor_list = jsonpath.jsonpath(obj, '$..book[?(@.price > 10)]')
print(anthor_list)


# 074_尚硅谷_爬虫_解析_jsonpath解析淘票票

import urllib.request

url = "https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1740322030503_52&jsoncallback=jsonp53&action=cityAction&n_s=new&event_submit_doGetAllRegion=true"

headers = {
    # 带冒号的 header 不能用, 用了会报错
    # ':authority': 'www.taopiaopiao.com',
    # ':method': 'GET',
    # ':path': '/cityAction.json?activityId&_ksTS=1740323113831_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    # ':scheme': 'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 特别注意: 这里没有支持 urf-8, 要注释掉
    # 'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'bx-v': '2.5.28',
    'cookie': 'cna=ySVCIAtovloBASQOA7NpcLwe; xlly_s=1; tfstk=gbrnH79MgyuBWXNv95oCkYM5FObTdpiS_7K-w0hP7flsJ4lRR72z97cKwyQQZPVz12hE2wOkq8ls29wRNg4ugfFJ2JFJdPNY3HEdR0KoA0iPMsIADpwIV07d2M4SORysUOHFGGhVu0iPM1IADJwIVSswTPEzQOD-eHJUa2RNIYHE4HuyYFRZ1Yor42-rQFkIh3ky84WgQfMr4bPr8jxy8jEzul5Z9-3dYmoTjv0ngRbX43VeD2c4SfxPglDnajyEs3-o9gh9bR2dtnwtAuNmHWIwxS2bf5DaggfiV5azaYVNcQnQkWZjSWQVNJmnEqorSL-zID4_GuoV0CD_7JUzAWvk4vZLD4cjST-SycrxurPHFtwZYYPSluCXAXyzhoaxmGLE0R4zizjrVF82TxxSQTEwPUgECAcvOY-1Kzq3taBGIEeS8AMjMOXMP9gECAqAIOYf_2ksnuC..; isg=BMPDN1YAoJG41Wzl0hqyo-veUodtOFd6xxd3-PWgcyKZtOPWfQtYyugqLkT6FK9y',
    'priority': 'u=1, i',
    'referer': 'https://www.taopiaopiao.com/?tbpm=3',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
    'x-requested-with': 'XMLHttpRequest'
}

request = urllib.request.Request(url = url, headers=headers)
content = urllib.request.urlopen(request).read().decode('utf-8')

content = content.split('(')[1].split(')')[0]

with open('./074_json/tao_piao_piao.json', 'w', encoding='utf-8') as fp:
    fp.write(content)

obj = json.load(open('./074_json/tao_piao_piao.json', 'r', encoding='utf-8'))
region_names = jsonpath.jsonpath(obj, '$..regionName')
print(region_names)

