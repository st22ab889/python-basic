"""
数据可视化
    折线图可视化
    地图
    动态柱状图

使用的技术: Echarts
    Echarts是个由百度开源的数据可视化，凭借着良好的交互性，精巧的图表设计，得到了众多开发者的认可. 而Python是门富有表达力的语言，很适合用于数据处理. 当数据分析遇上数据可视化时, pyecharts 诞生了.
    Echarts本身是用于 JavaScript 的语言, 但是也提供了 Python 语言的相关包, 这个包就叫做 pyecharts
    pyecharts模块安装:
        pip install pyecharts
    官方示例:
        官网: https://pyecharts.org/#/zh-cn/intro
        官方画廊(画廊是pyecharts的一个功能)：https://gallery.pyecharts.org/#/README
"""

# Json数据和Python字典的相互转换

# 将 Python 列表转换为Json
import json
data = [{"name": "admin", "age": 18}, {"name": "root", "age": 16}, {"name": "张三", "age": 20}]
json_str = json.dumps(data, ensure_ascii=False)                     # "ensure_ascii=False"参数确保中文可以正常转换
print(f"json_str数据为 {json_str}, 类型为 {type(json_str)}")


# 将 Python 字典转换为Json
data = {"name": "root", "password": 123456}
json_str = json.dumps(data, ensure_ascii=False)
print(f"json_str数据为 {json_str}, 类型为 {type(json_str)}")


# 将 Json 转换为 Python 列表
json_str = '[{"name": "admin", "age": 18}, {"name": "root", "age": 16}, {"name": "张三", "age": 20}]'
data = json.loads(json_str)
print(f"data数据为 {data}, 类型为 {type(data)}")


# 将 Json 转换为 Python 字典
json_str = '{"name": "root", "password": 123456}'
data = json.loads(json_str)
print(f"data数据为 {data}, 类型为 {type(data)}")




"""
pyecharts模块中有很多的配置选项, 常用到2个类别的选项:
    全局配置选项：针对整个图像进行设置,比如图像的标题、图像的图例、工具箱等等, 所以全局配置主要针对通用的配置进行设置. 全局配置选项可以通过 set_global_opts 方法来进行配置, 如下:  
        line.set_global_opts (
            title_opts=TitleOpts(title="GDP展示", is_show=True, pos_left="center", pos_bottom="1%"),    # 标题配置项
            legend_opts=LegendOpts(is_show=True),                                                       # 图例配置项
            toolbox_opts=ToolboxOpts(is_show=True),                                                     # 工具箱配置项
            visualmap_opts=VisualMapOpts(is_show=True),                                                 # 视觉映射配置项
            tooltip_opts=TooltipOpts(is_show=True),                                                     # 提示框配置项
        )
    系列配置选项：针对具体的轴数据进行配置.
"""

# pyecharts 入门使用, 首先安装 pyecharts
# pip install pyecharts

# 构建一个基础的折线图
from pyecharts.charts import Line
from pyecharts.options import TitleOpts
from pyecharts.options import LegendOpts
from pyecharts.options import ToolboxOpts
from pyecharts.options import VisualMapOpts
from pyecharts.options import TooltipOpts
line = Line()       # 得到折线图对象
line.add_xaxis(["China", "the United States", "United Kingdom"])    # 添加X轴数据
line.add_yaxis("GDP", [30, 20, 10])                                 # 添加y轴数据

# 使用全局配置项设置属性, 每个配置项都有很多属性可以设置,,具体有哪些属性可以查看源代码或文档, 或者 "ctrl + P" 可以列出参数
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", is_show=True, pos_left="center", pos_bottom="1%"),   # 标题配置项
    legend_opts=LegendOpts(is_show=True),                                                     # 图例配置项, 默认开启显示, 所以不设置也会显示
    toolbox_opts=ToolboxOpts(is_show=True),                                                   # 工具箱配置项
    visualmap_opts=VisualMapOpts(is_show=True),                                               # 视觉映射配置项
    tooltip_opts=TooltipOpts(is_show=True),                                                   # 提示框配置项
    # 全局配置项非常多, 也可以在官网中查看文档(https://pyecharts.org/#/zh-cn/global_options)
)

line.render()   # 生成图表, 运行后会生成"render.html", 在浏览器中打开就会看到图表

