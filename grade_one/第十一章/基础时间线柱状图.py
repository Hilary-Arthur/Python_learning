from pyecharts.charts import Timeline, Bar
from pyecharts.options import LabelOpts

# 时间线对象
timeline = Timeline()
# 柱状图对象
bar1 = Bar()
bar2 = Bar()

bar1.add_xaxis(["中国","美国","英国"])
bar2.add_xaxis(["中国","美国","英国"])
bar1.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(
    position="right"
))
bar2.add_yaxis("GDP",[100,30,20],label_opts=LabelOpts(
    position="right"
))
# 翻转坐标轴
bar1.reversal_axis()
bar2.reversal_axis()
# 添加时间线
timeline.add(bar1,"2021年GDP")
timeline.add(bar2,"2022年GDP")
# 通过时间线绘制
timeline.render("基础时间线柱状图.html")