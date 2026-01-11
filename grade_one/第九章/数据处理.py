# 得到的数据格式已经为标准的json格式
import json
from pyecharts.charts import Line
from pyecharts.options import *
def get_data():
    file_path = "COVID-19-Data-master/json格式/countrydata.json"
    try :
        with open(file_path,"r",encoding="UTF-8") as r:
            data = json.load(r)
            data = data.get("RECORDS", [])
    except Exception as e :
            print(e)
    return data
# 将json数据转化为字典,注意json格式是列表套多个字典
# 创建一个专门用于接收美国数据的字典
# 需要的数据:id、时间id、累计确诊、新增确诊、累计死亡、新增死亡、累计治愈、新增治愈
def get_country(data):
    tmp_Country = set()
    for i in data:
        tmp_Country.add(i["countryName"])
    return list(tmp_Country)

def get_only_data(data,country="美国"):
    DATA = list()

    for i in data:
        tmp_dict = dict()
        # 重新使用一个临时字典来存放找到的数据
        if i["countryName"] == country:
            tmp_dict["id"] = i["id"]
            tmp_dict["dateId"] = i["dateId"]
            tmp_dict["confirmedCount"] = i["confirmedCount"]
            tmp_dict["confirmedIncr"] = i["confirmedIncr"]
            tmp_dict["deadIncr"] = i["deadIncr"]
            tmp_dict["deadCount"] = i["deadCount"]
            tmp_dict["curedIncr"] = i["curedIncr"]
            tmp_dict["curedCount"] = i["curedCount"]
            # 上述操作完成了对一条字典的处理，将其暂存至tmp_dict中
            # 将该数据存放至列表里面
            DATA.append(tmp_dict)
    data_path = f"json文件/{country}_DATA.json"
    with open(f"{data_path}","w",encoding="UTF-8") as w:
        try :
            DATA = json.dumps(DATA,ensure_ascii=False)
            w.write(DATA)
            w.flush()
            print(f"{country}新冠疫情数据写入成功，即将对数据进行处理")
        except Exception as e:
            print(e)
    return data_path


def build_line(data_path,name):
    # 处理得到的国家数据
    line = Line()
    f = open(f"{data_path}","r",encoding="UTF-8")
    data = json.load(f)
    x_list = list()
    y_dict = dict()
    for i in data:
        x_list.append(i["dateId"])
    line.add_xaxis(x_list)
    # 对纵坐标进行处理
    get_dict_key = data[0]
    keys = list(get_dict_key.keys())
    for i in keys:
        if i != "id" and i != "dateId":
            y_dict[i] = None

    # 再获取每个数据的列表
    i = 0
    while i < len(y_dict):
        keys = list(y_dict.keys())
        tmp_list = list()
        for j in data:
            tmp_list.append(j[keys[i]])
        y_dict[keys[i]] = tmp_list
        line.add_yaxis(keys[i],tmp_list)
        i += 1

    line.set_global_opts(
        # xaxis_opts=opts.AxisOpts(name="专业代码",name_rotate=0,name_textstyle_opts={"color": "black","fontSize":15},axislabel_opts={"rotate":45,"color":"blue","fontSize":12},is_show =True,is_inverse = False, name_location = 'center'),

        title_opts=TitleOpts(title=f"{name}", pos_left="center", pos_bottom="1%"),
        legend_opts=LegendOpts(is_show=True),
        # 工具箱
        toolbox_opts=ToolboxOpts(is_show=True),
        # 视觉
        visualmap_opts=VisualMapOpts(is_show=True),
    )

    # 生成折线图
    line.render(f"折线图/{name}.html")
    f.close()

data = get_data()
country = get_country(data)
data_path = list()
print(country)
for i in country:
   #  这里是朝着列表里面追加数据，同时得到的文件路径根据国家决定，因此不能使用集合，因为集合无序
   data_path.append(get_only_data(data,country=i))

if len(data_path) == len(country):
    j = 0
    while j < len(data_path):
        print(f"正在画出{country[j]}的折线图,json文件路径为{data_path[j]}")
        build_line(data_path[j],country[j])
        j += 1
else :
    print(f"数据长度不一致请再次检查,国家长度{len(country)},数据路径长度{len(data_path)}")

