import scrapy


class WubatcSpider(scrapy.Spider):
    name = "wubatc"
    allowed_domains = ["gz.58.com"]
    start_urls = ["https://gz.58.com"]

    def parse(self, response):
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # 获取的是响应的是字符串
        # content = response.text
        # 获取的是二进制数据
        # content = response.body
        # print(content)

        # 使用xpath获取元素
        span = response.xpath('//div[@class="colWrap"]//div[@class="board"]/a')[0]
        # print(span)                 # <a href="/shangpucz/" tongji_tag="pc_home_fc_spcz">商铺出租</a>
        print(span.extract())         # <a href="/shangpucz/" tongji_tag="pc_home_fc_spcz">商铺出租</a>
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        pass
