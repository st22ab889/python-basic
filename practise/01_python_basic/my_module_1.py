def test(a, b):
    print(f"from my_module_1 : {a} + {b} = {a + b}")
    print(f"__name__ : {__name__}")


def test_2(a, b):
    print(f"from my_module_1 : {a} * {b} = {a * b}")
    print(f"__all__ : {__all__}")

"""
测试模块
    在实际开发中，当一个开发人员编写完一个模块后，为了让模块能够在项目中达到想要的效果，
    这个开发人员会自行在py文件中添加一些测试信息，例如，在my_module_1.py文件中添加测试代码test(5, 3)

问题: 
    此时，无论是当前文件，还是其他已经导入了该模块的文件，在运行的时候都会自动执行`test`函数的调用
    
解决方案:
    只在当前文件中调用该函数，其他导入的文件内不符合该条件，则不执行test函数调用
        if __name__ == '__main__':
            test (1, 1)
    解释：
        "__name__"是python的内置变量:
            当直接运行此python文件时, "__name__"的值就会被就会被设置为"__main__", 所以这时"__name__ == '__main__'"的值就为True
            如果这个文件是以模块的形式导入,通过其它文件调用此模块时, "__name__"的值就是此python文件的文件名,  所以这时"__name__ == '__main__'"的值就为False
    
"""


# test(5, 3)       # 直接这样写有问题


if __name__ == '__main__':
    test(5, 3)



"""
如果一个模块文件中有`__all__`变量, "__all__"也是python的内置变量:
    当使用`from xxx import *`导入时，只能导入这个列表中的元素
    当使用`from xxx import 功能名`导入时， 可以使用这个功能，即使这个功能没在`__all__`变量中定义
"""
__all__ = ['test']