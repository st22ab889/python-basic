import scrapy
from scrapy_movie_099.items import ScrapyMovie099Item

class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["www.dydytt.net"]
    start_urls = ["https://www.dydytt.net/html/gndy/china/index.html"]

    def parse(self, response):
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

        a_list = response.xpath('//div[@class="co_content8"]//td[2]//a[2]')

        for a in a_list:
            name = a.xpath('./text()').extract_first()
            url = 'https://www.dydytt.net' + a.xpath('./@href').extract_first()

            # 访问url
            yield scrapy.Request(url=url, callback=self.parse_image, meta={'name': name})

        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        pass

    def parse_image(self, response):
        print('----------------------------------------------------')

        name = response.meta['name']

        # 这里 print(src) 的值是none, 因为有些标签不能识别, 只能一遍遍试。注意: 如果拿不到数据的情况下,一定要检查 xpath 语法是否正确
        # src = response.xpath('//div[@id="Zoom"]/span/img/@src').extract_first()
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()

        movie = ScrapyMovie099Item(src=src, name=name)
        yield movie

        print('----------------------------------------------------')
        pass


