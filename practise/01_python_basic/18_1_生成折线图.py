"""
折线图开发
"""

import json
from pyecharts.charts import Line
from pyecharts.options import LabelOpts, TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, TooltipOpts


def handle_data(path, str_replaced):
    try:
        f_file = open(path, "r", encoding="UTF-8")
        data = f_file.read()
        # 去掉不符合Json规范的数据
        data = data.replace(str_replaced, "")
        data = data[:-2]
        # JSON 转 Python 字典
        dict_data = json.loads(data)

        trend_data = dict_data['data'][0]['trend']          # 获得 trend key
        x_data = trend_data['updateDate'][:314]             # 获取日期数据,用于x轴,取2020年(到314下标结束)
        y_data = trend_data['list'][0]['data'][:314]        # 获取日期数据,用于y轴,取2020年(到314下标结束)
        return x_data, y_data
    except Exception as e:
        print(f"内部逻辑错误: {e}")
    finally:
        f_file.close()


x_us_data, y_us_data = handle_data("./可视化案列数据/折线图数据/美国.txt", "jsonp_1629344292311_69436(")
print(x_us_data)
print(y_us_data)


x_in_data, y_in_data = handle_data("./可视化案列数据/折线图数据/印度.txt", "jsonp_1629350745930_63180(")
print(x_in_data)
print(y_in_data)

x_jp_data, y_jp_data = handle_data("./可视化案列数据/折线图数据/日本.txt", "jsonp_1629350871167_29498(")
print(x_jp_data)
print(y_jp_data)

line = Line()                   # 得到折线图对象
line.add_xaxis(x_us_data)       # 添加X轴数据,x轴是公用的,所以使用一个国家的数据即可

# 添加y轴数据, LabelOpts表示设置系列的属性, 控制它的基础行为. "is_show=False"表示不要在折线图上显示具体的数据,当鼠标移动到对应的位置时才显示
line.add_yaxis("美国确诊人数", y_us_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", y_in_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", y_jp_data, label_opts=LabelOpts(is_show=False))

line.set_global_opts(
    title_opts=TitleOpts(title="2020年每日印三国确诊人数对比折线图", is_show=True, pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
    tooltip_opts=TooltipOpts(is_show=True),
)

line.render()

