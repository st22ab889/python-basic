"""
复写：子类继承父类的成员属性和成员方法后，如果对其“不满意”，那么可以进行复写。即：在子类中重新定义同名的属性或方法即可。

调用父类同名成员, 一旦复写父类成员，那么类对象调用成员的时候，就会调用复写后的新成员. 如果需要使用被复写的父类的成员，需要特殊的调用方式:
    方式1：调用父类成员
         使用成员变量：
            父类名.成员变量
         使用成员方法：
            父类名.成员方法(self)
    方式2：使用super()调用父类成员
        使用成员变量：
            super().成员变量
        使用成员方法：
            super().成员方法()

    注意：
        只能在子类内调用父类的同名成员。子类的类对象直接调用会调用子类复写的成员
"""

class Phone:
    IMEI = "1010101"
    producer = "@_@"

    def call_by_4g(self):
        print("4G 通话")


# PhonePlus 继承自 Phone
class PhonePlus(Phone):
    producer = "*_*"        # 复写父类的成员属性
    face_id = "1010101"

    def call_by_4g(self):   # 复写父类的成员方法
        # 方式1：调用父类成员
        print({Phone.producer})
        Phone.call_by_4g(self)          # 这里参数不要忘了加self
        print("4G 通话,改善语音质量")

    def call_by_5g(self):
        # 方式2：调用父类成员
        print({super().producer})
        super().call_by_4g()            # 使用 super() 的方式调用父类方法不用加 self 参数

        print("5G 通话")
        print(self.producer)            # 因为子类已经复写父类成员属性 producer , 所以这里"self.producer"访问的是子类的 producer 属性


phone_plus = PhonePlus()
print(phone_plus.producer)
phone_plus.call_by_4g()
phone_plus.call_by_5g()

# 注意： 只能在子类内调用父类的同名成员。子类的类对象直接调用会调用子类复写的成员


