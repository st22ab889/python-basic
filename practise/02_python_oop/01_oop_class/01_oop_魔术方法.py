"""
几种常用的类内置方法:
    上文的 __init__ 构造方法，是Python类内置的方法之一。这些内置的类方法，各自有各自特殊的功能，这些内置方法称之为"魔术方法"

__str__ 字符串方法
    当类对象需要被转换为字符串之时，会输出" <__main__.xxxx object at 0x000001FE892DE390>"类似结果（内存地址）
    内存地址没有多大作用，可以通过__str__方法，控制类转换为字符串的行为

__lt__ 小于符号比较方法
    直接对2个对象进行比较是不可以的，但是在类中实现__lt__方法，即可同时完成小于符号 和 大于符号 2种比较

__le__ 小于等于比较符号方法
    可用于：<=、>= 两种比较运算符上。
    注意: >= 符号实现的魔术方法是 __ge__ , 不过实现了 __le__ , 那么 __ge__ 就没必要实现了

__eq__，比较运算符实现方法
    不实现__eq__方法，对象之间可以比较，但是是比较内存地址，也即是：不同对象==比较一定是False结果。
    实现了__eq__方法，就可以按照自己的想法来决定2个对象是否相等了。
"""


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print(f"大家好,我是 {self.name}")

    def __str__(self):
        return f"Student类对象, name={self.name}, age={self.age}"

    def __lt__(self, other):
        return self.age < other.age         # 也可以写为 elf.age > other.age ,  "__lt__"方法支持 < 和 > 两种符号

    def __le__(self, other):
        return self.age >= other.age        # 也可以写为 elf.age <= other.age ,  "__le__"方法支持 <= 和 >= 两种符号

    # 如果" __eq__"没有自定义实现, 默认比较的是两个对象的内存地址
    def __eq__(self, other):
        return self.age == other.age        # "__eq__"方法支持 ==


stu_1 = Student("Tom", 30)
print(stu_1)
print(str(stu_1))

stu_2 = Student("Lily", 25)

print(stu_1 > stu_2)
print(stu_1 >= stu_2)
print(stu_1 == stu_2)

