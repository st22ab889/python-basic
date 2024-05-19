"""
Spark是Apache Spark是用于大规模数据（large-scala data）处理的统一（unified）分析引擎。
    简单来说，Spark是一款分布式的计算框架，用于调度成百上千的服务器集群，计算TB、PB乃至EB级别的海量数据

Spark作为全球顶级的分布式计算框架，支持众多的编程语言进行开发。而Python语言，则是Spark重点支持的方向。

Spark对Python语言的支持，重点体现在，Python第三方库：PySpark之上。
    PySpark是由Spark官方开发的Python语言第三方库。
    Python开发者可以使用pip程序快速的安装PySpark并像其它三方库那样直接使用。

PySpark的两种用法:简单说用PySpark库写出来的代码可以在本地电脑上运行去做数据分析处理, 又可以把代码无缝迁移到成百上千的服务器集群上去做分布式计算
    作为Python库进行数据处理
    提交至Spark集群进行分布式集群计算

Why PySpark
    Python应用场景和就业方向是十分丰富的，其中，最为亮点的方向为：大数据开发 和 人工智能
    本节中，不会涉及到分布式等大数据相关理论，仅使用PySpark作为普通的Python第三方库进行使用。会Python，就能学会。
    Hadoop是大数据技术的基础入门技术栈
"""


"""
# PySpark 库的安装
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyspark

# 构建PySpark执行环境入口对象。想要使用PySpark库完成数据处理，首先需要构建一个执行环境入口对象。PySpark的执行环境入口对象是：类 SparkContext 的类对象
"""

import os
from pyspark import SparkConf, SparkContext

os.environ['JAVA_HOME'] = 'D:\JavaDevTools\JDK 1.8.0_172\jdk1.8.0_172'

# "local[*]" 表示设置spark的运行模式, 这里表示单机模式运行, 如果是集群模式这几就需要设置为'spark://ip:port'. setAppName 用来设置spark应用的名称
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 基础 SparkConf 类对象闯将 SparkContext 对象
sc = SparkContext(conf=conf)

print(sc.version)

sc.stop()


"""
PySpark的编程模型
    SparkContext类对象，是PySpark编程中一切功能的入口。
    PySpark的编程，主要分为如下三大步骤：
        数据输入:通过SparkContext类对象的成员方法完成数据的读取操作,读取后得到RDD类对象
        数据处理计算:通过RDD类对象的成员方法(求和、求最大最小值、分组统计等，这些方法叫RDD的算子)完成各种数据计算的需求
        数据输出:将处理完成后的RDD对象,调用各种成员方法完成写出文件、转换为list等操作

PySpark的编程模型（左图）可以归纳为：
    准备数据到RDD -> RDD迭代计算 -> RDD导出为list、文本文件等.即：源数据 -> RDD -> 结果数据
"""