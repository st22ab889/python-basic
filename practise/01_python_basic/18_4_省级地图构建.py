
"""
省级地图构建
"""
import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

f_file = open("./可视化案列数据/地图数据/疫情.txt", "r", encoding="UTF-8")
data = f_file.read()
f_file .close()

# 将字符串json转换为python的字典
data_dict = json.loads(data)

# 取出省份的数据
cities_data = data_dict["areaTree"][0]["children"][7]["children"]

data_list = []
for city_data in cities_data:
    city_name = city_data["name"] + "市"
    city_confirm = city_data["total"]["confirm"]
    data_list.append((city_name, city_confirm))


print(data_list)

my_map = Map()

my_map.add("广东省确诊人数", data_list, "广东")


# 设置全局选项
my_map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,                  # 表示是否分段, 如果开启表示开启手动校准范围
        pieces=[                            # 设置自定义分段范围
            {"min": 1, "max": 99, "label": "1-99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999人", "color": "#FF6666"},
            {"min": 1000, "max": 4999, "label": "1000-9999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "1000-9999人", "color": "#FF9966"},
            {"min": 10000, "max": 99999, "label": "10000-99999人", "color": "#CC3333"},
            {"min": 100000, "label": "100000以上", "color": "#990033"},
        ]
    )
)

my_map.render("广东省疫情地图.html")


