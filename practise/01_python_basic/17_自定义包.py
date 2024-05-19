"""
python的模块太多就会造成一定的混乱, 这时候就需要通过python包的功能来管理！包的本质依然是模块！一个包，就是一堆同类型功能的集合体!

从物理上看,python包就是一个文件夹,这个文件夹里面包含:
    一堆的python模块
    一个额外的"__init__.py"的文件

导入包:
    方式1:
        import 包名.模块名
        包名.模块名.目标
    方式2:
        from 包 import 模块名
        模块名.目标
    方式3:导入具体的功能
        from 包名.模块名 import 目标
        目标
"""
import my_package.my_module_1

"""
# 方式1
import my_package.my_module_1
my_package.my_module_1.info_print_1()

"""

"""
# 方式2
from my_package import my_module_1
my_module_1.info_print_1()
"""

"""
# 方式3:导入具体的功能
from my_package.my_module_1 import info_print_1
info_print_1()
"""

# 通过 "__all__"变量控制 import *
from my_package import *
# 这里提示"Unresolved reference 'my_module_1'", 因为 my_package 包中的"__init__.py"文件中定义了"__all__ = ['my_module_2']"
my_module_1.info_print_1()



"""
在Python程序的生态中，有许多非常多的第三方包（非Python官方），可以极大的提高开发效率，如：
    科学计算中常用的：numpy包
    数据分析中常用的：pandas包
    大数据计算中常用的：pyspark、apache-flink包
    图形可视化常用的：matplotlib、pyecharts
    人工智能常用的：tensorflow
    等, 这些第三方的包，极大的丰富了Python的生态，提高了开发效率。但是由于是第三方，所以Python没有内置，所以我们需要安装它们才可以导入使用哦。

使用pip安装第三方包, pip是Python内置的程序,安装方法:
    打开令提示符程序
    pip install 包名称
    
python pip安装的包放在哪里:
    使用 pip list 查看已安装的包名
    然后用 pip show 包名，就可以看到安装到哪了    

pip的网络优化, 由于pip是连接的国外的网站进行包的下载，所以有的时候会速度很慢。可以通过如下命令，让其连接国内的网站进行包的安装
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称


PyCharm也提供了安装第三方包的功能：
    右下角点击"python x.xx" --> interpreter --> 左边栏默认 --> 点击"+" --> 就可以搜索包
        --> 搜索到包后可以直接下载
        --> 在右边下面的Options栏,可以设置代理. 比如添加 -i https://pypi.tuna.tsinghua.edu.cn/simple --> 然后再下载
"""