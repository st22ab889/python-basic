# bool类型字面量
True
False

# 使用变量定义
bool_1 = True
bool_2 = False
print(f"bool_1值为：{bool_1}, 类型为:{type(bool_1)}; bool_2值为：{bool_2}, 类型为:{type(bool_2)}")

# 比较运算符: ==、 !=、 >、 <、 >=、 <=
num_1 = 10
num_2 = 15
print(f"num_1 == num_2 的结果为: {num_1 == num_2}")
print(f"num_1 =< num_2 的结果为: {num_1 <= num_2}")


# if 、if else、if elif else;  逻辑运算符 and、or、not ，基本格式: a and b、 a or b、 not a
age = 16
if age >= 18:
    print("成年人")
elif 12 <= age < 18:    # 12 <= age  and  age < 18
    print("青少年")
else:
    print("还是小孩")


# while 循环
count = 0
while count < 3:
    print(f"count = {count}")
    count += 1


# for  in , 无法定义循环条件， for 循环语句本质上是遍历"序列类型"，这些"序列类型"包括字符串、列表、数组等
name = "牌神"
for x in name:                  # x是for循环的临时变量,在for循环外部可以访问到这个临时变量,但是在规范上不允许这样做. 如需访问临时变量,可以预先在循环外定义它
    print(f"---{x}---")         # 空格缩进在python中异常重要


# range 语句, 获取简单的数字序列
range_value = range(2)
print({f"range的值是: {range_value},range的类型是: {type(range_value)}"})
for x in range(3):                      # range(3) 获取的数据是[0,1,2]
    print(f"a---{x}---")
for x in range(3, 6):                   # range(3, 6) 获取的数据是[3,4,5]
    if x == 4:
        continue
    print(f"b---{x}---")
for x in range(3, 9, 2):                # range(3, 10, 2) 获取的数据是[3,5,7], 语法为: range(num1, num2, step), step的默认值为1
    if x == 5:
        break
    print(f"c---{x}---")

