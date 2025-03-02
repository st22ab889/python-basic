'''
requests和urllib的作用几乎一样, 但是部分业务用requests更加方便

一.基本使用
    1.文档:
        官方文档
            http://cn.python-requests.org/zh_CN/latest/
        快速上手
            http://cn.python-requests.org/zh_CN/latest/user/quickstart.html
    2.安装
        pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
    3.response的属性以及类型
        类型                :models.Response
        r.text              :获取网站源码
        r.encoding          :访问或定制编码方式
        r.url               :获取请求的ur1
        r.content           :响应的字节类型
        r.status_code       :响应的状态码
        r.headers           :响应的头信息

二.get请求
    requests.get()
        eg:
            import requests
            url = 'http://www.baidu.com/s?'
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'
            }
            data = {
                'kw': '北京'
            }
            response = requests.get(url=url, params=data, headers=headers)
    定制参数
        参数使用params传递
        参数无需urlencode编码
        不需要请求对象的定制
        请求资源路径中?可加可不加

三.post请求
    requests.post()
    百度翻译:
    eg:
        import requests
        post_url = 'http://fanyi.baidu.com/sug'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'
        }
        data = {
            'kw': '北京'
        }
        r=requests.post(url = post_url, headers=headers, data=data)

    6: get和 post区别?
        1: get请求的参数名字是params, post请求的参数的名字是data
        2: 请求资源路径后面可以不加 ?
        3: 不需要手动编解码
        4: 不需要做请求对象的定制
'''


'''
# urllib
(1)一个类型以及六个方法
(2)get请求
(3)post请求百度翻译
(4)ajax的get请求
(5)ajax的post请求
(6)cookie登陆 微博
(7)代理

# requests
(1)一个类型以及六个属性
(2)get请求
(3)post请求
(4)代理
(5)cookie 验证码
'''

import requests

# 084_尚硅谷_爬虫_requests_基本使用
'''
https://requests.readthedocs.io/en/latest/
'''

# 此示例的 requests 的版本是 2.32.3
print(requests.__version__)

url = 'http://www.baidu.com'
response = requests.get(url)

# 一个类型和六个属性

# Response类型
print(type(response))

# 设置响应的编码格式, 解决乱码
# response.encoding = 'utf-8'

# 以字符串的形式返回的网页源码,之前的一些版本不设置编码会有乱码,此版本没有
# print(response.text)

# 返回访问的 url 地址
print(response.url)

# 返回的是二进制的数据(用的不多)
# print(response.content)

# 返回响应状态码
print(response.status_code)

# 返回响应头
print(response.headers)


# 085_尚硅谷_爬虫_requests_get请求

# url = 'https://www.baidu.com/s?'
# 请求资源路径中的"?"可以加也可以不加
url = 'https://www.baidu.com/s'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'
}
# 参数无需 urlencoding编码
data = {
    'kw': '北京'
}
# params 参数; kwargs 字典;
response = requests.get(url=url, params=data, headers=headers)
content = response.text
# print(content)


# 086_尚硅谷_爬虫_requests_post请求
import json
url = 'https://fanyi.baidu.com/sug'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'
}
data = {
    'kw': '编程语言'
}
try:
    # data 参数; kwargs 字典;
    response = requests.post(url=url, data=data, headers=headers)
    print(response.status_code)
    print(response.text)
    # 之前的一些json版本需要传 encoding 参数, 如 json.loads(response.text, encoding='utf-8')
    obj = json.loads(response.text)
    print(obj)
except Exception as e:
    print(e)


# 087_尚硅谷_爬虫_requests_代理

url = 'https://www.baidu.com/s?'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'
}
data = {
    'wd': 'ip'
}

proxy = {
    # 如果url中是http,这里就写http; url中是https,这里就写https.不一致有时候可能出问题.
    'https': '121.230.210.31:3256'
}

try:
    response = requests.get(url=url, params=data, headers=headers, proxies=proxy)
    content = response.text
    with open("./87_88_requests/proxy.html", 'w', encoding='utf-8') as fp:
        fp.write(content)
except Exception as e:
    print(e)


# 088_尚硅谷_爬虫_requests_cookie登陆古诗文网
'''
古诗文网登录界面: https://www.gushiwen.cn/user/login.aspx?from=http://www.gushiwen.cn/user/collect.aspx
需求:通过登陆 然后进入到主页面
难点:
      (1) 隐藏域：如此例中的"__VIEWSTATE 和 __VIEWSTATEGENERATOR", 一般情况下看不到数据,都是在页面的源码中,所以需要获取页面的源码,然后进行解析就可以获取
      (2) 验证码 
      (3) 可以加ddddocr(一款强大的开源OCR库)自动识别验证码内容
'''

'''
登录接口需要的data；
    # __VIEWSTATE 和 __VIEWSTATEGENERATOR 是一个可以变化的量. 但是在界面登录那里并没有看到传值. 一般看不到的数据都在页面的源码中, 在源码页面搜索即可. 以"__"为前缀的变量一般都是隐藏域.
    __VIEWSTATE: xeqQhhfyH7OE5AXEt7BNz+0+9f+d6BD8bwwybe16YOCZLeNVzYivcpMRZCg4wLsTb3U4X6JDOAvDXT+GehT1xQk/ovm+UFot3WWlCaRsueEGfIHW1kkE8Ns/B0rGG+G93VZUBjk3oXOLIx3i+MI0gQ1V2yc=
    __VIEWSTATEGENERATOR: C93BE1AE
    from: http://www.gushiwen.cn/user/collect.aspx
    email: 18926293659
    pwd: asdfasdfasdf
    # code 就是验证码
    code: 99B8
    denglu: 登录
'''

login_page = "https://www.gushiwen.cn/user/login.aspx?from=http://www.gushiwen.cn/user/collect.aspx"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'
}
response = requests.get(url=login_page, headers=headers)
content = response.text
# 解析页面源码,获取 __VIEWSTATE 和 __VIEWSTATEGENERATOR
from bs4 import BeautifulSoup
soup = BeautifulSoup(content, 'lxml')
# 一般大的网站都设置'隐藏域(隐藏标签),每次进到这个页面这些隐藏域的一些属性值可能都不一样'
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
# 获取验证码
code = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'https://so.gushiwen.cn' + code

# 注意：这里获取的验证码和登录时的验证码不一样，因为这个获取验证码这个地址是每访问一次都会变
# import urllib.request
# urllib.request.urlretrieve(url=code_url, filename='./87_88_requests/Verification_code.jpg')

# 通过session的访问值就能使请求变成一个对象
seesion = requests.session()
# 验证码的url的内容
response_code = seesion.get(code_url)
# 注意此时要使用二进制数据,因为要使用的是图片的下载
content_code = response_code.content
# wb的模式就是将二进制数据写入到文件，如果用IDE看不到图片，就进入到文件管理器中查看. (如果图片显示不了,下载图片之后要关闭文件. 这一点未验证)
with open("./87_88_requests/Verification_code.jpg", 'wb') as fp:
    fp.write(content_code)

# 查看验证码并手动输入
code_name = input('pls input Verification_code: ')

# 登录
login_api = 'https://www.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fwww.gushiwen.cn%2fuser%2fcollect.aspx'
login_data = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://www.gushiwen.cn/user/collect.aspx',
    'email': '1212315@qq.com',
    'pwd': 'gushiwenwang0101',
    'code': code_name,
    'denglu': '登录'
}

# 用这种方式 获取到的验证码 和 login 时返回的验证码是不一样的. 因为获取验证码 和 login 是两个请求, 验证码每访问一次都不一样
# login_response = requests.post(url=url, headers=headers, data=login_data)

# 使用session, 可以让 login 和 获取验证码 变成一个对象
login_response = seesion.post(url=url, headers=headers, data=login_data)

content_post = login_response.text
with open("./87_88_requests/gushiwenwang.html", 'w', encoding='utf-8') as fp:
    fp.write(content)


# 089_尚硅谷_爬虫_requests_超级鹰打码平台的使用
'''
企业级开发并不会认为输验证码内容, 需要找破解验证码的平台.比如超级鹰
超级鹰打码: https://www.chaojiying.com/
Python语言Demo下载: https://www.chaojiying.com/api-14.html
参考: ".\87_88_requests\chaojiying_Python\chaojiying.py"
'''



