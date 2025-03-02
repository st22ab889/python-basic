import scrapy
import json

class TestpostSpider(scrapy.Spider):
    name = "testpost"
    allowed_domains = ["fanyi.baidu.com"]

    # post 请求如果没有参数,那么这个请求将没有任何意义. 所以 start_urls 没有用, 进而 parse 方法页没有用
    # start_urls = ["https://fanyi.baidu.com/sug"]
    #
    # def parse(self, response):
    #     pass

    # post 请求要使用 start_requests, 这是 scrapy 框架提供的
    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'

        data = {
            'kw': '编程语言'
        }

        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)

    def parse_second(self, response):
        content = response.text
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        obj = json.loads(content)
        print(obj)
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')