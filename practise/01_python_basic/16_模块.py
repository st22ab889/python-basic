"""
模块(Module)就是一个Python文件，里面有类、函数、变量等，可以拿过来用（导入模块去使用）

模块的导入方式:
    导入语法:
        [from 模块名] import [ 模块 | 类 | 变量 | 函数 | * ] [as 别名]
    常用的组合形式如：
        import 模块名
        from 模块名 import 类、变量、方法等
        from 模块名 import *
        import 模块名 as 别名
        from 模块名 import 功能名 as 别名
    注意：
        当模块名字太长时, 使用别名可以定义一个短名字
        模块的导入一般写在文件的开头位置
"""

# 这种方式相当于导入整个模块
import time

# 让程序休眠一秒(让程序中断一秒)
time.sleep(1)

"""
# 只导入某个模块的某个功能
from time import sleep
sleep(1)
"""

"""
# 使用 * 导入time模块的全部功能. 相当于"import time", 但是这种方法使用time模块功能时要在前面加上"time."
from time import *
sleep(1)        # 注意: 这里不用加上"time."
"""

"""
# 模块别名,使用as给模块加上别名
import time as tt
tt.sleep(1)
"""

"""
# 功能别名
from time import sleep as sl
sl(2)
"""


# 自定义模块: 模块的名字就是文件的名字,自定义模块名必须要符合标识符命名规则

"""
# 方式1: 使用自定义模块
import my_module_1
my_module_1.test(2, 3)
"""

"""
# 方式2: 使用自定义模块
from my_module_1 import test
test(2, 3)
"""


# 导入不同模块的同名功能
"""
# 注意事项: 当导入多个模块的时候,且模块内有同名功能,当调用这个同名功能的时候,调用到的是后面导入的模块的功能
from my_module_1 import test        # 如果一行代码变成灰色(和注释的代码一个颜色), 说明这行代码没有被使用
from my_module_2 import test
test(5, 3)
"""


# "__name__变量", 详细查看"my_module_1"


# "__all__"变量, 详细查看"my_module_1"
"""
from my_module_1 import *           # 注意: "__all__"只对 "from 模块名 import *" 有效
test_2(5, 3)
"""

from my_module_1 import test_2      # 当指定功能导入时, 即使这个功能没在"__all__"这个变量的列表中,也能导入这个功能
test_2(5, 3)


