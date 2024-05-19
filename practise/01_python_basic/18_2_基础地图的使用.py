
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 地图对象
my_map = Map()

data = [
    ("北京市", 99),
    ("上海市", 199),
    ("广东省", 399),
    ("四川省", 299),
    ("台湾省", 599),
    ("香港特别行政区", 499)
]

# 设置全局选项
my_map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,                  # 开启手动校准范围
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#FF6666"},
            {"min": 100, "max": 500, "label": "100-500", "color": "#990033"}
        ]
    )
)

my_map.add("地图", data, "china")

my_map.render()
