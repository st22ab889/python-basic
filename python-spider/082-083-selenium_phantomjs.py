'''
二.Phantomjs
    1.什么是Phantomjs?
        (1)是一个无界面的浏览器
        (2)支持贡面元素查找，js的执行等
        (3)由于不进行css和gui渲染，运行效率要比真实的浏览器要快很多
        注意: Phantomjs基本被淘汰了, 因为公司解散了. 推荐使用"Chrome handless"
    2.如何使用Phantomis?
        (1)获取PhantomJs.exe文件路径path
        (2)browser =webdriver.Phantom]s(path)
        (3)browser.get(url)
        扩展:保存屏幕快照:browser.save screenshot('baidu.png')

三.Chrome handless
    Chrome-headless 模式，Google 针对 Chrome 浏览器 59版 新增加的一种模式，可以让你不打开U!界面的情况下使用 Chrome 浏览器，所以运行效果与 Chrome 保持完美一致。
    1.系统要求:
        Chrome
            Unix\Linux系统需要 chrome >= 59
            Windows系统需要chrome>=60
        Python3.6
        Selenium==3.4.*
        ChromeDriver==2.31
    2.配置:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import options
        chrome options =options()
        chrome options.add argument('--headless')
        chrome options.add argument('--disable-gpu')
        path =r'c:\Program Files(x86)\Google\chrome\Applicationchrome.exe'
        chrome options.binary location = path
        browser =webdriver.chrome(chrome options=chrome options)
        browser.get('http://www.baidu.com/')

Phantomjs 和 Chrome handless 都是基于 selenium 使用
'''



# 082_尚硅谷_爬虫_selenium_phantomjs的基本使用

'''
# selenium 的所有方法和属性 Phantomjs 都能用

from selenium import webdriver
import time

path ='phantomjs.exe
browser = webdriver.PhantomJS(path)

url ='https://www.baidu.combrowser.get(url)
browser.get(url)
browser.save_screenshot('baidu.png')

time.sleep(2)

input = browser.find_element_by_id('kw')
input.send_keys('昆凌')
time.sleep(3)
browser.save_screenshot('kunling.png')
'''



# 083_尚硅谷_爬虫_selenium_handless


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# 解决某些情况下Chrome浏览器启动时遇到的安全沙箱问题。安全沙箱是一种安全特性，旨在隔离浏览器进程，防止浏览器中的恶意代码对操作系统造成损害。然而在某些特定的环境或配置下(例如，在Linux容器中运行Chrome)，安全沙箱可能会阻止浏览器启动。
chrome_options.add_argument("--no-sandbox")
# 用于配置 Chrome 浏览器的启动参数。该参数的作用是‌禁用 /dev/shm 的使用‌。/dev/shm 是一个在类 Unix 系统中的特殊目录，用于共享内存。Chrome 浏览器在默认情况下会使用共享内存来加速某些操作，但在某些受限环境中（如 Docker 容器或某些 Linux 发行版），这种使用方式可能会导致问题，如内存不足或权限错误。
chrome_options.add_argument("--disable-dev-shm-usage")
# 用于配置 Chrome 浏览器的启动参数。该参数的作用是‌禁用 GPU 加速‌。GPU 加速通常用于加速网页渲染、视频播放等图形密集型任务。然而，在某些情况下，GPU 加速可能会导致问题，如浏览器崩溃、性能下降或图形显示错误。此时，使用 --disable-gpu 参数可以禁用 GPU 加速，以提高浏览器的稳定性和兼容性。
chrome_options.add_argument("--disable-gpu")
# 将 detach 参数设置为 true后, 只要不向driver发送quit命令, 就可以在任务结束后仍然保持浏览器打开
chrome_options.add_experimental_option('detach', True)
# 如果不需要图形界面，可以使用无头模式
chrome_options.add_argument("--headless")

# 获取 selenium 版本
print(webdriver.__version__)

# 注意: 之前的一些 selenium 版本这里的path是"chrome.exe"文件的路径,本示例的 selenium 的版本是 "4.29.0".
# path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# 指定chromedriver的路径. 如果要定义一个原始字符串(即不进行任何特殊字符转义的字符串)，你可以在字符串前加上前缀 r 或 R.
path = r'./chromdriver/chromedriver.exe'
service = Service(path)
# 创建谷歌浏览器操作对象:
browser = webdriver.Chrome(service=service, options=chrome_options)
# 最大化网页显示
# browser.maximize_window()

url = 'https://www.baidu.com'
browser.get(url)
browser.save_screenshot('./selenium/baidu.png')
browser.quit()

# 封装的 handless
def share_browser(is_max_mize: bool = False):
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option('detach', True)
    chrome_options.add_argument("--headless")

    path = r'./chromdriver/chromedriver.exe'
    service = Service(path)
    browser = webdriver.Chrome(service=service, options=chrome_options)
    if is_max_mize:
        browser.maximize_window()
    return browser

qq_url = "https://www.qq.com"

browser = share_browser()
browser.get(qq_url)
browser.save_screenshot('./selenium/qq.png')



