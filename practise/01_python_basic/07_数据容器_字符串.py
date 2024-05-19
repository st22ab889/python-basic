"""
字符串是字符的容器，一个字符串可以存放任意数量的字符.
字符串也有正向索引和反向索引
同元组一样，字符串是一个无法修改的数据容器. 如果必须要做，只能创建一个新的字符串
"""

my_str = "string is container which is only included char"

print(f"index为2的字符为 {my_str[2]}, index为-2的字符为 {my_str[-2]}")


# 常规操作
print(f"is在字符串 {my_str} 的起始下标为 {my_str.index('is')}")     # 查找字符下标(从左到右第一个匹配到的元素的下标)

new_str = my_str.replace("is", "是")                              # 字符串替换，这个方法不是修改字符串本身，而是得到一个新的字符串，所以replace方法会返回一个新的字符串
print(f"替换后得到的新的字符串为 {new_str}")

str_list = my_str.split(" ")                                      # 字符串的分割. 按照指定的分隔符分割字符串. 字符串本身不变,而是得到一个列表对象
print(f"字符串列表为: {str_list}, 类型为 {type(str_list)}")


my_str2 = " string is container which is only included char "
new_str = my_str2.strip()                                     # 字符串的规整操作. 两种用法: strip() 去前后空格,  strip(字符串) 去前后指定字符串
print(f"strip后的字符串为:{new_str}")

my_str3 = "12string is container which is only included char21"
new_str = my_str3.strip("12")                                 # 注意：传入的"12"其实就是"1"、"2"都会移除,按照单个字符. 只要字符串前后包含"1"或"2"都会被移除
print(f"strip后的字符串为:{new_str}")

print(f"{my_str} 中'is'出现的次数是: {my_str.count('is')}")     # 统计字符串中某字符串的出现次数

print(f"{my_str} 的长度是: {len(new_str)}")                    # 统计字符串的长度


# while 循环
my_str = "python"
index = 0
while index < len(my_str):
    print(f"my_str[{index}]={my_str[index]}")
    index += 1

for item in my_str:
    print(f"my_str的元素为：{item}")
