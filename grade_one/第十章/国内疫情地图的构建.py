# 进行数据清洗:选择日期为关键字，排列各个城市的数据
import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

city = set()
# 首先获得各个省的名称
with open("json数据/china_provincedata.json","r",encoding="UTF-8") as f:
    data = json.load(f)
    data = data.get("RECORDS",[])
    for i in data:
        city.add(i["provinceName"])
    # 将集合转换为列表,避免无序
    city = list(city)
file_path = list()
# 然后将各个省的确诊人数写进各自的列表，读取confirmedCount
def get_province_data(city,file_path,data):
    try :
        tmp = ""
        if city == "台湾":
            tmp = city
            city = "台湾省"
        elif city == "香港":
            tmp = city
            city = "香港特别行政区"
        elif city == "澳门":
            tmp = city
            city = "澳门特别行政区"
        tmp_path = f"province/{city}.txt"
        tmp_list = list()
        for i in data:
            # 如果总的数据的名字等于当前传入的city名，那么就写入临时列表
            if i["provinceName"] == city:
                tmp_list.append(i["confirmedCount"])
            elif i["provinceName"] == tmp:
                tmp_list.append(i["confirmedCount"])
            elif i["provinceName"] == tmp:
                tmp_list.append(i["confirmedCount"])
            elif i["provinceName"] == tmp:
                tmp_list.append(i["confirmedCount"])
        with open(tmp_path,"w",encoding="UTF-8") as w:
            for j in tmp_list:
                w.write(j)
                w.write("\n")
        file_path.append(tmp_path)
    except Exception as e:
        print(f"发生错误:{e}")

for i in city:
    get_province_data(i,file_path,data)

# 快速排序获得最大数
import QuickSort.quicksort as quick
def get_province_data_list(file_path):
    province_data_list = list()
    try :
        for i in file_path:
            f = open(i,"r",encoding="UTF-8")
            info = list()
            for j in f:
                # 字符串的规整会生成新的字符串
                j = j.strip()
                info.append(j)
            # print(info)
            # quick.quickSort(0,len(info)-1,info)
            # 问题出现在快速排序,原本有序，无需排序
            final = info[-1]
            province_data_list.append(final)
    except Exception as e:
        print(f"发生错误:{e}")
    finally:
        if f:
            f.close()
    return province_data_list

def write_final(province,province_data):
    final_dict = dict()
    if len(province_data) == len(province):
        i = 0
        while i < len(province_data):
            index_1 = province[i].index("/")
            index_2 = province[i].index(".")
            name = province[i][index_1+1:index_2]
            final_dict[name] = province_data[i]
            i += 1
    return final_dict

province_data_list = get_province_data_list(file_path)# map_data已经出现问题
map_data = write_final(file_path,province_data_list)


def get_list(data):
    map_list = list()
    for i in data:
        tmp_tunple = (i,data[i])
        map_list.append(tmp_tunple)
    return map_list

def draw_map(data):
    map = Map()
    map.add("国内疫情地图",data,"china")
    # 视觉映射器
    map.set_global_opts(
        visualmap_opts=VisualMapOpts(
            is_show=True,
            is_piecewise=True,
            pieces=[
                {"min":1,"max":9,"label":"1-9人","color":"#CCFFFF"},
                {"min":10,"max":99,"label":"10-99人","color":"#FFFF99"},
                {"min":100,"max":499,"label":"100-499人","color":"#FF9966"},
                {"min": 500, "max": 999, "label": "500-999人", "color": "#FF6666"},
                {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#CC3333"},
                {"min": 10000, "label": "10000人以上", "color": "#FF990033"}
            ]
        )
    )
    # 绘图
    map.render("国内疫情地图.html")

map_list = get_list(map_data)
draw_map(map_list)