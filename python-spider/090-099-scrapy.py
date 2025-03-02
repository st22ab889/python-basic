'''
一.scrapy
    (1)scrapy是什么?
        Scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架。可以应用在包括数据挖掘，信息处理或存储历史数据等一系列的程序中。
    (2)安装scrapy:
        pip install scrapy -i https://pypi.tuna.tsinghua.edu.cn/simple
        安装过程中出错:
        如果安装有错误!!!!
        pip install scrapy
        building "twisted.test.raiser'extension
        error: Microsoft Visual c++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools

        解决方案:
            http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
            下载twisted对应版本的wh1文件(如我的Twisted-17.5.0-cp36-cp36m-win_amd64.wh1)，cp后面是python版本，amd64代表64位，运行命令:
                pip install c:\Users\...\Twisted-17.5.0-cp36-cp36m-win amd64.whl
                pip install scrapy
            如果再报错
                python -m pip install --upgrade pip
            如果再报错 win32
            解决方法:
                pip install pypiwin32
            再报错:使用 anaconda
                使用步骤:
                    打开 anaconda
                    点击 environments
                    点击 not installed
                    输入 scrapy
                    apply
                    在p ycharm 中选择 anaconda 的环境
                扩展:
                    anaconda 可以自动下载好依赖,不需要自己去解决.但是对爬虫来说, anaconda 是重量级的, 很多东西用不到
                    anaconda 下载安装好后, 需要在 PyCharm 里面改为引用 anaconda 的环境:
                        File -> Setting -> Project: {项目名称} -> Python Interpreter -> Python Interpreter: {anaconda的安装目录(也就是有 python.exe 这个文件的目录)}

二.scrapy项目的创建以及运行
    1.创建scrapy项目:
        终端输入
        scrapy startproject 项目名称
    2.项目组成:
        spiders
            init .py
            自定义的爬虫文件·Py               ---》由我们自己创建，是实现爬虫核心功能的文件
        __init__ .py
        items.py                            ---》定义数据结构的地方，是一个继承自scrapy.Item的类
        middlewares.py                      ---》中间件代理
        pipelines.py                        ---》管道文件，里面只有一个类，用于处理下载数据的后续处理, 默认是300优先级，值越小优先级越高(1-1000)
        settings.py                         ---》配置文件 比如:是否遵守robots协议，user-Agent定义等
    3.创建爬虫文件:
        (1)跳转到spiders文件夹cd 目录名字/目录名字/spiders
        (2)scrapy genspider 爬虫名字 网页的域名
            爬虫文件的基本组成:
                继承scrapy.spider类
                    name ='baidu                    ---》运行爬虫文件时使用的名字
                    allowed domains                 ---》爬虫允许的域名，在爬取的时候，如果不是此域名之下的url,会被过滤掉.
                    start_urls                      ---》声明了爬虫的起始地址，可以写多个ur1，一般是一个
                    parse(self，response)           ---》解析数据的回调函数
                        response.text                   ---》响应的是字符串
                        response.body                   ---》响应的是二进制文件
                        response.xpath()                ---》xpath方法的返回值类型是selector列表
                        extract()                       ---》提取的是selector对象的是data
                        extract_first()                 ---》提取的是selector列表中的第一个数据
    4.运行爬虫文件
        scrapy crawl 爬虫名称
        注意: 应在spiders文件夹内执行

三.scrapy架构组成
    (1)引擎            ---》自动运行，无需关注，会自动组织所有的请求对象，分发给下载器
    (2)下载器          ---》从引擎处获取到请求对象后，请求数据
    (3)spiders        ---》spider类定义了如何爬取某个(或某些)网站。包括了爬取的动作(例如:是否跟进链接)以及如何从网页的内容中提取结构化数据(爬取item)。 换句话说，spider就是您定义爬取的动作及分析某个网页(或者是有些网页)的地方,
    (4)调度器          ---》有自己的调度规则，无需关注
    (5)管道(Item pipeline)    ---》最终处理数据的管道，会预留接口供我们处理数据   当Item在spider中被收集之后，它将会被传递到Item Pipeline，一些组件会按照一定的顺序执行对Item的处理。每个item pipeline组件(有时称之为“Item pipeline”)是实现了简单方法的Python类。他们接收到Item并通过它执行一些行为，同时也决定此Item是否继续通过pipeline，或是被丢弃而不再进行处理。
            以下是item pipeline的一些典型应用:
            1.清理HTML数据
            2.验证爬取的数据(检查item包含某些字段)
            3.查重(并丢弃)
            4.将爬取结果保存到数据库中

四.scrapy工作原理
    1、引擎向spiders要ur
    2、引擎将要爬取的url给调度器
    3、调度器会将url生成请求对象放入到指定的队列中
    4、从队列中出队一个请求
    5、引学将请求交给下载器进行处理6、下载器发送请求获取互联网数据
    7、下载器将数据返回给引擎
    8、引擎将数据再次给到spiders9、spiders通过xpath解析该数据，得到数据或者url10、spiders将数据或者url给到引擎
    9、spiders通过xpath解析该数据，得到数据或者url
    10、spiders将数据或者ur给到引擎
    11、引学判断该数据还是url，是数据，交给管道(itempipeline)处理，是url交给调度器处理

注意. 本次所有的案例都是基于  2.12.0 版本的 scrapy , 之前的一些 scrapy 版本需要注意的是:
     1. 创建爬虫文件时 url 不要加 "http://" 或 "https://" 前缀
        scrapy genspider baidu www.baidu.com
     2. 如果 url 的结尾是以 ".html" 结尾的,  genspider 会在生成的爬虫文件的 start_urls 中的 url 会自动在 ".html" 加上 "/", 变成".html/", 需要手动删除这个"/", 否则运行的时候会报错
        scrapy genspider baidu www.baidu.com
'''
# 090_尚硅谷_爬虫_scrapy_安装
# 安装方法以及安装过程中报错的解决方法

# 091_尚硅谷_爬虫_scrapy_基本使用
'''
此案列的 scrapy 版本是 2.12.0

1.进入到想要创建 scrapy 项目的目录,使用终端命令创建. 项目名不能以'数字'开头. 也不能包含中文
    # scrapy startproject {项目的名字}
    scrapy startproject scrapy_baidu_091    
2.在"{项目名}/{项目名}/spiders"目录下使用终端创建爬虫文件, 一般情况下不用添加"http://"协议, 因为 scrapy 会自动加. 注意: 当前案列的scrapy版本可以加上协议
    # scrapy genspider 爬虫文件的名字 要爬取的网页
    scrapy genspider baidu www.baidu.com
3.在"{项目名}/{项目名}/spiders"目录下使用终端运行爬虫代码
    # scrapy crawl {爬虫的名字}
    scrapy crawl baidu
4.注释掉robots协议(是个君子协议，各大厂商互相有个约定，不能互相爬取数据 https://www.baidu.com/robots.txt)
     注释掉"../settings.py"文件中的"ROBOTSTXT_OBEY = True",或将此值设为 False'
    
'''


# 092_尚硅谷_爬虫_scrapy_58同城项目结构和基本方法
'''
此案列的 scrapy 版本是 2.12.0

scrapy startproject scrapy_wubatongcheng_092

scrapy genspider wubatc https://gz.58.com

注释掉robots协议

cd .\scrapy_wubatongcheng_092\scrapy_wubatongcheng_092\spiders

scrapy crawl wubatc
'''

'''
scrapy 项目的结构:
    项目名字
        项目名字
            spiders文件夹              存储的是爬虫文件,也就是自定义的文件
                 __init__.py
                自定义的爬虫文件        *核心功能文件
        __init__.py
        items.py                        定义数据结构的地方(爬取的数据都包含哪些)
        middleware                      中间件(代理机制)
        pipelines                       管道(用来处理下载的数据)
        settings                        配置文件(robots协议, ua定义等)
        
response的属性和方法:
    response.text             获取的是响应的是字符串
    response.body             获取的是二进制数据
    response.xpath            可以直接用xpath方法来解析response中的内容
    response.extract()        提取selector对象的data属性值, 也就是标签的data. 比如 <span>test</span> , test就是对象的data属性值.
                              在目前的 2.12.0版本的scrapy不需要extract()也能直接取到象的data属性值, 参考 scrapy_carhome_093.
    response.extract_first()  提取的是selector列表中的第一个数据
'''


# 093_尚硅谷_爬虫_scrapy_汽车之家scrapy工作原理
'''
# 此案列的 scrapy 版本是 2.12.0

scrapy startproject scrapy_carhome_093

scrapy genspider car https://www.autohome.com.cn/price/brandid_15

注释掉robots协议

cd .\scrapy_carhome_093\scrapy_carhome_093\spiders

scrapy crawl car

'''

# 094_尚硅谷_爬虫_scrapy_scrapyshell
'''
# 此案列的 scrapy 版本是 2.12.0

六.scrapy shell
    1.什么是scrapy shel1?
        Scrapy终端，是一个交互终端，供您在未启动spider的情况下尝试及调试您的爬取代码。其本意是用来测试提取数据的代码，不过您可以将其作为正常的Python终端，在上面测试任何的Python代码。
        该终端是用来测试xPath或css表达式，查看他们的工作方式及从爬取的网页中提取的数据。在编写您的spider时，该终端提供了交互性测试您的表达式代码的功能，免去了每次修改后运行spider的麻烦。
        一旦熟悉了scrapy终端后，您会发现其在开发和调试spider时发挥的巨大作用。
    2.安装ipython
        安装:
            pip install ipython -i https://pypi.tuna.tsinghua.edu.cn/simple
        简介:
            如果您安装了 IPython Scrapy终端将使用 IPython(替代标准Pthon终端)。IPython 终端与其他相比更为强大，提供智能的自动补全，高亮输出，及其他特性。
    3.应用:
        (1)scrapy shell www.baidu.com
        (2)scrapy shell http://www.baidu.com
        (3)scrapy shell "http://www.baidu.com"
        (4)scrapy shell "www.baidu.com"
    语法:
        (1)response对象:
            response.body
            response.text
            response.url
            response.status
        (2)response的解析:
            response.xpath()        (常用)使用xpath路径查询特定元素，返回一个selector列表对象
            response.css()
                使用css selector查询元素，返回一个selector列表对象
                获取内容 :response.css('#su::text').extract first()
                获取属性 :response.css('#su::attr("value")').extract first()
        (3)selector对象(通过xpath方法调用返回的是seletor列表)
            extract()
                提取selector对象的值
                如果提取不到值 那么会报错
                使用xpath请求到的对象是一个selector对象，需要进一步使用extract()方法拆包，转换为unicode字符串
            extract_first()
                提取seletor列表中的第一个值
                如果提取不到值 会返回一个空值
                返回第一个解析到的值，如果列表为空，此种方法也不会报错，会返回一个空值
            xpath()
            css()       注意:每一个selector对象可以再次的去使用xpath或者css方法

注意：
    直接在window的终端中输入 scrapy shell 域名 就可以进入到scrapy shell的终端 
        scrapy shell www.baidu.com
    如果想看到一些高亮 或者 自动补全那么可以安装 ipython 
        pip install ipython -i https://pypi.tuna.tsinghua.edu.cn/simple
    使用 Scrapy 不建议使用bs4语法, 因为特别复杂
        a = response.css('#su::attr("value")')
    如果代码非常多，可以使用 scrapy shell 调试, 如果业务能力比较强、改错能力强, scrapy shell 用处就不太大.
'''

# example
'''
Windows PowerShell
版权所有（C） Microsoft Corporation。保留所有权利。

安装最新的 PowerShell，了解新功能和改进！https://aka.ms/PSWindows

PS C:\Users\Aaron J WU> scrapy shell www.baidu.com
2025-03-01 21:06:36 [scrapy.utils.log] INFO: Scrapy 2.12.0 started (bot: scrapybot)
2025-03-01 21:06:36 [scrapy.utils.log] INFO: Versions: lxml 5.3.1.0, libxml2 2.11.7, cssselect 1.2.0, parsel 1.10.0, w3lib 2.3.1, Twisted 24.11.0, Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)], pyOpenSSL 25.0.0 (OpenSSL 3.4.1 11 Feb 2025), cryptography 44.0.1, Platform Windows-10-10.0.22000-SP0
//......
2025-03-01 21:06:36 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://www.baidu.com> (referer: None)
[s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x000002CABC48F5B0>
[s]   item       {}
[s]   request    <GET http://www.baidu.com>
[s]   response   <200 http://www.baidu.com>
[s]   settings   <scrapy.settings.Settings object at 0x000002CABC48F370>
[s]   spider     <DefaultSpider 'default' at 0x2cabc8e6f80>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local objects
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser
2025-03-01 21:06:37 [asyncio] DEBUG: Using proactor: IocpProactor
In [1]: response.text
Out[1]: '<!DOCTYPE html>\r\n<!--STATUS OK--><html> ...... </html>\r\n'

2025-03-01 21:06:43 [asyncio] DEBUG: Using proactor: IocpProactor
In [2]: response.body
Out[2]: b'<!DOCTYPE html>\r\n<!--STATUS OK--><html> ...... </html>\r\n'

2025-03-01 21:06:48 [asyncio] DEBUG: Using proactor: IocpProactor
In [3]: response.url
Out[3]: 'http://www.baidu.com'

2025-03-01 21:06:51 [asyncio] DEBUG: Using proactor: IocpProactor
In [4]: response.status
Out[4]: 200

2025-03-01 21:06:55 [asyncio] DEBUG: Using proactor: IocpProactor
In [5]: a = response.xpath('//input[@id="su"]/@value')

2025-03-01 21:08:19 [asyncio] DEBUG: Using proactor: IocpProactor
In [6]: a
Out[6]: [<Selector query='//input[@id="su"]/@value' data='百度一下'>]

2025-03-01 21:08:38 [asyncio] DEBUG: Using proactor: IocpProactor
In [7]: a.extract_first()
Out[7]: '百度一下'

2025-03-01 21:10:36 [asyncio] DEBUG: Using proactor: IocpProactor
In [8]: a = response.css('#su::attr("value")')                          # 使用 Scrapy 不建议使用bs4语法, 因为特别复杂

2025-03-01 21:12:16 [asyncio] DEBUG: Using proactor: IocpProactor
In [9]: a
Out[9]: [<Selector query="descendant-or-self::*[@id = 'su']/@value" data='百度一下'>]

2025-03-01 21:12:17 [asyncio] DEBUG: Using proactor: IocpProactor
In [10]: a.extract_first()
Out[10]: '百度一下'

2025-03-01 21:12:24 [asyncio] DEBUG: Using proactor: IocpProactor
In [11]:
'''

# 095_尚硅谷_爬虫_scrapy_当当网爬取数据
'''
# 此案列的 scrapy 版本是 2.12.0

scrapy startproject scrapy_dangdang_095

scrapy genspider dang https://category.dangdang.com/cp01.01.02.00.00.00.html

注释掉robots协议

cd .\scrapy_dangdang_095\scrapy_dangdang_095\spiders

scrapy crawl dang
'''


'''
3.yield
    1.带有 yield 的函数不再是一个普通函数，而是一个生成器generator，可用于迭代
    2.yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值。重点是:下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行
    3.简要理解:vield就是return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开始
案例:
    1.当当网        (1)yield(2).管道封装(3).多条管道下载 (4)多页数据下载 
    2.电影天堂      (1)一个item包含多级页面的数据        
'''


# 096_尚硅谷_爬虫_scrapy_当当网管道封装
'''
需求: 一条管道下载 json 数据, 另外一条管道下载图片. 实现一边下载json数据,一边下载图片
参考: 
    ".\scrapy_dangdang_095\scrapy_dangdang_095\scrapy_dangdang_095\pipelines.py"
    ".\scrapy_dangdang_095\scrapy_dangdang_095\scrapy_dangdang_095\settings.py"

运行项目:
    cd .\scrapy_dangdang_095\scrapy_dangdang_095\spiders
    scrapy crawl dang
'''


# 097_尚硅谷_爬虫_scrapy_当当网开启多条管道下载
'''
需求: 下载多页数据
运行项目:    
    cd .\scrapy_dangdang_095\scrapy_dangdang_095\spiders
    scrapy crawl dang
'''

# 098_尚硅谷_爬虫_scrapy_当当网多页下载
'''
需求: 下载多页数据
参考：".\scrapy_dangdang_095\scrapy_dangdang_095\spiders\dang.py"

运行项目:    
    cd .\scrapy_dangdang_095\scrapy_dangdang_095\spiders
    scrapy crawl dang
'''

# 099_尚硅谷_爬虫_scrapy_电影天堂多页数据下载
'''
场景: 第一页是电影列表,这个列表显示了电影的名字. 每个名字点进去是电影的图片.
需求: 获取每个电影的名字以及图片, 所以本案例有了层级关系
注意: 如果在公司做项目, 遇到网速比较慢的情况, 可以和公司特殊申请

scrapy startproject scrapy_movie_099

scrapy genspider movie https://www.dydytt.net/html/gndy/china/index.html

cd .\scrapy_movie_099\scrapy_movie_099\spiders

scrapy crawl movie
'''