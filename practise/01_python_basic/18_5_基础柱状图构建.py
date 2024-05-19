
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

bar = Bar()

# 添加X轴以及y轴的数据
bar.add_xaxis(["China", "the United States", "United Kingdom"])
bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))  # "LabelOpts(position="right")"设置数值在柱的右边显示

# 反转x和y轴
bar.reversal_axis()

bar.render("基础柱状图.html")

