'''
一.基本简介
    1.Beautifulsoup简称: bs4
    2.什么是Beatifulsoup? Beautifulsoup，和1xm1一样，是一个htm1的解析器，主要功能也是解析和提取数据3.优缺点?
        缺点:效率没有1xm1的效率高
        优点:接口设计人性化，使用方便

二.安装以及创建
    1.安装
        在'PyCharm -> Settings -> Porject:{项目名} -> python Intergreter'找到python解释器的位置.比如在"D:\JavaDevTools\JetBrains\Python\Python310\python.exe"
        安装 lxml 到“D:\JavaDevTools\JetBrains\Python\Python310\Scripts”.打开终端,进入到此目录,然后运行以下命令.
        pip install bs4 -i https://pypi.tuna.tsinghua.edu.cn/simple
    2.导入
        from bs4 import Beautifulsoup
    3.创建对象
        服务器响应的文件生成对象
        soup = Beautifulsoup(response.read().decode(),'lxml')本地文件生成对象
        soup = Beautifulsoup(open('1.html')，'lxml')
    注意:默认打开文件的编码格式gbk所以需要指定打开编码格式

三.节点定位
    1.根据标签名查找节点
        soup.a   # 注:只能找到第一个 a
            soup.a.name
            soup.a.attrs
    2.函数
        (1) .find(返回一个对象)
                find('a')       只找到第一个a标签
                find('a', title='名字')
                find('a', class='名字')
        (2) .find_all(返回一个列表)
                find_all('a')   查找所有的a
                find_all('a', title='名字')      返回所有的a和span
                find_all('a', class='名字')      只找前两个a
        (3).select(根据选择器得到节点对象)【推荐】
                1.element
                    eg:p
                2..class
                    eg:.firstname
                3.#id
                    eg:#firstname
                4.属性选择器
                    [attribute]
                        eg:li = soup.select('li[class]')
                    [attribute=value]
                        eg:li = soup.select('li[class="hengheng1"]')
                5.层级选择器
                    element element
                        div p
                    element>element
                        div>p
                    element,element
                        div,p
                                eg:soup = soup.select('a,span')

四.节点信息
    1.获取节点内容:适用于标签中嵌套标签的结构
        obj.string
        obj.get_text()  【推荐】
    2.节点的属性
        tag.name    获取标签名
            eg:tag = find('li')
                print(tag.name)
        tag.attrs 将属性值作为一个字典返回
    3.获取节点的属性
        obj.attrs.get('title')      【常用】
        obj.get('title')
        obj['title']

注意: BeautifulSoup 用起来或多或小有些坑, 实际项目中用xPath比较多
'''


from bs4 import BeautifulSoup

# 075_尚硅谷_爬虫_解析_bs4的基本使用

# 解析本地文件, 默认打开的文件的编码格式是gbk,所以打开文件的时候需要指定编码
soup = BeautifulSoup(open('075_BeautifullySoup_usage.html', encoding='utf-8'), 'lxml')

# 根据标签名查找节点, 找到的是第一个符合提奥健的数据
print(soup.a)

# 获取标签的属性和属性值
print(soup.a.attrs)

# bs4的一些函数
# 返回的是第一个符合条件的数据
print(soup.find('a'))

# 根据title的值找到对应的标签对象
print(soup.find('a', title='a2'))

# 根据class的值找到对应的标签对象, class 是python的关键字，解决方法: 在class后面加上下划线
print(soup.find('a', class_='s1'))

# 以列表的形式返回所有的a标签
print(soup.find_all('a'))

# 以列表的形式返回所有的a标签和span标签, 注意参数传的是列表
print(soup.find_all(['a', 'span']))

# limit=2 表示查找前2个
print(soup.find_all('li', limit=2))

# 推荐使用 select， 但是一般会结合 find 和 find_all 使用
# select 返回的是一个列表，并且会返回多个数据, 直接写a表示获取所有的a标签
print(soup.select('a'))

# 可以通过 . 代表class, 这种操作叫做类选择器
print(soup.select('.s1'))

# 根据id查找对象
print(soup.select('#i1'))

# 根据属性查找对象
# 获取li标签有id属性的对象
print(soup.select('li[id]'))

# 取li标签有id属性的值为i2的对象, 属性值可以加引号也可以不加
print(soup.select('li[id=i2]'))
print(soup.select('li[id="i2"]'))

# 层级(层次)选择器(谁在谁的下边,谁是谁的子代, 谁和谁同级)
# 后代选择器. eg:找到div下面的li, 空格表示后代
print(soup.select('div li'))

# 子代选择器(某标签的第一级子标签). eg:找到div下面的ul的li, ">"表示后代. 'div > ul > li' 也可以写为 'div>ul>li'.在很多的计算机编程语言中,如果不加空格不会输出内容,但是在bs4中不会报错,并且会显示内容
print(soup.select('div > ul > li'))
print(soup.select('div>ul>li'))

# 找到组合标签. eg. 找到所有的a标签和li标签
print(soup.select('a,li'))


# 节点信息
# 获取节点内容
obj = soup.select('#div1')[0]
# 下面的代码配合 html 文件的 "<!-- 测试1 -->" 使用
# print(obj.string)       # 能获取到值
# print(obj.get_text())   # 能获取到值

# 下面的代码配合 html 文件的 "<!-- 测试2 -->" 使用
print(obj.string)       # 不能获取到值
print(obj.get_text())   # 能获取到值
'''
造成上述情况的原因是: 如果标签对象中只有内容, 那么 string 和 get_text() 都可以使用
如果标签对象中除了内容还有标签, string 就获取不到数据, 而 get_text() 可以获取数据
我们一般情况下, 推荐使用 get_text()
'''

# 节点的属性
# 获取标签名
obj = soup.select('#p1')[0]
print(obj.name)
# 将属性值作为一个字典返回
print(obj.attrs)
# 获取节点的属性值，也就是获取字典里面key对应的值. 有以下三种方法:
print(obj.attrs.get('class'))   # 推荐使用
print(obj.get('class'))         # 使用get也可以获取属性的值,但是不推荐,推荐使用"obj.attrs.get('xxx')"
print(obj['class'])             # 也可以使用这种方式获取属性的值



# 076_尚硅谷_爬虫_解析_bs4爬取星巴克数据

import urllib.request
url = 'https://www.starbucks.com.cn/menu/'
response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')

soup = BeautifulSoup(content, 'lxml')
# //ul[@class=".grid padded-3 product strong"]//strong/text()   # 使用 xpath插件 可以找到数据

# 这种方式找不到元素的原因是空格在选择器中,属于后代选择器,而3个类并不存在层级关系. 在html中".grid"后面的"padded-3 product strong"代表3个样式, 所以这是css语法的原因
# name_list = soup.select('.grid padded-3 product strong')

name_list = soup.select('ul[class="grid padded-3 product"] strong')
for name in name_list:
    print(name.get_text())  # print(name.string)


