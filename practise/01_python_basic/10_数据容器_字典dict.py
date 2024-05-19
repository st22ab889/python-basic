"""
字典(映射)，使用 {} 定义， 里面存储的元素是键值对, 如下语法:
    {key: value, ......,key: value}

字典中的key不能重复, 如果重复定义, 后面的会覆盖前面的
字典不可以使用下标索引(所以也不能用while循环), 可以通过key取得value
字典的key和value可以是任意数据类型, 但是key不能是字典

字典总结：
    可以容纳多个不同类型的数据,每一份数据是 KeyValue 键值对
    不支持下标索引, 所以不支持while循环,但是支持for循环
    可以增删改查
"""

# 字典的定义
{"name": "Tom", "age": 10}                  # 定义字典字面量
my_dict = {"name": "Tom", "age": 10}        # 定义字典变量
print(f"my_dict字典的内容为 {my_dict}, 类型为 {type(my_dict)}")

none_dict = {}                                # 定义空字典
none_dict = dict()                            # 定义空字典

name = my_dict["name"]                        # 基于key获取value
print(f"name为 {name}")


stu_score_dict = {                            # 定义嵌套字典
    "Tom": {
        "语文": 60,
        "数学": 61,
        "英语": 62
    }, "Jay": {
        "语文": 67,
        "数学": 68,
        "英语": 69
    }
}
print(f"考试信息是 {stu_score_dict}")

stu_math_score = stu_score_dict["Jay"]["数学"]    # 从嵌套字典中获取数据
print(f"Jay的数学成绩是 {stu_math_score}")


"""
字典的常用操作
    新增元素
        语法如下,如果key不存在就相当于增加操作
            字典[key]=value  
    更新元素
        语法如下,如果key存在就相当于更新操作
            字典[key]=value
    删除元素
        语法如下:
            字典.pop(key)
        结果: 获得指定的key的value, 同时字典里面的key和value被删除
    获取全部的key
        语法如下:
            字典.keys()
    清空字典
        语法如下:
            字典的.clear()
            
"""

my_dict["gender"] = "male"                  # my_dict 中没有 gender 这个key， 所以会新增
my_dict["age"] = 11                         # my_dict 有 age 这个key， 所以会修改
print(f"my_dict中的元素为 {my_dict}")

value = my_dict.pop("gender")               # 删除元素
print(f"gender的value是 {value}")

keys = my_dict.keys();                      # 获取字全部的key
print(f"my_dict的全部key为 {keys}, 类型为 {type(keys)}")

# 遍历字典方式1
for key in keys:
    print(f"key为{key},value为{my_dict[key]}")

# 遍历字典方式2,直接遍历字典, 实际便遍历的也是key, 然后通过key获取value
for key in my_dict:
    print(f"key为{key},value为{my_dict[key]}")

count = len(my_dict)                        # 统计字典的元素数量
print(f"my_dict中的元素有 {count} 个")

value = my_dict.clear()                     # 清空字典
print(f"my_dict中的元素为 {my_dict}")



