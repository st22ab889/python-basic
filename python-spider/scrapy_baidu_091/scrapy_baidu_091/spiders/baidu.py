import scrapy


class BaiduSpider(scrapy.Spider):

    # 此案列的 scrapy 版本是 2.12.0
    print(scrapy.__version__)

    # 爬虫的名字, 用于运行爬虫的时候使用的值
    name = "baidu"
    # 允许访问的域名和其子域名
    allowed_domains = ["www.baidu.com"]
    # 起始的url地址,指的是第一次要访问的域名
    start_urls = ["https://www.baidu.com"]

    # 运行 start_urls 之后运行的方法,方法中的response就是返回的对象. 相当于 response = requests.get(url).
    def parse(self, response):
        print('如果此方法没有运行. 注释掉"../settings.py"文件中的"ROBOTSTXT_OBEY = True",或将此值设为 False')
        pass
