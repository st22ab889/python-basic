
import urllib.request
import urllib.error

# 066_尚硅谷_爬虫_urllib_handler处理器的基本使用
'''
不能定制请求头:
    urllib.request.urlopen(url)
可以定制请求头:
    urllib.request.Request(url, data, headers)
使用handle定制更高级的请求头:
    随着业务逻辑的复杂，请求对象的定制已经满足不了需求，因为动态 cookie(每次登录cookie都不一样) 和 代理 不能使用请求对象的定制。
'''
url = 'https://www.baidu.com'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'
}
request = urllib.request.Request(url, headers=headers)
handler = urllib.request.HTTPHandler()
opener = urllib.request.build_opener(handler)
response = opener.open(request)
content = response.read().decode('utf-8')
# print(content)


# 067_尚硅谷_爬虫_urllib_代理
'''
代理的常用功能：
    突破自身ip访问限制，访问国外站点。
    访问一些单位或团体内部资源。
    提高访问速度。通常代理服务器都设置一个较大的硬盘缓冲区，当访问时也将数据保存在缓冲区，其它用户再次访问相同信息时，则直接从缓冲区取出数据，这样就提高了访问速度。
    隐藏真实IP。上网者也可以通过这种方法隐藏自己的IP,免受攻击。

代码配置代理:
    创建 ProxyHandler 对象。

免费代理：https://www.kuaidaili.com/free/
'''
url = 'http://www.baidu.com/s?wd=ip'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'
}
request = urllib.request.Request(url, headers=headers)
proxies = {
    'http': '202.101.213.203:20771'
}
proxyHandler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(proxyHandler)
try:
    response = opener.open(request)
    content = response.read().decode('utf-8')
    # print(content)
    with open('test_proxy_ip.html', 'w', encoding='utf-8') as fp:
        fp.write(content)
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e}")
except urllib.error.URLError as e:
    print(f"URLError: {e}")

# 068_尚硅谷_爬虫_urllib_代理池
# 用列表定义代理池, 一般公司都有自己的代理池，随机使用
proxies_pool = [
    {'http': '103.82.132.103:18209'},
    {'http': '104.84.133.104:18209'},
    {'http': '105.85.134.105:18209'},
    {'http': '106.86.135.106:18209'}
]

import random
# 随机从代理池中选一个代理
proxies = random.choice(proxies_pool)
print(f"type:{type(proxies)} , proxies = {proxies}")
