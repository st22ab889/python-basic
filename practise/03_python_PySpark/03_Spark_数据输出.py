"""
RDD数据输出:
    输出为Python对象：
        collect方法：将RDD各个分区的数据,统一收集到Driver中,形成一个List对象
        reduce方法：对RDD数据集按照传入的逻辑进行聚合
        take算子：取RDD的前N个元素,组成list返回
        count算子：计算RDD有多少条数据,返回一个数字
    输出到文件中：
        saveAsTextFile方法：
            将RDD数据写入文本文件中。支持本地写出、hdfs等文件系统. 调用保存文件的方法(算子)，需要配置Hadoop依赖
            输出的结果是个文件夹
            有几个分区就输出多少个结果文件

"saveAsTextFile"依赖 hadoop 框架, hadoop框架配置如下：
    下载Hadoop安装包,解压到电脑任意位置   http://archive.apache.org/dist/hadoop/common/hadoop-3.0.0/hadoop-3.0.0.tar.gz
    在Python代码中使用os模块配置：os.environ[‘HADOOP_HOME’] = ‘HADOOP解压文件夹路径’
    下载winutils.exe，并放入Hadoop解压文件夹的bin目录内 https://raw.githubusercontent.com/steveloughran/winutils/master/hadoop-3.0.0/bin/winutils.exe
    下载hadoop.dll，并放入:C:/Windows/System32 文件夹内 https://raw.githubusercontent.com/steveloughran/winutils/master/hadoop-3.0.0/bin/hadoop.dll
"""
import os
from pyspark import SparkConf, SparkContext

os.environ['JAVA_HOME'] = 'D:\JavaDevTools\JDK 1.8.0_172\jdk1.8.0_172'
# 因为 Spark 不能找到 Python 解释器的位置, 所以这里需要在环境变量中指定
os.environ['PYSPARK_PYTHON'] = 'D:\JavaDevTools\JetBrains\Python\python310\python.exe'
os.environ['HADOOP_HOME'] = 'D:\JavaDevTools\JetBrains\hadoop-3.0.0'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)

rdd = sc.parallelize(range(1, 10))     # range(1, 10) 的结果是 [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(rdd.collect())

print("----------------------------------------------------------------------------------")


print(rdd.reduce(lambda a, b: a + b))


print("----------------------------------------------------------------------------------")


print(rdd.take(6))


print("----------------------------------------------------------------------------------")


print(rdd.count())


# 这个方法依赖hadoop框架，
# rdd.saveAsTextFile("./rdd_data/output/")

"""
saveAsTextFile 方法运行后有多个文件？
    这是因为RDD有多个分区，saveAsTextFile这个算子输出文件的个数是根据RDD的分区来决定的，有多少个分区就输出多少个文件，默认的分区数量等于CPU的核心个数！
    简单说，分区就是在RDD中把数据均匀分散到各个分区中存储。如果数据本身很少，那么有些分区中就没有数据，那么对应产生的文件也没有数据

修改RDD分区为1个:
    方式1: 全局设置, SparkConf对象设置属性全局并行度为1：
        conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
        conf.set("spark.default.parallelism", "1")
        sc = SparkContext(conf=conf)
        
    方式2: 针对某个RDD设置， 创建RDD的时候设置(parallelize方法传入numSlices参数为1)
        rdd_1 = sc.parallelize([1, 2, 3, 4, 5], numSlices=1)        # 关键字参数
        rdd_2 = sc.parallelize([1, 2, 3, 4, 5], 1)                  # 因为第二个参数就是 numSlices, 所以也可以使用位置传参
"""

sc.stop()

