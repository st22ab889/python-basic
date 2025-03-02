# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 如果想使用管道就必须在settings中开启管道
class ScrapyDangdang095Pipeline:

   # 这里的 item 就是"yield book"返回的book对象
    def process_item(self, item, spider):

        # (1) write 方法必须要写一个字符串,而不能是其它的对象
        # (2) w 模式会每次都会打开一个文件, 会覆盖之前的内容
        # (3) 以下保存数据的方法不推荐, 因为每传递过来一个对象, 就会打开一次文件, 对文件的操作过于频繁
        # with open('book.json', 'a', encoding='utf-8') as fp:
        #     fp.write(str(item))

        # 推荐使用(解决了以上问题,整个过程只需打开一次文件和关闭一次文件)
        self.fp.write(str(item))

        return item

    # 在爬虫文件运行之前 运行的方法
    def open_spider(self, spider):
        self.fp = open('book.json', 'w', encoding='utf-8')

    # 在爬虫文件运行之后 运行的方法
    def close_spider(self, spider):
        self.fp.close()

'''
# 在爬虫文件运行之前 运行的方法, 这个方法在项目初始化后没有显示生成出来,需要手动写
def open_spider(self, spider):
    
# 在爬虫文件运行过程中 运行的方法
def process_item(self, item, spider):

# 在爬虫文件运行之后 运行的方法, 这个方法在项目初始化后没有显示生成出来,需要手动写
def close_spider(self, spider):
'''


import urllib.request
'''
多条管道开启
    (1) 定义管道类
    (2) 在setting中开启管道
            "scrapy_dangdang_095.pipelines.DangDangDownloadPipeline": 301
'''
class DangDangDownloadPipeline:
    def process_item(self, item, spider):

        url = 'http:' + item.get('src')
        # 有些特殊字符不能作为文件名, 会导致创建文件失败,所以需要替换
        name = item.get('name').replace("/", "-")
        # 需要提前创建 book_images 这个文件夹
        file_name = './book_images/' + name + '.jpg'
        urllib.request.urlretrieve(url=url, filename=file_name)

        return item


