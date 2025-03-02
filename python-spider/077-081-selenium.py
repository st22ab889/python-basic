'''
一.Selenium
    1.什么是selenium?
        (1)selenium是一个用于web应用程序测试的工具,
        (2)selenium 测试直接运行在浏览器中，就像真正的用户在操作一样。
        (3)支持通过各种driver(firfoxDriver,IternetExplorerpriver,operaDriver，chromeDriver)驱动真实浏览器完成测试。
        (4)selenium也是支持无界面浏览器操作的。
    2.为什么使用selenium?模拟浏览器功能，自动执行网页中的js代码，实现动态加载
    3.如何安装selenium?
        (1)操作谷歌浏览器驱动下载地址(使用驱动去驱动浏览器)
            http://chromedriver.storage.googleapis.com/index.html
        (2)谷歌驱动和谷歌浏览器版本之间的映射表(已过时，不用管)
            http://blog.csdn.net/huilan same/article/details/51896672
        (3)查看谷歌浏览器版本
            谷歌浏览器右上角-->帮助-->关于
        (4)pip install selenium
    4.selenium的使用步骤?
        (1)导入:from selenium import webdriver
        (2)创建谷歌浏览器操作对象:
             path =谷歌浏览器驱动文件路径
             browser =webdriver.chrome(path)
        (3)访问网址
            url =要访问的网址
            browser.get(url)

    4-1:selenium的元素定位?
        元素定位:自动化要做的就是模拟鼠标和键盘来操作来操作这些元素，点击、输入等等。操作这些元素前首先要找到它们，webDriver提供很多定位元素的方法
        方法:
            1.find element by id
                eg:button = browser.find element by id('su')
            2.find elements by name
                eg:name = browser.find element by name('wd')
            3.find elements by_xpath
                eg:xpath1 = browser.find elements by xpath('//input[@id="su"]')
            4.find elements by tag name
                eg:names =browser.find elements by tag name('input')
            5.find elements by css_selector
                eg:my input =browser.find elements by css selector('#kw')[0]
            6.find elements by link text
                eg:browser.find element by link text("新闻”)

    4-2:访问元素信息
        获取元素属性
            .get_attribute('class')
        获取元素文本
            .text
        获取标签名
            .tag_name

    4-3:交互
        点击:click()
        输入:send_keys()
        后退操作:browser.back()
        前进操作:browser.forword()
        模拟Js滚动:
            js='document.documentElement.scrollTop=100000
            browser.execute_script(js)执行js代码获
        取网页代码:page_source
        退出:browser.quit()

Selenium缺点: 有点慢
'''

import urllib.request

# 077_尚硅谷_爬虫_selenium_为什么要学习selenium
'''
京东首页的秒杀模块, 用浏览器访问有数据,用下面的代码模拟浏览器访问没有数据,因为京东检查到了不是真实的浏览器访问,selenium就是解决这个问题的
注意：目前京东首页没有秒杀模块,这里只是说明 selenium 的优势
'''
url = 'https://www.jd.com/'
response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')
# print(content)


# 078_尚硅谷_爬虫_selenium_基本使用

'''
下载浏览器驱动：
    1. 首先看自己的chrome浏览器的版本号: 谷歌浏览器右上角-->帮助-->关于
        eg:  版本 133.0.6943.127（正式版本） （64 位） , 主要看前两位版本号,后面的小版本号可忽略 ，所以这里浏览器版本是"133.0"
    2. 下载驱动.
        下载地址: 可以下载的地方有很多，如果在下面地址没有找到与浏览器匹配的版本，搜索其它下载驱动的地方
            114以及之前谷歌浏览器驱动版本: https://registry.npmmirror.com/binary.html?path=chromedriver/
            126之后谷歌浏览器驱动版本: https://googlechromelabs.github.io/chrome-for-testing/
        注意事项:
            驱动的版本号要 >= 浏览器版本号 , 驱动的版本可以向下兼容浏览器的版本
    3. 安装 Selenium python 包
        pip install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple
    4. 打开浏览器闪退的解决办法：
        https://www.cnblogs.com/brf-test/p/18160830
        https://www.cnblogs.com/yanghj010/p/18544752   #推荐
    5. Selenium 高版本和低版本 的用法有区别, 直接搜索对应版本的用法
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 获取 selenium 版本, 本示例的 selenium 的版本是 "4.29.0"
print(webdriver.__version__)

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_experimental_option('detach', True)
# 自定义request header 的方式
# chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0")
chrome_options.add_argument("--disable-infobars")
# 如果不需要图形界面，可以使用无头模式
# chrome_options.add_argument("--headless")

# 指定chromedriver的路径
path = './chromdriver/chromedriver.exe'
service = Service(path)
# 创建谷歌浏览器操作对象:
browser = webdriver.Chrome(service=service, options=chrome_options)
# 最大化网页显示
browser.maximize_window()

'''
访问京东时, 会发现首页数据显示不全，暂时没找到解决方法. 如果数据显示全，可以解决"代码模拟浏览器时有些数据看不到的问题,比如秒杀，京东首页目前没有秒杀模块,这里只是说明 selenium 的作用"
访问百度、淘宝、天猫等网站正常(目前正常, 不知道后面服务器端是否会和京东一样, 限制 selenium 驱动打开浏览器访问, 从而导致数据不能完全返回)
'''
#url = 'https://www.jd.com'
url = 'https://www.baidu.com'
browser.get(url)
# 返回网页源码
page_source = browser.page_source
# print(page_source)



# 079_尚硅谷_爬虫_selenium_元素定位

# 如果涉及到没有给到页面但是要数据可以使用"Chrome handless"

from selenium.webdriver.common.by import By

# 通过id定位元素(通过标签的name属性的值获取对象)  ==>> 常用
button = browser.find_element(By.ID, 'su')
print(button)
# 通过标签的name属性的值获取对象
input0 = browser.find_element(By.NAME, 'wd')
print(input0)
# 使用xpath表达式获取对象, 使用"find_elements"返回的是个列表   ==>> 常用
button = browser.find_elements(By.XPATH, '//input[@id="su"]')
print(button)
# 通过标签的名字获取对象
inputs = browser.find_elements(By.TAG_NAME, 'input')
print(inputs)
# 使用bs表达式获取对象(使用bs4的语法获取对象)   ==>> 常用
button = browser.find_elements(By.CSS_SELECTOR, '#su')
print(button)
# 根据衔接文件获取对象(也就是a标签这个对象). 比如 <a href="http://video.baidu.com">视频</a>
atag = browser.find_element(By.LINK_TEXT, "视频")
print(atag)


# 080_尚硅谷_爬虫_selenium_元素信息
button = browser.find_element(By.ID, 'su')
# 获取标签的指定属性的值. <input type="submit" value="百度一下" id="su" class="btn self-btn bg s_btn"> , "bg s_btns"是属性值，"btn self-btn"是样式
print(button.get_attribute('class'))

# 获取标签名
print(button.tag_name)

# 获取元素文本 , <a >视频</a> , "视频"就是元素文本
print(atag.text)


# 081_尚硅谷_爬虫_selenium_交互

import time

# 获取文本框的对象
text = browser.find_element(By.ID, 'kw')
# 在文本框中输入"尚硅谷"
text.send_keys('尚硅谷')
# 获取'百度一下'的按钮点击
browser.find_element(By.ID, 'su').click()
# 这里要sleep几秒小面的代码才会生效
time.sleep(1)
# 划到底部,在企业级开发中，距离顶部10万就能滑倒底部
js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)
# 获取下一页的按钮并点击
next = browser.find_element(By.XPATH, '//a[@class="n"]')
next.click()
time.sleep(2)
# 回到上一页
browser.back()
time.sleep(2)
# 再返回
browser.forward()

time.sleep(3)

# 退出
browser.quit()

