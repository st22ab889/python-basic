"""
多态指的是多种状态，即完成某个行为时，使用不同的对象会得到不同的状态。

抽象类（接口）:含有抽象方法, 方法体是空实现的（pass）称之为抽象方法
    这种设计的含义是：
        父类用来确定有哪些方法
        具体的方法实现，由子类自行决定
    抽象类的作用
        多用于做顶层设计（设计标准），以便子类做具体实现。
        也是对子类的一种软性约束，要求子类必须复写（实现）父类的一些方法
        并配合多态使用，获得不同的工作状态。

抽象类配合多态，完成:
    抽象的父类设计（设计标准）
    具体的子类实现（实现标准
"""


class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("dog......")


class Cat(Animal):
    def speak(self):
        print("cat......")


def make_noise(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()
make_noise(dog)     # 形参接收的是父类的类型, 但实际传递的是子类的对象
make_noise(cat)




