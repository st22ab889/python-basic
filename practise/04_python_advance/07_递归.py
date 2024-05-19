"""
递归： 即方法（函数）自己调用自己的一种特殊编程写法，递归在编程中是一种非常重要的算法

最典型的递归场景为找出一个文件夹中全部的文件。
"""


import os


def test():
    print(os.listdir('./..'))       # 列出路径下的内容
    print(os.path.isdir('./'))      # 判断指定路径是不是文件夹
    print(os.path.exists('./'))     # 判断指定路径是否存在


def get_files_recursion_from_dir(path):
    """
    从指定的文件夹中使用递归的方式, 获取全部的文件列表
    :param path: 文件夹
    :return: list, 包含全部的文件, 如果目录不存在或者无文件就返回一个空list
    """
    print(path)

    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + "/" + f
            if os.path.isdir(new_path):
                file_list += get_files_recursion_from_dir(new_path)
            else:
                file_list.append(new_path)
    else:
        print(f"指定的目录 {path} 不存在")
        return []

    return file_list


if __name__ == '__main__':
    test()
    print("---------------------------------------------------------------------------")
    file_data = get_files_recursion_from_dir('./..')
    print(file_data)





