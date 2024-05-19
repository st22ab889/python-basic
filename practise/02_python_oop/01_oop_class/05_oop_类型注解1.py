"""
类型注解:
    Python在3.5版本的时候引入了类型注解，以方便静态类型检查工具，IDE等第三方工具。
    类型注解：在代码中涉及数据交互的地方，提供数据类型的注解（显式的说明）。

主要功能：
    帮助第三方IDE工具（如PyCharm）对代码进行类型推断，协助做代码提示
    帮助开发者自身对变量进行类型注释

支持：
    变量的类型注解。基础语法如下:
        变量: 类型
    函数（方法）形参列表和返回值的类型注解
"""

# 基础数据类型注解
import json
import random

var_1: int = 10         # 说明 var 的类型是 int
var_2: float = 3.14
var_3: bool = True


# 基础容器类型注解
var_4: str = "字符串"
var_5: list = [1, 2, 3]
var_6: tuple = (1, 2, 3)
var_7: set = {1, 2, 3}
var_8: dict = {"str": "字符串"}


"""
容器类型详细注解(这种用法比较多)

注意：
    元组类型设置类型详细注解，需要将每一个元素都标记出来
    字典类型设置类型详细注解，需要2个类型，第一个是key第二个是value
"""
var_9: list[int] = [1, 2, 3]
var_10: tuple[str, int, bool] = ("字符串", 2222, 3.14)
var_11: set[int] = {1, 2, 3}
var_12: dict[str, int] = {"age": 30}


# 类对象类型注解
class Student:
    pass

# 说明 stu 这个对象的类型是 Student
stu: Student = Student()



"""
在注释中进行类型注解
    除了使用 变量: 类型， 这种语法做注解外，也可以在注释中进行类型注解。
语法：
   # type: 类型
"""
# 标记 var_13 这个变量是 int 类型
var_13 = random.randint(1, 10)                   # type:int
var_14 = json.loads('{"age": 30}')               # type:dict
var_15 = Student()                               # type:Student


"""
为变量设置注解，显示的变量定义，一般无需注解：
    var_1: int = 10                     # 这就是"显示的变量定义",一眼就能看出来类型
    var_5: list = [1, 2, 3]
    var_8: dict = {"str": "字符串"}
    stu: Student = Student()
    
一般，无法直接看出变量类型之时会添加变量的类型注解, 如下：
    var_13: int = random.randint(1, 10)
    var_14: dict = json.loads(data)
    def func():
        return 10
    var_15: int = func()      
"""



"""
类型注解的限制, 
    类型注解主要功能在于：
        帮助第三方IDE工具（如PyCharm）对代码进行类型推断，协助做代码提示
        帮助开发者自身对变量进行类型注释(备注),并不会真正的对类型做验证和判断。也就是，类型注解仅仅是提示性的，不是决定性的
"""
var_16: int = "字符串"     # 这里虽然注解的类型和实际变量类型不匹配, 但是也不会报错
var_16: str = 123
