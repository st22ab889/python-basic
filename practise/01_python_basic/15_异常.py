"""
当python解释器遇到错误(异常),就无法继续运行

异常的捕获, 基本语法如下:
    try:
        可能发生错误的代码
    except:
        如果出现异常运行的代码

捕获指定的异常:
    try:
        可能发生错误的代码
    except NameError as e:
        如果出现异常运行的代码

捕获多个异常:
    try:
        可能发生错误的代码
    except (NameError_1, NameError_2,... ,NameError_N):
        如果出现异常运行的代码

捕获所有异常:
    try:
        可能发生错误的代码
    except Exception as e:
        如果出现异常运行的代码

异常 else, 没有异常姚运行的代码
    try:
        可能发生错误的代码
    except Exception as e:
        如果出现异常运行的代码
    else:
       没有异常姚运行的代码

finally 表示无论是否有异常都要运行
    try:
        可能发生错误的代码
    except Exception as e:
        如果出现异常运行的代码
    else:
       没有异常姚运行的代码
    finally:
        有没有异常都要运行

"""

# 捕获异常,默认捕获所有异常
my_str = "python"
try:
    my_int = int(my_str)
except:
    print("出现异常, 字符串不能转换为整形")


# 捕获指定的异常
try:
    my_int = int(my_str)
except ValueError as e:
    print(f"异常信息：{e}")


# 捕获多个异常, 未正确设置捕获异常类型, 将无法捕获异常
try:
    1/0
except (ValueError, ZeroDivisionError) as e:
    print(f"异常信息：{e}")


# 捕获所有异常, Exception是个所有的异常对象的顶级异常, 一般使用这种方式捕获所有异常，
try:
    1/0
except Exception as e:
    print(f"异常信息：{e}")


# 异常 else, 没有异常姚运行的代码; finally 表示无论是否有异常都要运行
try:
    1/1
except Exception as e:
    print(f"异常信息：{e}")
else:
    print("没有异常")
finally:
    print("有没有异常都要运行此代码")


"""
异常具有传递性, 如果一个函数有异常，当调用这个函数的时候, 这个异常也会传递!
当所有函数都没有捕获异常的时候,程序就回报错!
"""


def func_1():
    1/0


def fun_2():
    func_1()


def main():
    try:
        fun_2()
    except Exception as ee:             # func_1 发生的异常在这里能捕获到
        print(f"异常信息: {ee}")


main()


