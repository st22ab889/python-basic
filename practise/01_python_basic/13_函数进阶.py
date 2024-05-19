# 函数的多返回值, 返回值的类型不受限
def test():
    return 11, "python", ["aa", 1.001]


x, y, z = test()
print(f"x = {x}, 类型是 {type(x)}; y = {y}, 类型是 {type(y)}; z = {z}, 类型是 {type(z)}")


"""
函数的多种传参方式:
    位置参数: 传递的参数和定义的参数的顺序及个数必须一致
    关键字参数: 函数调用时通过“键=值”形式传递参数. 
        可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求.
        可以不按照固定顺序
    不定长参数
    缺省参数
"""


def user_info_1(name, age, gender):
    print(f"name={name}, age={age}, gender={gender}")


# 位置传参
user_info_1('Tom', 10, 'male')

# 关键字传参, 可以不按照固定顺序
user_info_1(age=11, gender="male", name="Tom")

# 位置传参 和 关键字传参 可以混用, 位置参数必须在前, 且匹配参数顺序. 关键字传参可以不按照固定顺序
user_info_1("Tom", gender="male", age=12)


# 设置函数的默认参数值, 设置默认值的这个参数必须在参数列表的最后面
def user_info_2(name, age, gender="male"):
    print(f"name={name}, age={age}, gender={gender}")


user_info_2("Joy", age=12)


# 不定长参数(可变参数), 位置传递, 形参前面用一个 * 号
def user_info_3(*args):     # args 是形参变量名字,变量名字可以是任意的. 传进来的所有参数会被这个变量收集, 这个变量是元组类型，这就是位置传递
    print(f"args的值为 {args}, 类型为 {type(args)}")


# 不定长参数(可变参数), 关键字传递, 形参前面用二个 * 号
def user_info_4(**kwargs):    # args 是形参变量名字,变量名字可以是任意的. 传进来的所有参数会被这个变量收集, 这个变量是字典类型，这就是关键字传递
    print(f"args的值为 {kwargs}, 类型为 {type(kwargs)}")


user_info_3("aa", "bb", 1.0001)
user_info_4(name="kerr", age=10, gender="male", addr="china")


"""
匿名函数
    函数作为函数参数
    lambda匿名函数
        def关键字，可以定义带有名称的函数, 有名称的函数，可以基于名称重复使用。
        lambda关键字，可以定义匿名函数（无名称）, 无名称的匿名函数，只可临时使用一次。
    lambda匿名函数定义语法:
        lambda 传入参数: 函数体(一行代码)
    注意:
        lambda 是关键字，表示定义匿名函数
        传入参数表示匿名函数的形式参数，如：x, y 表示接收2个形式参数
        函数体，就是函数的执行逻辑，要注意：只能写一行，无法写多行代码
        lambda 不用写return语句,直接就是return的
"""


# 将函数作为函数的参数
def calculator(calculate):
    print(f"calculate的值为{calculate}, 类型为{type(calculate)}")
    result = calculate(10, 20)
    print(f"result = {result}")


def add(a, b):
    return a + b


# 将函数作为函数的参数, 是计算逻辑的传递，而非数据的传递
calculator(add)


# lambda匿名函数, 使用def和使用lambda，定义的函数功能完全一致，只是lambda关键字定义的函数是匿名的，无法二次使用
calculator(lambda a, b: a + b)      # "lambda a, b: a + b" 这就是一个函数, "a, b"是形参, "a + b"是函数体,是函数的逻辑



