"""
在类中定义私有成员：
    私有成员变量：变量名以__开头（2个下划线）
    私有成员方法：方法名以__开头（2个下划线）
"""


class Phone:
    __current_voltage = 0.5

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self. __keep_single_core()
            print("电量不足, 无法使用5g通话, 并已设置为单核运行进行省电.")


phone = Phone()
# print(f"{phone.__current_voltage}")        # 无论是访问类的私有成员还是私有方法都会报错
phone.call_by_5g()
