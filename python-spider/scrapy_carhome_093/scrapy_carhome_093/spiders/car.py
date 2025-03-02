import scrapy


class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["www.autohome.com.cn"]
    start_urls = ["https://www.autohome.com.cn/price/brandid_15"]

    def parse(self, response):
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        name_list = response.xpath('//div[@class="tw-mb-2 tw-flex tw-flex-nowrap tw-items-center"]/a/text()')
        price_list = response.xpath('//div[@class="tw-mb-2.5 tw-flex tw-items-center tw-whitespace-nowrap tw-text-sm tw-text-[#828CA0]"]/a/text()')
        for i in range(len(name_list)):
            name = name_list[i]
            price = price_list[i]
            print(name, price)
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        pass
