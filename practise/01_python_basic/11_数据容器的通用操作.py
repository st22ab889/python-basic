"""
数据容器的总结对比:
    是否支持下标索引
        支持：列表、元组、字符串，这三类属于序列类型
        不支持：集合、字典，这两类属于非序列类型
    是否支持重复元素：
        支持：列表、元组、字符串，这三类属于序列类型
        不支持：集合、字典，这两类属于非序列类型
    是否可以修改：
        支持：列表、集合、字典
        不支持：元组、字符串

数据容器的应用场景总结：
    列表：一批数据，可修改、可重复的存储场景
    元组：一批数据，不可修改、可重复的存储场景
    字符串：一串字符串的存储场景
    集合：一批数据，去重存储场景
    字典：一批数据，可用Key检索Value的存储场景

数据容器的通用操作：
    通用1：
        列表、集合、字典、元组、字符串都支持for循环遍历
        列表、元组、字符串支持while循环，集合、字典不支持（无法下标索引）
    通用2：可以通用非常多的功能方法
       统计容器的元素个数: len(容器)
       统计容器的最大元素: max(容器)
       统计容器的最小元素: min(容器)
    通用3：容器的通用转换功能
        将给定容器转换为列表: list(容器)
        将给定容器转换为元组: tuple(容器)
        将给定容器转换为字符串: str(容器)
        将给定容器转换为集合: set(容器)
        注意: 转字典的函数为 dict(容器) , 但是字典要求键值对, 所以列表、元组、字符串、集合不能转换为字典,强制转换会出错
   通用4：容器通用排序功能
        将给定容器进行排序，语法：
            sorted(容器, [reverse=True])
        注意，排序后都会得到列表（list）对象
"""

my_list = [3, 2, 1, 5, 4]
my_tuple = (2, 4, 5, 1, 3)
my_str = "python"
print(max(my_list))         # 结果为 3
print(min(my_tuple))        # 结果为 1
print(max(my_str))          # 结果为 y

my_set = {1, 5, 3, 4, 2}
my_dict = {"name": "Tom", "age": 10}

# 容器转列表
print(f"列表转列表的结果是: {list(my_list)}")
print(f"元组转列表的结果是: {list(my_tuple)}")
print(f"字符串转列表的结果是: {list(my_str)}")
print(f"集合转列表的结果是: {list(my_set)}")
print(f"字典转列表的结果是: {list(my_dict)}")             # 字典转列表, 得到的list里面的元素是字典里面的key, value 会丢失


# 容器转元组
print(f"列表转元组的结果是: {tuple(my_list)}")
print(f"元组转元组的结果是: {tuple(my_tuple)}")
print(f"字符串转元组的结果是: {tuple(my_str)}")
print(f"集合转元组的结果是: {tuple(my_set)}")
print(f"字典转元组的结果是: {tuple(my_dict)}")             # 字典转列表, 得到的元组里面的元素是字典里面的key, value 会丢失

# 容器转字符串, 容器转字符串结果看起来没有变化, 实际上结果已经是字符串, 只不过双引号没有打印出来，比如 [1, 2, 3] 实际上是 "[1, 2, 3]", {'abc', 1.0001, 123} 实际上是 "{'abc', 1.0001, 123}"
print(f"列表转字符串的结果是: {str(my_list)}")
print(f"元组转字符串的结果是: {str(my_tuple)}")
print(f"字符串转字符串的结果是: {str(my_str)}")
print(f"集合转字符串的结果是: {str(my_set)}")
print(f"字典转字符串的结果是: {str(my_dict)}")             # 字典转字符串, value 不会丢失

# 容器转集合
print(f"列表转集合的结果是: {set(my_list)}")
print(f"元组转集合的结果是: {set(my_tuple)}")
print(f"字符串转集合的结果是: {set(my_str)}")
print(f"集合转集合的结果是: {set(my_set)}")
print(f"字典转集合的结果是: {set(my_dict)}")             # 字典转集合, value 会丢失

# 进行容器的排序, 排序的结果会变为列表对象
print(f"列表对象的排序结果是: {sorted(my_list)}")
print(f"元组对象的排序结果是: {sorted(my_tuple)}")
print(f"字符串对象的排序结果是: {sorted(my_str)}")
print(f"集合对象的排序结果是: {sorted(my_set)}")          #  如果set的元素既有'str'类型, 也有'int'类型, 则不支持排序, 会报错
print(f"字典对象的排序结果是: {sorted(my_dict)}")         # 是对字典的key进行排序, 排序后得到一个列表, 会丢失value

print(f"列表对象的反向排序结果是: {sorted(my_list, reverse=True)}")
print(f"元组对象的反向排序结果是: {sorted(my_tuple, reverse=True)}")
print(f"字符串对象的反向排序结果是: {sorted(my_str, reverse=True)}")
print(f"集合对象的反向排序结果是: {sorted(my_set, reverse=True)}")
print(f"字典对象的反向排序结果是: {sorted(my_dict, reverse=True)}")         # 是对字典的key进行排序, 排序后得到一个列表, 会丢失value
