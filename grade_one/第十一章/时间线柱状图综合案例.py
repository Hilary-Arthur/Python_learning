import csv

from pyecharts.charts import Timeline, Bar
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts
from pyecharts.render.engine import render
from pyecharts.types import DataZoom



def read_same_year(year,data):
    container = dict()
    for i in data:
        if i[0] == year:
            # 给字典赋值
            container[i[1]] = i[2]
    # print(year,container,data)
    return container

# 首先对数据进行处理,由于原文件是一个csv文件，所以读取方法和原来的json数据不同
def read_data():
    f = open("gdp数据/1960-2019全球GDP数据.csv","r",encoding="GBK")
    # 跳过第一行
    f.readline()
    data = csv.reader(f)
    data = list(data)
    time_record_set = set()
    result_dict = dict()
    for i in data:
        time_record_set.add(i[0])
    time_record_set = list(time_record_set)
    # 数据的存储选择字典套用字典
    for i in time_record_set:
        # 将一个年份传进去
        tmp_dict = read_same_year(i,data)
        result_dict[i] = tmp_dict
    f.close()
    return result_dict

# 传入的时间关键字
def build_bar(key,data):
    sort_list = list()
    # 横坐标
    country_list = list(data[key].keys())
    # 获取纵坐标
    data_list = list()
    count = 10
    length = count
    for i in country_list:
        if count > 0:
            tmp_list = list()
            tmp_list.append(i)
            tmp_list.append(data[key][i])
            sort_list.append(tmp_list)
            count -= 1
        else :
            break
    i = 0

    while i < len(sort_list):
        # 首先将数字转化为整数类型
        sort_list[i][1] = int(float(sort_list[i][1]))
        i += 1
    # sort_list.sort(key=choose_sort_key,reverse=True)
    # 匿名函数
    sort_list.sort(key=lambda element : element[1], reverse=True)
    for i in sort_list:
        data_list.append(i[1])
    bar = Bar()
    bar.add_xaxis(country_list[0:length-1])
    bar.add_yaxis(f"{key}年GDP",data_list,label_opts=LabelOpts(
        position="right"
    ))
    bar.reversal_axis()
    return key,bar

def choose_sort_key(element):
    return element[1]

def data_type_int(data):
    for i in data:
        index = data.index(i)
        data[index] = int(i)

def data_type_str(data):
    for i in data:
        index = data.index(i)
        data[index] = str(i)

if __name__ == '__main__':
    timeline = Timeline({"theme":ThemeType.LIGHT})
    result_dict = read_data()
    keys = list(result_dict.keys())

    data_type_int(keys)
    keys.sort(key=lambda element : element,reverse=False)
    data_type_str(keys)
    i = 0
    while i < len(keys):
        year,bar = build_bar(keys[i],result_dict)
        timeline.add(bar,f"{year}年GDP")
        i += 1
    timeline.add_schema(
        play_interval=750,
        is_timeline_show=True,
        is_auto_play=True,
        is_loop_play=True
    )
    timeline.render("各年份GDP前十合集.html")