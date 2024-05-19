
# windows安装python要科学上网,因为要下载依赖包

print("hello python")


'''
PS D:\python-workspace\practise\01-认识python> python -V
Python 3.11.2
PS D:\python-workspace\practise\01-认识python> python .\01-HelloPython.py
hello python
'''


"""
Ipython 和 python 的区别:
IPython是一个python交互shell，它比默认的python shell更易于使用。它支持自动变量完成、自动缩进、bash shell命令，并且内置了许多有用的函数和函数。
IPython是基于BSD的开源软件。

python pip 是什么？
pip 是一个现代的，通用的 Python 包管理工具。提供了对Python 包的查找、下载、安装、卸载的功能。

windows安装python后没有python3这个命令，解决方法是复制"python.exe",然后重命名为"python3.exe"，保持"python3.exe"和"python.exe"在同一目录下
"""


"""
PowerShell中查看环境变量
$env:path

CMD中查看环境变量
set
""" 