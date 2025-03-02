'''
xpath: 解析 xml, 能帮助获取网页源码的部分数据:
JsonPath: 解析json
BeautifulSoup：
'''

'''
xpath使用：
    注意：提前安装浏览器xpath插件(用来调试xpath语句)
        (1) chrome右上角找到选项-->更多工具-->扩展程序。打开开发者模式, 然后拖拽crx文件到此页面，即可安装。安装后，打开xpath插件上的开关
        (2) 如果crx无法安装，修改后缀名为 zip 或者 rar 后再次安装
        (3) 关闭浏览器重新打开，按 "ctrl + shift + x" 打开, 出现调试工具窗口说明工具安装成功。再按一次就是关闭。
        (4) 其它：
                解决crx文件扩展程序chrome下载自动删除的问题: https://blog.csdn.net/m0_61315707/article/details/138424658
    1.安装lxml库
        在'PyCharm -> Settings -> Porject:{项目名} -> python Intergreter'找到python解释器的位置.比如在"D:\JavaDevTools\JetBrains\Python\Python310\python.exe"
        安装 lxml 到“D:\JavaDevTools\JetBrains\Python\Python310\Scripts”.打开终端,进入到此目录,然后运行以下命令.
        pip install lxml -i https://pypi.tuna.tsinghua.edu.cn/simple
        注意：
            (1). pip 安装包超时的解决方法: https://blog.csdn.net/mnb1V9cxz/article/details/127561910
            (2).安装后如果"from lxml import etree"语句报错,有两种可能：
                位置安装错误，安装后, 在'PyCharm -> Settings -> Porject:{项目名} -> python Intergreter'右边的列表中可以看到lxml包。
                关掉 PyCharm 再重新打开。
    2.导入lxml.etree
        from lxml import etree
    3.解析本地文件
        html_tree = etree.parse('xx.html')
    4.解析服务器响应文件
        html_tree = etree.HTML(response.read().decode('utf-8'))
    5.
        html_tree.xpath(xpath路径)
'''

'''
xpath基本语法
    1. 路径查询
     //：查找所有子孙节点，不考虑层级关系
     / ：找直接子节点(一层一层找)
    2. 谓词查询
     //div[@id]
     //div[@id="maincontent"]
    3. 属性查询
     //@class
    4. 模糊查询
     //div[contains(@id, "he")]
     //div[starts‐with(@id, "he")]
    5. 内容查询
     //div/h1/text()
    6. 逻辑运算
     //div[@id="head" and @class="s_down"]
     //title | //price
'''

# 069_尚硅谷_爬虫_解析_xpath插件的安装
# 070_尚硅谷_爬虫_解析_xpath的基本使用

from lxml import etree

# 如果报"lxml.etree.XMLSyntaxError: Opening and ending tag mismatch: meta line 4 and head, line 6, column 8"说明某个元素无结束标签，找到这个标签然后加上即可
html_tree = etree.parse('./070_xpath_usage.html')

# 查看 ur 标签下面的 li
li_list = html_tree.xpath('//ul/li')
print(len(li_list))

# [@id] 查看有id属性的li标签
li_list = html_tree.xpath('//ul/li[@id]')
print(len(li_list))

# text() 获取标签中的内容
li_list = html_tree.xpath('//ul/li[@id]/text()')
print(li_list)

# 查找 id 为 i1 的标签
li_list = html_tree.xpath('//ul/li[@id="i1"]/text()')
print(li_list)

# 查找到 id 为 i1 的 li 标签的class的属性值
li_list = html_tree.xpath('//ul/li[@id="i1"]/@class')
print(li_list)

# 查询 id 属性值 中包含 ii 的 li 标签
li_list = html_tree.xpath('//ul/li[contains(@id, "ii")]/text()')
print(li_list)

# 查询 id 属性的值以 i 开头的 li 标签
li_list = html_tree.xpath('//ul/li[starts-with(@id, "i")]/text()')
print(li_list)

# 查询 id 属性的值为 i1 和 class 属性的值为 c1 的标签
li_list = html_tree.xpath('//ul/li[@id="i1" and @class="c1"]/text()')
print(li_list)

# 查询 id 属性的值为 i1 或 class 属性的值为 c2 的标签
li_list = html_tree.xpath('//ul/li[@id="i1"]/text() | //ul/li[@class="c2"]/text()')
print(li_list)


# 071_尚硅谷_爬虫_解析_获取百度网站的百度一下

import urllib.request
# 这里一定要加上协议名称 "http://" 或 "https://"
url = 'https://www.baidu.com'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
context = response.read().decode('utf-8')

# 解析网页源码获取数据
tree = etree.HTML(context)
result = tree.xpath('//input[@id="su"]/@value')
print(result)
print(result[0])


# 072_尚硅谷_爬虫_解析_站长素材
'''
站长素材: https://sc.chinaz.com/
下载站长素材的前十页图片
'''

def get_request(page):
    if(page == 1):
        url = 'https://sc.chinaz.com/tupian/xingganmeinvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/xingganmeinvtupian_' + str(end_page) + '.html'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'
    }

    return urllib.request.Request(url, headers=headers)


def get_images_urls(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content):
    '''
    注意问题 1: 这里获取到的源码, 和浏览器开发者工具那里显示的源码不一样, 所以要根据获取到的源码(也就是网页那里右键"查看网页源代码")写xpath语句
    注意问题 2: 一般涉及图片的网站都会进行懒加载。比如:
        当打开一个页面的时候, 有一些img标签的里面保存地址的属性名称为src2, 当页面划到显示这个图片的时候, js 会动态修改属性名称, 把 src2 修改为 src。
        在写 xpath 语句时, 要写修改前的属性名称。
    '''
    images_urls = etree.HTML(content).xpath('//div[@class="item"]/img/@data-original')
    images_names = etree.HTML(content).xpath('//div[@class="item"]/img/@alt')
    for i in range(len(images_urls)):
        src = "http:" + images_urls[i]
        name = images_names[i]
        urllib.request.urlretrieve(url=src, filename='./072_Image/' + name + '.jpg')

if __name__ == '__main__':
    start_page = int(input("输入起始页: "))
    end_page = int(input("输入起始页: "))
    for page in range(start_page, end_page + 1):
        request = get_request(page)
        content = get_images_urls(request)
        down_load(content)


