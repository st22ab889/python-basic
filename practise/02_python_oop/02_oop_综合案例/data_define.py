"""
定义数据的类
"""


class Record:
    date = None
    order_id = None
    money = None
    province = None

    def __init__(self, date, order_id, money, province):
        self.date = date  # 订单日期
        self.order_id = order_id
        self.money = money
        self.province = province  # 销售省份

    def __str__(self):
        #  下面两种写法都可以拼接字符串
        # return self.date + ", " + self.order_id + ", " + str(self.money) + ", " + self.province
        return f"{self.date}, {self.order_id}, {self.money}, {self.province}"

