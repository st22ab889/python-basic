"""
继承表示：将从父类那里继承（复制）来成员变量和成员方法（不含私有）
    单继承
    多继承
"""

# 单继承示例


class Phone:
    IMEI = None
    producer = "@_@"

    def call_by_4g(self):
        print("4G 通话")


# PhonePlus 继承自 Phone
class PhonePlus(Phone):
    face_id = "1010101"

    def call_by_5g(self):
        print("5G 通话")

phone = PhonePlus()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()




"""
多继承示例

多继承注意事项: 
    多个父类中，如果有同名的成员(变量和方法)，那么默认以继承顺序(从左到右)为优先级。即：先继承的保留，后继承的被覆盖！
    总结: 谁先继承,谁的优先级就越高！
"""
class NFCReader:
    nfc_type = "最新nfc"
    producer = "*_*"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启")


class PhonePlusPlus(Phone, NFCReader, RemoteControl):
    # pass 关键字用来补充语法, 比如这个类不写任何代码时语法会报错, 但是pass关键字能补全语法, 同时也表示这里没有内容
    pass


phonePP = PhonePlusPlus()
phonePP.call_by_4g()
phonePP.read_card()
phonePP.control()
print(phonePP.producer)         # 这里打印出来是Phone的producer, 说明: 如果继承的有同名的属性, 先继承的保留，后继承的被覆盖. 方法也是一样！






