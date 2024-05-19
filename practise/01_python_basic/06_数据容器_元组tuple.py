"""
tuple 也称为"元组", 元组特点如下:
元组的任意元素可以是任意类型
元组一旦定义完成，就不可修改(强制修改会报错)，相当于 only read list
如果元组嵌套了一个list,那么这个list里面的元素是可以修改的
"""

# 元组的定义格式，使用小括号定义
("abc", 123, 1.0001)                   # 字面量

my_tuple = ("abc", 123, 1.0001)        # 使用变量定义list
print(f"my_tuple = {my_tuple}, type = {type(my_tuple)}")
print(f"my_tuple[1] = {my_tuple[1]}")                             # 正向向索引
print(f"my_tuple[-1] = {my_tuple[-1]}")                           # 反向索引. 倒数第一个元素的下标为 -1, 倒数第二个元素的下标为 -2, 以此类推 ...

tuple_1 = ()                          # 定义空元组
tuple_2 = tuple()                     # 定义空元组

tuple_3 = (111, )                     # 如果元组里面只有一个元素, 元素后面必须要跟一个","号, 否侧就不是元组类型


# 元组的嵌套
tuple_4 = (my_tuple, tuple_3)


# 元组的操作
print(f"tuple_4[1][-1] = {tuple_4[1][-1]}")                         # 通过下标取元组元素,语法和list一样

print(f"1.0001在元组my_tuple中的下标为:{my_tuple.index(1.0001)}")     # 查找某一元素的下标

print(f"1.0001在元组my_tuple中有多少个:{my_tuple.count(123)}")        # 统计某一元素在元组中有多少个

print(f"my_tuple 共有 {len(my_tuple)} 个元素")                       # len函数统计元组元素数量


# while 循环
index = 0
while index < len(my_tuple):
    print(f"my_tuple[{index}] = {my_tuple[index]}")
    index += 1

for item in my_tuple:
    print(f"my_tuple的元素有: {item}")




