"""
数据分析案例
"""

from file_define import FileReader, TextFileReader, JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType


text_file_reader = TextFileReader("./2011年1月销售数据.txt")
json_file_reader = JsonFileReader("./2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 将2个月份的数据合并为1个list
all_data: list[Record] = jan_data + feb_data


data_dict = {}
for record in all_data:
    if record in data_dict.keys():
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

print(data_dict)


# 柱状图
bar = Bar(init_opts=InitOpts(ThemeType.LIGHT))
# data_dict.keys() 的类型是"dict_keys", 所以要转换为list
bar.add_xaxis(list(data_dict.keys()))
# data_dict.values() 的类型是"dict_values",要转换为list
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)
bar.render("每日销售柱状图.html")

print(type(data_dict.keys()))
print(type(data_dict.values()))
