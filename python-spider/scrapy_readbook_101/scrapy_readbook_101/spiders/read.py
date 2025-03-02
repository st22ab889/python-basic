import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_readbook_101.items import ScrapyReadbook101Item

class ReadSpider(CrawlSpider):
    name = "read"
    allowed_domains = ["www.dushu.com"]
    # 使用这行会发现,本来有13页,结果值爬取了12的数据, 这是因为第一页的这个url不能被正则表达式"/book/1188_\d+\.html"匹配到
    # start_urls = ["https://www.dushu.com/book/1188.html"]
    # 通过测试可以发现"https://www.dushu.com/book/1188.html"和"https://www.dushu.com/book/1188_1.html"都是访问的第一页, 改为如下的 url, 就能被正则表达式"/book/1188_\d+\.html"匹配到
    start_urls = ["https://www.dushu.com/book/1188_1.html"]
    '''
    正则表达式 r"/book/1188_\d+\.html
       \d   表示数字
       +    表示一个或多个
       \.   表示给.转移,因为有时候"."匹配不到
    
    follow=True 表示跟进, 就是按照提取连接规则进行提取
        也就是说在这个"https://www.dushu.com/book/1188_1.html"页面只匹配到了13页的数据, 如果设置 follow=True, 就会根据表达式匹配的规则继续爬取14、15、...页的数据,一直到爬取不到.
    '''
    rules = (
        Rule(LinkExtractor(allow=r"/book/1188_\d+\.html"),
             callback="parse_item",
             follow=False),
    )

    def parse_item(self, response):
        # 以下注释为自动生成的源码
        #item = {}
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        # return item

        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

        img_list = response.xpath('//div[@class="bookslist"]//img')
        for img in img_list:
            name = img.xpath('./@alt').extract_first()
            # 如果标签里面属性出现了"data-original",要马上考虑到懒加载
            src = img.xpath('./@data-original').extract_first()

            book = ScrapyReadbook101Item(name=name, src=src)
            yield book

        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')


