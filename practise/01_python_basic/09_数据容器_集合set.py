"""
列表可修改,支持重复元素且有序
元组、字符串不可修改,支持重复元素且有序

集合: 不支持元素的重复(自带去重功能),并且内容无序
集合使用 {} 定义集合

因为集合无序, 所以集合不支持 下标索引访问！所以序列也不包括集合(集合不是序列)！
集合和列表一样, 允许被修改

集合特点总结：
    可以容纳多个不同类型的数据,数据在set中是无序的且不允许元素重复
    可以修改(增加或删除元素等)
    支持for循环,不支持while循环(因为set不支持下标访问)
"""

# 定义格式
{"abc", 123, 1.0001}                                # 字面量

my_set = {"abc", 123, "abc", 1.0001, 123}           # 使用变量定义set
print(f"my_set = {my_set}, type = {type(my_set)}")

set_1 = set()                                       # 定义空集合
print(f"my_set = {set_1}, type = {type(set_1)}")

my_dict = {}                                        # 注意:这种方式定义的不是空集合, 而是定义的空字典, 这是一个空字典类型
print(f"my_dict = {my_dict}, type = {type(my_dict)}")


# 常见操作
my_set.add("python")                                # add new element
my_set.add("python")                                # 虽然添加了两次,但是会被去重
print(f"my_set = {my_set}")

my_set.remove("python")                             # remove element
print(f"my_set = {my_set}")

item = my_set.pop()                                 # 从集合中随机取出元素, 取出后这个元素在集合中就不存在了
print(f"item = {item}, 取出后集合为 {my_set}")

print(f"my_set集合中的数量为 {len(my_set)}")          # 统计集合元素数量

my_set.clear()                                     # 清空集合
print(f"清空后的my_set集合为 {my_set}")


"""
取两个集合的差集
    语法:
        集合1.difference(集合2)
    功能: 取出集合1有而集合2没有的, 得到一个新的集合, 集合1和集合2不变
    
消除2个集合的差集
    语法:
        集合1.difference_update(集合2)
    功能: 对比集合1和集合2, 在集合1内,删除和集合2相同的元素
    结果: 集合1被修改, 集合2不变
    
两个集合合并为1个
    语法:
        集合1.union(集合2)
    结果：得到新集合, 集合1和集合2不变
        
"""
set_1 = {1, 2, 3}
set_2 = {2, 5, 6}
set_3 = set_1.difference(set_2)
print(f"set_3 的集合为 {set_3}")

set_1.difference_update(set_2)
print(f"set_1 的集合为 {set_1}, set_2 的集合为 {set_2}")

set_3 = set_1.union(set_2)
print(f"set_3 的集合为 {set_3}")


# 集合的遍历, 集合不支持下标索引,所以不能用while循环, 但是可以用for循环
for item in set_3:
    print(f"set_3 的集合的元素为 {item}")




