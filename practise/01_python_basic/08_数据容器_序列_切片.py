"""
序列是指: 内容连续、有序,可使用下标索引的一类数据容器
列表、元组、字符串均可以视为序列！ 序列均支持切片, 即列表、元组、字符串均支持切片操作
    列表、元组切片后的数据类型均为 list
    字符串切片后的数据类型为 str

切片: 从一个序列中，取出一个子序列
语法:
    序列[起始下标:结束下标:步长]
注意事项:
    取子序列时包含起始下标对应的元素,不包含结束下标对应的元素
    起始下标如果留空,表示从头开始
    结束下标如果留空,表示截取到结尾
    步长：
        为1, 表示依次取每个元素
        为2, 表示每次跳过1个元素取
        为N, 表示跳过 N-1 个元素取
        为负数, 反向取(注意, 起始下标和结束下标也要反向标记)
    切片不会影响序列本身, 而是得到一个新的序列
"""

# 对list进行切片.
my_list = ["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "jj", "kk", "ll", "mm", "nn"]
new_list = my_list[1:6]         # 从1开始, 6结束, 步长为1. 当步长为1可以省略不写
print(f"list切片后的数据为：{new_list}, 类型是：{type(new_list)}")

new_list2 = my_list[3:1:-1]     # 从3开始到1结束,步长为-1
print(f"list切片后的数据为：{new_list2}, 类型是：{type(new_list2)}")


# 对tuple进行切片.
my_tuple = ["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "jj", "kk", "ll", "mm", "nn"]
new_tuple = my_tuple[:]         # 从1开始一直到最后, 步长为1
print(f"元组切片后的数据为：{new_tuple}, 类型是：{type(new_tuple)}")

new_tuple2 = my_tuple[::-2]     # 从头开始到尾结束,步长为-2
print(f"元组切片后的数据为：{new_tuple2}, 类型是：{type(new_tuple2)}")


# 对str进行切片,
my_str = "string is container which is only included char"
new_str = my_str[::2]               # 从头开始到最后结束,步长为2
print(f"字符串切片后的数据为：{new_str}, 类型是：{type(new_str)}")

new_str2 = my_str[::-1]             # 从头开始, 到最后结果, 步长为-1, 这种写法相当于将序列反转
print(f"字符串切片后的数据为：{new_str2}, 类型是：{type(new_str2)}")


