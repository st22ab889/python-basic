'''
4.Mysq!
    (1)下载(https://dev.mysal.com/downloads/windows/installer/5.7.html)
    (2)安装(https://iingvan.baidu.com/album/d7130635f1c77d13fdf475df.html)

5.pymysql的使用步骤
    (1). pip install pymysql
    (2). pymysql.connect(host,port,user,password,db,charset)
    (3). conn.cursor()
    (4). cursor.execute()

6.Crawlspider
    1.继承自scrapy.spider
    2.独门秘笈Crawlspider可以定义规则，再解析html内容的时候，可以根据链接规则提取出指定的链接，然后再向这些链接发送请求
        所以，如果有需要跟进链接的需求，意思就是爬取了网页之后，需要提取链接再次爬取，使用crawlspider是非常合适的
    3.提取链接
        链接提取器，在这里就可以写规则提取指定链接
            scrapy.linkextractors.LinkExtractor(
                allow=(),               # 正则表达式,提取符合正则的链接
                deny =(),               # (不用)正则表达式，不提取符合正则的链接
                allow domains =(),      # (不用)允许的域名
                deny domains =(),       # (不用)不允许的域名
                restrict_xpaths=(),     # xpath，提取符合xpath规则的链接
                restrict_css=()         # 提取符合选择器规则的链接
            )
    4.模拟使用
        正则用法:links1 =Linkextractor(allow=r'list 23 \d+\.html')
        xpath用法:links2 = Linkextractor(restrict xpaths=r'//div[@class="x"]')
        css用法:links3 =LinkExtractor(restrict css='.x')
    5.提取连接
        link.extract_links(response)
    6.注意事项
        【注1】callback只能写函数名字符串，callback='parse item
        【注2】在基本的spider中，如果重新发送请求，那里的callback写的是 callback=self.parse_item【注-稍后看】follow=true 是否跟进 就是按照提取连接规则进行提取

7.Crawlspider案例
    需求:读书网数据入库
    1.创建项目: scrapy startproject dushuproject
    2.跳转到spiders路径: cd \dushuproject\dushuproject\spiders
    3.创建爬虫类:  scrapy genspider -t crawl read www.dushu.com
    4.items
    5.spiders
    6.settings
    7.pipelines
        数据保存到本地
        数据保存到mysq1数据库

8.数据入库
    (1)settings配置参数:
        DB HOST ='192.168.231.128
        DB PORT = 3306
        DB USER ='root'
        DB PASSWORD ='1234'
        DB NAME = 'test'
        DB CHARSET ='utf8

    (2)管道配置
        from scrapy.utils.project import get project settings
        import pymysql
        class MysqlPipeline(object):
        # __init__ 方法和 open spider 的作用是一样的

9.日志信息和日志等级
    (1)日志级别:
        CRITICAL: 严重错误
        ERROR : 一般错误
        WARNING: 警告
        INFO: 一般信息
        DEBUG: 调试信息
        默认的日志等级是 DEBUG
        只要出现了 DEBUG 或者 DEBUG以上等级的日志, 那么这些日志将会打印
    (2)settings.py文件设置:
        默认的级别为 DEBUG，会显示上面所有的信息
        在配置文件中 settings.py
        LOG_FILE: 将屏幕显示的信息全部记录到文件中，屏幕不再显示，注意文件后缀一定是 ".log"
        LOG_LEVEL: 设置日志显示的等级，就是显示哪些，不显示哪些

10.scrapy的post请求
    (1)重写 start_requests 方法:
        def start_requests(self)
    (2) start_requests的返回值:
        scrapy.FormRequest(url=url, headers=headers, callback=self.parse_item, formdata=data)
            url: 要发送的post地址
            headers: 可以定制头信息
            callback: 回调函数
            formdata: post所携带的数据，这是一个字典

11.代理
    (1)到 settings.py中，打开一个选项
        DOWNLOADER_MIDDLEWARES={
            'postproject.middlewares.Proxy':543,
        }
    (2)到 middlewares.py 中写代码
        def process_request(self, request, spider):
            request.meta['proxy']='https://113.68.202.10:9999'
            return None
'''

# 100_尚硅谷_爬虫_scrapy_链接提取器的使用

# 需求: 根据正则表达式提取符合url规则的衔接

'''
Windows PowerShell
版权所有（C） Microsoft Corporation。保留所有权利。

安装最新的 PowerShell，了解新功能和改进！https://aka.ms/PSWindows

PS C:\Users\Aaron J WU> scrapy shell https://www.dushu.com/book/1188.html
2025-03-02 14:51:55 [scrapy.utils.log] INFO: Scrapy 2.12.0 started (bot: scrapybot)
2025-03-02 14:51:55 [scrapy.utils.log] INFO: Versions: lxml 5.3.1.0, libxml2 2.11.7, cssselect 1.2.0, parsel 1.10.0, w3lib 2.3.1, Twisted 24.11.0, Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)], pyOpenSSL 25.0.0 (OpenSSL 3.4.1 11 Feb 2025), cryptography 44.0.1, Platform Windows-10-10.0.22000-SP0
2025-03-02 14:51:55 [scrapy.addons] INFO: Enabled addons:
//......
2025-03-02 14:51:55 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.dushu.com/book/1188.html> (referer: None)
[s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x000001766B27F580>
[s]   item       {}
[s]   request    <GET https://www.dushu.com/book/1188.html>
[s]   response   <200 https://www.dushu.com/book/1188.html>
[s]   settings   <scrapy.settings.Settings object at 0x000001766B27F340>
[s]   spider     <DefaultSpider 'default' at 0x1766b6daf50>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local objects
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser
2025-03-02 14:51:56 [asyncio] DEBUG: Using proactor: IocpProactor
In [1]: from scrapy.linkextractors import LinkExtractor

2025-03-02 14:53:00 [asyncio] DEBUG: Using proactor: IocpProactor
In [2]: link = LinkExtractor

2025-03-02 15:08:41 [asyncio] DEBUG: Using proactor: IocpProactor
In [3]: link = LinkExtractor(allow=r'/book/1188_\d+\.html')

2025-03-02 15:11:06 [asyncio] DEBUG: Using proactor: IocpProactor
In [4]: link
Out[4]: <scrapy.linkextractors.lxmlhtml.LxmlLinkExtractor at 0x1766d9910c0>

2025-03-02 15:11:16 [asyncio] DEBUG: Using proactor: IocpProactor
In [5]: link.extract_links(response)
Out[5]:
[Link(url='https://www.dushu.com/book/1188_2.html', text='2', fragment='', nofollow=False),
 Link(url='https://www.dushu.com/book/1188_3.html', text='3', fragment='', nofollow=False),
 Link(url='https://www.dushu.com/book/1188_4.html', text='4', fragment='', nofollow=False),
 Link(url='https://www.dushu.com/book/1188_5.html', text='5', fragment='', nofollow=False),
 Link(url='https://www.dushu.com/book/1188_6.html', text='6', fragment='', nofollow=False),
 Link(url='https://www.dushu.com/book/1188_7.html', text='7', fragment='', nofollow=False),
 Link(url='https://www.dushu.com/book/1188_8.html', text='8', fragment='', nofollow=False),
 Link(url='https://www.dushu.com/book/1188_9.html', text='9', fragment='', nofollow=False),
 Link(url='https://www.dushu.com/book/1188_10.html', text='10', fragment='', nofollow=False),
 Link(url='https://www.dushu.com/book/1188_11.html', text='11', fragment='', nofollow=False),
 Link(url='https://www.dushu.com/book/1188_12.html', text='12', fragment='', nofollow=False),
 Link(url='https://www.dushu.com/book/1188_13.html', text='13', fragment='', nofollow=False)]

2025-03-02 15:19:59 [asyncio] DEBUG: Using proactor: IocpProactor
In [6]: link_1 = LinkExtractor(restrict_xpaths=r'//div[@class="pages"]/a')

2025-03-02 15:20:41 [asyncio] DEBUG: Using proactor: IocpProactor
In [7]: link_1.extract_links(response)
Out[8]:
[Link(url='https://www.dushu.com/book/1188_2.html', text='2', fragment='', nofollow=False),
 Link(url='https://www.dushu.com/book/1188_3.html', text='3', fragment='', nofollow=False),
 Link(url='https://www.dushu.com/book/1188_4.html', text='4', fragment='', nofollow=False),
 Link(url='https://www.dushu.com/book/1188_5.html', text='5', fragment='', nofollow=False),
 Link(url='https://www.dushu.com/book/1188_6.html', text='6', fragment='', nofollow=False),
 Link(url='https://www.dushu.com/book/1188_7.html', text='7', fragment='', nofollow=False),
 Link(url='https://www.dushu.com/book/1188_8.html', text='8', fragment='', nofollow=False),
 Link(url='https://www.dushu.com/book/1188_9.html', text='9', fragment='', nofollow=False),
 Link(url='https://www.dushu.com/book/1188_10.html', text='10', fragment='', nofollow=False),
 Link(url='https://www.dushu.com/book/1188_11.html', text='11', fragment='', nofollow=False),
 Link(url='https://www.dushu.com/book/1188_12.html', text='12', fragment='', nofollow=False),
 Link(url='https://www.dushu.com/book/1188_13.html', text='13', fragment='', nofollow=False)]

2025-03-02 15:20:42 [asyncio] DEBUG: Using proactor: IocpProactor
In [9]:
'''


# 101_尚硅谷_爬虫_scrapy_crawlspider读书网
#参考: .\scrapy_readbook_101\scrapy_readbook_101\spiders\book.json
'''  
cd python-spider
scrapy startproject scrapy_readbook_101
cd ./scrapy_readbook_101/scrapy_readbook_101/spiders
scrapy genspider -t crawl read https://www.dushu.com/book/1188.html
scrapy crawl read 
'''


# 102_尚硅谷_爬虫_scrapy_读书网数据入库和链接跟进
# linux 
'''
mysql -uroot -p1234
create database spider charset-utf-8
use spider
create table book(id int primary key auto_increment, name varchar(128), src varchar(128));
select * from book;
'''

# install pymysql
'''
pip install pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple
'''

# run
'''
参考：
    配置Mysql参数以及设置管道: ".\scrapy_readbook_101\scrapy_readbook_101\settings.py"
    封装Mysql: ".\scrapy_readbook_101\scrapy_readbook_101\pipelines.py"
 运行:
    cd ./scrapy_readbook_101/scrapy_readbook_101/spiders
    scrapy crawl read
'''


# 103_尚硅谷_爬虫_scrapy_日志信息以及日志级别
'''
参考: .\scrapy_log_103\scrapy_log_103\settings.py
注意：
    日志文件一定要有, 日志级别基本不会调整.
    只要配置了日志文件,日志就不会再打印到终端上,而是写到日志文件里.  
    
cd python-spider
scrapy startproject scrapy_log_103
cd ./scrapy_log_103/scrapy_log_103/spiders
scrapy genspider log https://www.baidu.com
scrapy crawl log
'''

# 104_尚硅谷_爬虫_scrapy_百度翻译post请求
'''
cd python-spider
scrapy startproject scrapy_post_104
cd ./scrapy_post_104/scrapy_post_104/spiders
scrapy genspider testpost https://fanyi.baidu.com/sug
scrapy crawl testpost
'''

