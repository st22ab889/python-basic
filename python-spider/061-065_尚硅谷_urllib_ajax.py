
import urllib.request
import urllib.parse
import urllib.error

# 061_尚硅谷_爬虫_urllib_ajax的get请求豆瓣电影第一页
# 此案例没有成功，因为最新的接口加入了反爬机制

douban_movie = 'https://m.douban.com/rexxar/api/v2/movie/recommend?refresh=0&start=0&count=20&selected_categories=%7B%22%E7%B1%BB%E5%9E%8B%22:%22%E5%8A%A8%E4%BD%9C%22%7D&uncollect=false&tags=%E5%8A%A8%E4%BD%9C'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'
}

request = urllib.request.Request(douban_movie, headers=headers)
try:
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    # 下载数据到本地, 演示2种写法，下面是第一种:
    '''
    fp = open('movie.json', 'w', encoding='utf-8')
    fp.write(content)
    '''
    # 第二种写法(直接写文件名"61_movie.json", 文件将保存在此python文件同样的目录下, 加上相对路径或绝对路径可以保存在指定的目录下):
    with open('./061_062_063_open/61_movie.json', 'w', encoding='utf-8') as fp:
        fp.write(content)
except urllib.error.HTTPError as e:
    print(f"异常信息：{e}")


# 062_尚硅谷_爬虫_urllib_ajax的get请求豆瓣电影前10页
# 此案例没有成功，因为最新的接口加入了反爬机制

def create_request(page):
    base_url = "https://m.douban.com/rexxar/api/v2/movie/recommend?"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'
    }
    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }
    data = urllib.parse.urlencode(data)
    url = base_url + data
    print(url)
    return urllib.request.Request(url, headers=headers)


def get_content(request):
    return urllib.request.urlopen(request).read().decode('utf-8')


def down_load(name, page, content):
     with open(f'{name}_{page}.json', 'w', encoding='utf-8') as fp:
         fp.write(content)
    # 字符串相加时, “=”号两边的数据类型要一样
    # with open(name + '_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
    #    fp.write(content)


# 当作程序的入口
if __name__ == '__main__':
    start_page = int(input('输入起始的页面: '))
    end_page = int(input('输入结束的页面: '))
    # range 函数是左闭右开
    for page in range(start_page, end_page + 1):
        try:
            request = create_request(page)
            content = get_content(request)
            # down_load('62_movie', page, content)
            down_load('./061_062_063_open/62_movie', page, content)
        except urllib.error.HTTPError as e:
            print(f"异常信息: {e}")


# 063_尚硅谷_爬虫_urllib_ajax的post请求肯德基官网
def get_request(page):
    url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
        # x-requested-with 这个字段就是给 ajax 用的
        'x-requested-with': 'XMLHttpRequest'
    }
    data = {
        'cname': '广州',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10',
    }
    data = urllib.parse.urlencode(data).encode("utf-8")
    return urllib.request.Request(url, data, headers)


if __name__ == '__main__':
    start_page = int(input('输入起始的页面: '))
    end_page = int(input('输入结束的页面: '))
    for page in range(start_page, end_page +1):
        request = get_request(page)
        content = get_content(request)
        # down_load("kfc_address", page, content)
        down_load("./063_Json/kfc_address", page, content)

# 064_尚硅谷_爬虫_urllib_异常
'''
HTTPError类是URLError类的子类
异常有两类：
    HTTPError : 访问出错，比如服务器拒绝访问
    URLError  : 主机地址或参数错误
爬虫的项目用使用异常的地方并不多
'''


# 065_尚硅谷_爬虫_urllib_微博的cookie登陆
'''
适用场景，需要登录才能看到某个页面
网站常用的反爬手段：个人信息页面是 utf-8，但还是报编码错误。这个时候是因为并没有找到个人信息页面，而是跳转到登录页面，这个登录页面不是 urf-8
'''
'''
# example: 本例只是说明服务器返回的编码不一定是 urf-8, 所以在 decode 和 encoding 的时间要选实际的编码
# 忽略一些代码...
response = urllib.request.urlopen(request)
# 这里实际可能是返回的 gb2312
# content = response.read().decode('utf-8')
content = response.read().decode('gb2312')
with open('./061_062_063_open/example.json', 'w', encoding='ugb2312') as fp:
    fp.write(content)
'''

url = 'https://info.xxx.com/my/index'
headers = {
    # coockie 中包含登录信息，所以大多数网站只要携带cookie就可以正常登录. 但是也有很多网站使用动态 cookie
    'Cookie': '...',
    # Referer 判断当前路径是不是由上一个路径过来。一般情况下是做图片防盗链。也经常用来做 反爬虫识别
    'Referer': 'https://info.xxx.com'
}
request = urllib.request.Request(url, headers=headers)
try:
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    with open('./061_062_063_open/xxx.html', 'w', encoding='utf-8') as fp:
        fp.write(content)
except urllib.error.HTTPError as e:
    print(f"异常信息：{e}")

