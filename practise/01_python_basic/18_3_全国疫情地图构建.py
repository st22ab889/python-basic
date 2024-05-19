
"""
全国地图构建
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
province_data_list = data_dict["areaTree"][0]["children"]

data_list = []
# 组装每个省份和确诊人数为为元组, 然后把每个省的数据都封装在列表内
for province_data in province_data_list:
    province_name = province_data["name"]
    province_confirm = province_data["total"]["confirm"]

    if province_name == '内蒙古' or province_name == '西藏':
        province_name = province_name + "自治区"

    if province_name == '宁夏':
        province_name = province_name + "回族自治区"

    if province_name == '新疆':
        province_name = province_name + "维吾尔自治区"

    if province_name == '澳门' or  province_name == '香港':
        province_name = province_name + "特别行政区"

    if province_name == '广西':
        province_name = province_name + "壮族自治区"

    if province_name == '北京' or province_name == '天津' or province_name == '上海' or province_name == '重庆':
        province_name = province_name + "市"

    if len(province_name) == 2 or province_name == '黑龙江':
        province_name = province_name + "省"

    data_list.append((province_name, province_confirm))


print(data_list)

my_map = Map()

my_map.add("各省份确诊人数", data_list, "china")

# 设置全局选项
my_map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,                  # 表示是否分段, 如果开启表示开启手动校准范围
        pieces=[                            # 设置自定义分段范围
            {"min": 1, "max": 99, "label": "1-99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999人", "color": "#FF6666"},
            {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#FF9966"},
            {"min": 10000, "max": 99999, "label": "10000-99999人", "color": "#CC3333"},
            {"min": 100000, "label": "100000以上", "color": "#990033"},
        ]
    )
)

my_map.render("全国疫情地图.html")
