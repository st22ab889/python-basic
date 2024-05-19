"""
对函数(方法)形参进行类型注解
对函数(方法)返回值进行类型注解
使用Union进行联合类型注解
"""


# 对形参进行类型注解
def add(x: int, y: int):
    return x + y


# 对返回值进行类型注解
def func(data: list) -> list:
    return data


# add()    # 调用方法时,光标放在括号中, 按 "ctrl + p" 就能提示出参数的类型


"""
使用Union进行联合类型注解. 
"""
# 描述混合类型就需要使用union类型
my_list = [1, 2, "str", "字符串"]
my_dict = {"name": "Tom", "age": 30}

from typing import Union
my_list: list[Union[str, int]] = [1, 2, "str", "字符串"]           # 表示 list 中的元素既可以是 str 类型, 也可以是 int 类型
my_dict: dict[str, Union[str, int]] = {"name": "Tom", "age": 30}


def func(data: Union[int, str]) -> Union[int, str]:
    pass

