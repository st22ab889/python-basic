# 函数入门. 如果将函数定义为类的成员,那么函数就称之为方法
def count_machine(data):        # 定义函数和类的首行和末尾一行需要和相邻的代码(注释不算)隔两个空行
    count = 0
    for i in data:
        count += 1
    print(f"data：{data}, 长度为：{count}")
    return None                 # 没有返回值, 默认返回 None， None的类型为 <class 'NoneType'> . 没有返回值这行可以省略


count_machine("")
count_machine(range(10))


# 函数基础定义语法
def say_hello(name):
    return f"hello {name}"


def add(num1, num2):
    """
    函数的说明文档(这里实际上就是多行注释)，这一行可以说明行数的功能，比如"加法运算"
    :param num1:相加的第一个数字
    :param num2:相加的第二个数字
    :return:两数相加的结果
    """
    return num1 + num2


print(f"{say_hello('Lily')}")
print(f"1 + 2 =  {add(1, 2)}")


def check_temperature(temperature):
    if temperature > 30:
        return "the temperature is to high "
    else:
        return None                             # None 在判断中表示 false


result = check_temperature(20)
if not result:                                  # None在条件判断中有三种写法,另外两种是" result is None:"、"if result == None:"
    print("the temperature is normal")

# None 也可以用于生命无初始内容的变量, None是类型'NoneType'的字面量, 用于表示空的、无意义的
name = None

# 函数的嵌套调用就是在一个函数中调用另一个函数

# 函数变量的作用域. 函数内部定义的变量(局部变量)在外部不能访问; 全局变量在函数的内部或外部都可以被调用


# global 关键字, 将函数内部的局部变量声明为全局变量
num = 100


def test_a():
    print(f"test_a, num = {num}")


def test_b():
    global num                           # 将变量声明为 global 变量
    num = 200                            # 只有这个函数被调用, 全局变量num的值才会被修改为200
    print(f"test_b, num = {num}")


test_a()
test_b()
