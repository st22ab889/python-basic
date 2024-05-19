"""
装饰器：装饰器其实也是一种闭包， 其功能就是在不破坏目标函数原有的代码和功能的前提下，为目标函数增加新功能。

装饰器的写法：
    装饰器的一般写法(闭包写法)
    装饰器的语法糖写法
"""


# 装饰器一般写法：增强 sleep 函数的功能
def sleep():
    import random
    import time
    print("睡眠中......")
    time.sleep(random.randint(1, 5))


def outer(func):
    def inner():
        print("睡觉了")
        func()
        print("睡醒了")
    return inner


fun_1 = outer(sleep)
fun_1()


print("---------------------------------------------------------------------")


# 装饰器的语法糖写法：增强 sleep 函数的功能
def outer2(func):
    def inner():
        print("...睡觉了")
        func()
        print("...睡醒了")
    return inner


@outer2()
def sleep2():
    import random
    import time
    print("...睡眠中......")
    time.sleep(random.randint(1, 5))


sleep2()


"""
参考资料：
    python的装饰器如何传参：https://blog.csdn.net/qq_22795513/article/details/121950953
"""



