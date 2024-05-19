"""
RDD对象(RDD全称为弹性分布式数据集（Resilient Distributed Datasets）):
    PySpark支持多种数据的输入，在输入完成后，都会得到一个：RDD类的对象
    PySpark针对数据的处理，都是以RDD对象作为载体，即：数据存储在RDD内
        各类数据的计算方法，也都是RDD的成员方法
        RDD的数据计算方法，返回值依旧是RDD对象

Python数据容器转RDD对象：
    list、tuple、set、dict、str转化为PySpark的RDD对象.
    读取文件转RDD对象

注意：
    字符串会被拆分出1个个的字符，存入RDD对象
    字典仅有key会被存入RDD对象
"""

import os
from pyspark import SparkConf, SparkContext

os.environ['JAVA_HOME'] = 'D:\JavaDevTools\JDK 1.8.0_172\jdk1.8.0_172'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)

# 通过 parallelize 方法将Python对象加载到Spark内, 成为RDD对象
rdd_1 = sc.parallelize([1, 2, 3, 4, 5])
rdd_2 = sc.parallelize((1, 2, 3, 4, 5))
rdd_3 = sc.parallelize("abcde")
rdd_4 = sc.parallelize({1, 2, 3, 4, 5})
rdd_5 = sc.parallelize({"key1": "value1", "key2": "value2"})

# 如果要查看RDD里面有什么内容,需要用 collect() 方法
print(rdd_1.collect())
print(rdd_2.collect())
print(rdd_3.collect())  # 字符串会被拆分出1个个的字符，存入RDD对象
print(rdd_4.collect())
print(rdd_5.collect())  # 字典仅有key会被存入RDD对象

# 用 testFile 方法, 读取文件数据加载到Spark内, 成为RDD的对象
rdd_6 = sc.textFile("./main.py")
print(rdd_6.collect())

sc.stop()

