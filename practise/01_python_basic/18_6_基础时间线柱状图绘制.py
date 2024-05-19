"""
Timeline()-时间线
    柱状图描述的是分类数据，回答的是每一个分类中『有多少？』这个问题. 这是柱状图的主要特点,同时柱状图很难动态的描述一个趋势性的数据.
    这里pyecharts为我们提供了一种解决方案-时间线

如果说一个Bar、Line对象是一张图表的话，时间线就是创建一个一维的x轴，轴上每一个点就是一个图表对象
"""

from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts


bar_1 = Bar()
bar_1.add_xaxis(["China", "the United States", "United Kingdom"])
bar_1.add_yaxis("GDP", [30, 20, 80], label_opts=LabelOpts(position="right"))  # "LabelOpts(position="right")"设置数值在柱的右边显示
bar_1.reversal_axis()

bar_2 = Bar()
bar_2.add_xaxis(["China", "the United States", "United Kingdom"])
bar_2.add_yaxis("GDP", [50, 30, 60], label_opts=LabelOpts(position="right"))  # "LabelOpts(position="right")"设置数值在柱的右边显示
bar_2.reversal_axis()

bar_3 = Bar()
bar_3.add_xaxis(["China", "the United States", "United Kingdom"])
bar_3.add_yaxis("GDP", [80, 600, 20], label_opts=LabelOpts(position="right"))  # "LabelOpts(position="right")"设置数值在柱的右边显示
bar_3.reversal_axis()

# 构建时间线对象并设置主题
timeline = Timeline({"theme": ThemeType.LIGHT})
timeline.add(bar_1, "2010")
timeline.add(bar_2, "2011")
timeline.add(bar_3, "2012")

# 设置自动播放
timeline.add_schema(
    play_interval=1000,         # 播放间接
    is_timeline_show=True,      # 是否显示时间线
    is_auto_play=True,          # 是否自动播放
    is_loop_play=True           # 是否循环播放
)

timeline.render("基础时间线柱状图.html")

