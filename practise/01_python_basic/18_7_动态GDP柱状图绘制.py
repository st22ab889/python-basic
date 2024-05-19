"""
列表的sort方法
    sorted函数，可以对数据容器进行排序。在数据处理中，如果需要对列表进行排序，并指定排序规则，sorted函数就无法完成。
    列表的sort方法, 可以自定义排序规则, 使用方式如下:
        列表.sort(key=选择排序依据的函数, reverse=True|False)
    参数解释:
        参数key，是要求传入一个函数，表示将列表的每一个元素都传入函数中，返回排序的依据
        参数reverse，是否反转排序结果，True表示降序，False表示升序
"""

my_list = [["a", 33], ["b", 55], ["c", 11]]


# 基于带名函数：降序排序
def choose_sort_key(element):
    return element[1]


my_list.sort(key=choose_sort_key, reverse=True)
print(my_list)

# 基于lambda函数：降序排序
my_list.sort(key=lambda element: element[1], reverse=True)
print(my_list)



"""
通过pyechars可以实现数据的动态显示, 直观的感受1960~2019年全世界各国GDP的变化趋势
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts, TitleOpts

# ANSI是windows系统的一个默认编码格式, 表示编码是跟随操作系统的语言版本. 比如win11是中文,默认的中文编码叫做 GB2312, 所以这里就是通过 GB2312 打开这个文件
# 1960-2019全球GDP数据.csv 这个文件的编码是 ANSI, 用 记事本打开, 在右下脚区域显示的是 ANSI, 用 notepad++ 打开, 右下脚区域显示的是 GB2312
f_file = open("./可视化案列数据/动态柱状图数据/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
data_lines = f_file.readlines()
f_file .close()

# 第一条数据是标头, 所以要删除
data_lines.pop(0)

# 组装数据
data_dict = {}
for line in data_lines:
    year = line.split(",")[0]
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])

    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# 对年份进行排序
sorted_year_list = sorted(data_dict.keys())
print(sorted_year_list)

# 创建时间线
timeline = Timeline({"theme": ThemeType.LIGHT})

for year in sorted_year_list:
    # 取GDP前8各元素,所以要对列表排序
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出本年份前8名的国家
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])                   # x轴添加国家
        y_data.append(country_gdp[1] / 100000000)       # y轴添加gdp数据

    x_data.reverse()    # 这里数据要反转, 反转后柱状图才会按照GDP从高到底显示,
    y_data.reverse()    # 对应y轴的数据也要反转
    # 构建柱状图
    bar = Bar()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    # 设置每一年的图表的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8的GDP数据")
    )

    timeline.add(bar, str(year))


# 设置时间线自动播放
timeline.add_schema(
    play_interval=1000,         # 播放间接
    is_timeline_show=True,      # 是否显示时间线
    is_auto_play=True,          # 是否自动播放
    is_loop_play=False          # 是否循环播放
)

# 绘图
timeline.render("1960-2019全球GDP前8国家.html")



