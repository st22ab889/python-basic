
# python 数据容器中的元素可以是任意类型的数据，比如 字符串、数字、布尔 等
# 数据容器包括: 列表(list)、元组(tuple)、字符串(str)、集合(set)、字典(dict)

# list 特点如下：
# 可以容纳多个元素(上线为 2**63 - 1), 且可以增删改查
# 可以容纳不同类型的元素
# 数据是有序存储, 且允许重复数据存在


# list 的定义格式
["abc", 123, 1.0001]                # 字面量

my_list = ["abc", 123, 1.0001]      # 使用变量定义list
print(f"my_list = {my_list}, type = {type(my_list)}")
print(f"my_list[1] = {my_list[1]}")                             # 正向向索引
print(f"my_list[-1] = {my_list[-1]}")                           # 反向索引. 倒数第一个元素的下标为 -1, 倒数第二个元素的下标为 -2, 以此类推 ...

list_1 = []                         # 定义空列表
list_2 = list()                     # 定义空列表

#  list 的嵌套
my_list_2 = [["abc", 123, 1.0001], ["abc", 123]]                    # 定义嵌套列表
print(f"my_list_2 = {my_list_2}, type = {type(my_list_2)}")
print(f"my_list_2[-1][1] = {my_list_2[-1][1]}")

# list 的常用操作
print(f"123在列表中的下标为 {my_list.index(123)}")    # 查找指定元素在列表的下标, 如果找不到, 会报 ValueError

my_list[1] = "python"               # 修改特定位置(索引)的元素值
print(f"my_list[1] = {my_list[1]}")

my_list.insert(1, "牌神")            # 插入元素, 在指定的index位置插入一个元素
print(f"my_list={my_list}, my_list[1] = {my_list[1]}")

my_list.append(None)                # 追加元素,将元素添加都列表的尾部
print(f"my_list={my_list}")


my_list.extend(my_list_2)           # 在列表尾部追加一批元素, 语法 .extend(其它数据容器)
my_list.extend(["aa", "bb", "cc"])
print(f"my_list={my_list}")

del my_list[0]                      # 删除元素方法1, 语法: del 列表[下标]
print(f"my_list={my_list}")

item = my_list.pop(0)               # 删除元素方法2,这种方式可以获取要删除元素  语法: 列表.pop(2)
print(f"删除的元素是 {item}, my_list={my_list}")

my_list.remove(1.0001)              # 删除某元素在列表中的第一个匹配项(从左到右匹配)
print(f"my_list={my_list}")

item_count = my_list.count(None)    # 统计列表内某元素的数量
print(f"元素为None的数量为 {item_count}")

list_count = len(my_list)            # 统计列表中全部的的元素数量
print(f"列表共有 {list_count} 个元素")

my_list.clear()                      # 清空列表所有元素
print(f"my_list={my_list}")


# list 循环
my_list_3 = ["python", 666, 666.666, ["abc", 123]]
index = 0
while index < len(my_list_3):
    element = my_list_3[index]
    print(f"while循环 >>>>> item: {element} ")
    index += 1

for element in my_list_3:
    print(f"for 循环 >>>>> item: {element} ")
