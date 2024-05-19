"""
设计模式是一种编程套路，可以极大的方便程序的开发。最常见、最经典的设计模式，就是面向对象。

除了面向对象外，在编程中也有很多既定的套路可以方便开发，称之为设计模式：
    单例、工厂模式
    建造者、责任链、状态、备忘录、解释器、访问者、观察者、中介、模板、代理模式
    等等模式

单例模式：
    确保某一个类只有一个实例存在
    用以节省创建类对象的开销和内存开销，比如某些工具类，仅需要1个实例，即可在各处使用

工厂模式：
    当需要大量创建一个类的实例的时候， 可以使用工厂模式。
    即，从原生的使用类的构造去创建对象的形式迁移到，基于工厂提供的方法去创建对象的形式。
    优点：
        大批量创建对象的时候有统一的入口，易于代码维护
        当发生修改，仅修改工厂类的创建方法即可
"""

from str_tools import str_tool

# 单例模式
s1 = str_tool
s2 = str_tool

print(id(s1))
print(id(s2))


# 工厂模式
class Person:
    pass


class Worker(Person):
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


class PersonFactory:
    def get_person(self, p_type):       # 方法名下面的波浪线解决方法： https://blog.csdn.net/qq_38025771/article/details/109643678
        if p_type == 'w':
            return Worker()
        elif p_type == 's':
            return Student()
        else:
            return Teacher()


pf = PersonFactory()

worker = pf.get_person('w')
stu = pf.get_person('s')
teacher = pf.get_person('t')
