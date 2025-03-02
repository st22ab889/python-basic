import scrapy
# 编译器这里报错,但是不影响任何操作
from scrapy_dangdang_095.items import ScrapyDangdang095Item

class DangSpider(scrapy.Spider):
    name = "dang"
    # 如果是多页下载, 需要注意 allowed_domains 的范围, 也就是多页下载的域名是 allowed_domains 指定的域名 或其 子域名. 一般情况下, allowed_domains 里面只写域名
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/cp01.01.02.00.00.00.html"]

    base_url = 'https://category.dangdang.com/pg'
    page = 1

    def parse(self, response):
        # pipeline 下载数据; item 定义数据结构
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

        # 所有的 Selector 的对象, 都可以再次调用 xpath 方法
        li_list = response.xpath('//ul[@id="component_59"]/li')

        for li in li_list:
            src = li.xpath('.//img/@data-original').extract_first()
            if not src:
                src = li.xpath('.//img/@src').extract_first()
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()

            book = ScrapyDangdang095Item(src=src, name=name, price=price)
            # 获取一个book就将book交给pipelines.然后在管道中写保存数据的逻辑(使用管道前要在setting中开启管道, 也就是打开 ITEM_PIPELINES 这个字典)
            yield book
            print(src, name, price)

        # 多页下载逻辑
        if self.page <= 3:
            self.page += 1
            url = self.base_url + str(self.page ) + '-cp01.01.02.00.00.00.html'
            # 调用 parse 方法. scrapy.Request 就是 scrapy的get请求. url是其它页的地址; callback 是要运行的那个函数[注意:不需要加"()"号]
            yield scrapy.Request(url=url, callback=self.parse)

        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

