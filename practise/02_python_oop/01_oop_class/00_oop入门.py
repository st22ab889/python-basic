"""
在类中定义成员方法和定义函数基本一致，但仍有细微区别. 成员方法的定义语法如下:
    def 方法名(self, 参数1, 参数2, ..., 参数N):
        方法体

可以看到，在方法定义的参数列表中，有一个self关键字, self关键字是成员方法定义的时候，必须填写的。
    它用来表示类对象自身的意思
    当我们使用类对象调用方法时，self会自动被python传入
    在方法内部，想要访问类的成员变量，必须使用self

注意事项:
    self关键字，尽管在参数列表中，但是传参的时候可以忽略它。
"""


class Student:
    name = None
    gender = None
    age = None

    def say_hi(self):                                # self关键字是成员方法定义的时候，必须填写的.
        print(f"大家好,我是 {self.name}")             # 在方法内部，想要访问类的成员变量，必须使用self.

    def say_hi_msg(self, msg):
        print(f"大家好,我是 {self.name}, {msg}")


stu_1 = Student()
stu_1.name = "Tom"
stu_1.gender = "male"
stu_1.age = 30

print(f"stu_1 的值 {stu_1}, 类型为 {stu_1}")
stu_1.say_hi()                                       # 传参的时候可以忽略self关键字
stu_1.say_hi_msg("你们好!")



"""
Python类可以使用：__init__()方法，称之为构造方法。可以实现：
    在创建类对象（构造类）的时候，会自动执行。
    在创建类对象（构造类）的时候，将传入参数自动传递给__init__方法使用。
    构造方法也是成员方法，不要忘记在参数列表中提供：self
    在构造方法内定义成员变量，需要使用self关键字.这是因为：变量是定义在构造方法内部，如果要成为成员变量，需要用self来表示
"""


class Person:

    # 如果在构造方法中已经给成员变量赋值,就不用再声明定义成员变量, 相当于在构造函数中既声明又赋值
    # 如果声明了成员变量, 构造函数就相当于赋值功能
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def say_hi(self):
        print(f"大家好,我是 {self.name}")

    def say_hi_msg(self, msg):
        print(f"大家好,我是 {self.name}, {msg}")


person_1 = Person("Lily", "female", 30)
person_1.say_hi()
