"""
读取文件转换成RDD，并完成：
    打印输出：
    打印输出：热门搜索词Top3
    打印输出：统计黑马程序员关键字在哪个时段被搜索最多
    将数据转换为JSON格式，写出为文件
"""


import os
from pyspark import SparkConf, SparkContext

os.environ['JAVA_HOME'] = 'D:\JavaDevTools\JDK 1.8.0_172\jdk1.8.0_172'
os.environ['PYSPARK_PYTHON'] = 'D:\JavaDevTools\JetBrains\Python\python310\python.exe'
os.environ['HADOOP_HOME'] = 'D:\JavaDevTools\JetBrains\hadoop-3.0.0'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
conf.set("spark.default.parallelism", "1")
sc = SparkContext(conf=conf)

# 读取文件转换成RDD
field_rdd = sc.textFile("./search_log.txt")


# 需求1： 热门搜索时间段（小时精度）Top3
# 取出全部时间并转换为小时 -> 转换为(小时,1)的二元元组 -> Key分组聚合为Value -> 排序(降序) -> 取前3
result_1 = field_rdd.map(lambda x: x.split("\t")).\
    map(lambda x: x[0][:2]).\
    map(lambda x: (x, 1)).\
    reduceByKey(lambda a, b: a + b).\
    sortBy(lambda x: x[1], ascending=False, numPartitions=1).\
    take(3)

print(f"需求1的结果{result_1}")


# 需求2：热门搜索词Top3
# 取出全部搜索词 -> 二元元组(词, 1) -> 分布聚合 -> 排序
result_2 = field_rdd.map(lambda x: (x.split("\t")[2], 1)).\
    reduceByKey(lambda a, b: a + b).\
    sortBy(lambda x: x[1], ascending=False, numPartitions=1).\
    take(3)

print(f"需求2的结果{result_2}")


# 需求3：统计"数据仓库"关键字在哪个时段被搜索最多
# 过滤内容 -> 转换为(小时, 1)的二元元组 -> Key分组聚合Value -> 排序(降序) -> 取前1
result_3 = field_rdd.map(lambda x: x.split("\t")).\
    filter(lambda x: x[2] == '数据仓库').\
    map(lambda x: (x[0][:2], 1)).\
    reduceByKey(lambda a, b: a + b).\
    sortBy(lambda x: x[1], ascending=False, numPartitions=1).\
    take(1)

print(f"需求3的结果{result_3}")      # 结果为 [('01', 245)] , 说明在 01 点的时候搜索次数最多, 搜索了245次


# 需求4：将数据转换为JSON格式，写出为文件
"""
想把数据变成JSON, 最好的方式先转换为字典, 再把字典转换为JSON字符串. 如果在转换的过程中, 数据没有Key, 那就构造一个Key
对于Spark来说, 只要把数据变为字典, 写到文件中就是JSON格式. 
"""
# 转换为 JSON 格式的 RDD -> 写出为文件
rdd_json = field_rdd.map(lambda x: x.split("\t")).\
    map(lambda x: {"time": x[0], "user_id": x[1], "key_word": x[2], "rank1": x[3], "rank2": x[4], "url": x[5]})
print(rdd_json.collect())
# rdd_json.saveAsTextFile("./data_json_output")



