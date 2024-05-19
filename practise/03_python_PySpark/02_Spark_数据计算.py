"""
PySpark的数据计算,基于RDD对象内置丰富的成员方法（算子）进行计算:
    map方法: 将RDD的数据一条条处理(处理的逻辑基于map算子中接收的处理函数),返回新的RDD
    flatmap方法：对rdd进行map操作,然后进行解除嵌套操作
    reduceByKey方法：针对KV型RDD,自动按照key分组,然后根据提供给的聚合逻辑,完成组内数据(value)的聚合操作.
            只要RDD存储的数据是二元元组就可以称之为KV型的RDD
            二元元组就是元组里面的数据只有两个，第一个元素称为 key,第二个元素称为 value
            reduceByKey中接收的函数,只负责聚合,不理会分组(分组是自动根据key来分组)
    filter方法：过滤数据
    distinct方法：去重
    sortBy方法：排序, 并且可以指定排序依据

注意：
   这里使用的 pyspark 版本是 3.3.2
        使用 python-3.11.2-amd64.exe, 运行map的方法会报错
        使用 python-3.10.10-amd64.exe, 运行map的方法不会报错
   第三方包支持的 python 版本很重要, 所以一定要清楚第三方包支持的是哪个 python 版本
"""
import os
from pyspark import SparkConf, SparkContext

os.environ['JAVA_HOME'] = 'D:\JavaDevTools\JDK 1.8.0_172\jdk1.8.0_172'
# 因为 Spark 不能找到 Python 解释器的位置, 所以这里需要在环境变量中指定
os.environ['PYSPARK_PYTHON'] = 'D:\JavaDevTools\JetBrains\Python\python310\python.exe'


conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])

# 将列表中的每个元素都乘以10, map 接收有个函数, "(T) -> U" 表示参数和返回值类型可以不一样,  "(T) -> T" 表示参数和返回值类型一样
rdd_2 = rdd.map(lambda x: x * 10)
print(rdd_2.collect())

rdd_3 = rdd_2.map(lambda x: x + 10)       # 也可以直接写成： rdd = rdd.map(lambda x: x * 10).map(lambda x: x + 10)
print(rdd_3.collect())


print("----------------------------------------------------------------------------------")


rdd_4 = sc.parallelize(["python  Django", "Java Golang C++", "Kubernetes Helm"])

# RDD数据里面的单词一个个提取出来
rdd_5 = rdd_4.map(lambda x: x.split(" "))
print(rdd_5.collect())     # 结果为一个嵌套的List： [['python', '', 'Django'], ['Java', 'Golang', 'C++'], ['Kubernetes', 'Helm']]

rdd_6 = rdd_4.flatMap(lambda x: x.split(" "))
print(rdd_6.collect())  # 结果为(flatMap能解除List嵌套): ['python', '', 'Django', 'Java', 'Golang', 'C++', 'Kubernetes', 'Helm']


print("----------------------------------------------------------------------------------")


rdd = sc.parallelize([('male', 10), ('male', 11), ('female', 9), ('female', 10), ('female', 11)])
# 当运行 reduceByKey 方法时会显示"UserWarning: Please install psutil to have better support with spilling", 安装 psutil 后再运行警告就会消除
# pip install psutil
rdd_2 = rdd.reduceByKey(lambda a, b: a + b)
print(rdd_2.collect())     # 结果为:   [('female', 30), ('male', 21)]


print("----------------------------------------------------------------------------------")

rdd = sc.parallelize([1, 2, 3, 4, 5])

# 保留偶数,过滤掉奇数
rdd = rdd.filter(lambda num: num % 2 == 0)
print(rdd.collect())


print("----------------------------------------------------------------------------------")


rdd = sc.parallelize([10, 20, 20, 30, 40, 50, 50])
rdd = rdd.distinct()
print(rdd.collect())          # 去重后数据不会保持原先顺序，结果为： [40, 10, 50, 20, 30]


print("----------------------------------------------------------------------------------")


rdd = sc.parallelize([('kubernetes', 10), ('docker', 18), ('python', 29), ('java', 20), ('linux', 99)])

# ascending为False表示降序; numPartitions表示用多少分区排序，跟分布式有关系，本地运行设为1就可以
rdd = rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)

print(rdd.collect())


sc.stop()
