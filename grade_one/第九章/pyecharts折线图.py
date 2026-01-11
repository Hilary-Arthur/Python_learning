# 构建一个基础折线图
# 导入包,有多种导入方法
from pyecharts.charts import Line
# import pyecharts as py
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, TooltipOpts

# 得到折线图对象
line = Line()
# 添加x轴数据
line.add_xaxis(["Tom","Anny","Andy"])
# 添加y轴数据
line.add_yaxis("result",[100,98,70])
# 全局配置设计
line.set_global_opts(
    # pos_left:靠近左边有多远，pos_bottom:最底部
    title_opts=TitleOpts(title="成绩",pos_left="center",pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    # 工具箱
    toolbox_opts=ToolboxOpts(is_show=True),
    # 视觉
    visualmap_opts=VisualMapOpts(is_show=True),
)
# 生成图表
line.render()
# 生成的图标为html文件render.html

