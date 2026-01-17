import json
import os.path
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts


class Data:
    data = None # type: dict[str,int]
    def change_type(self,filepath):
        with open(filepath,"r",encoding="UTF-8") as f:
            self.data = json.load(f)
            self.data = self.data.get("RECORDS",[])
    def get_info(self):
        pass

    def build_json(self, filename):
        # 先获得所有的keys
        keys_list = self.data.keys()
        with open(filename, "w", encoding="UTF-8") as f:
            tmp_dict = dict()
            for i in keys_list:
                tmp_dict[i] = self.data[i]
            tmp_dict = json.dumps(tmp_dict)
            f.write(tmp_dict)
            print(f"{filename}写入完成")

class Get_CuredIncr(Data):
    __tmp_dict: dict[str, int] = dict()
    def get_info(self):
        for i in self.data:
            # i代表一个字典
            tmp_time = i["dateId"]
            self.__tmp_dict[tmp_time] = abs(int(i["curedIncr"]))
        # 完成了对新增治愈人数获得的字典
        self.data = self.__tmp_dict

class Get_DeadIncr(Data):
    __tmp_dict: dict[str, int] = dict()
    def get_info(self):
        for i in self.data:
            # i代表一个字典
            tmp_time = i["dateId"]
            self.__tmp_dict[tmp_time] = abs(int(i["deadIncr"]))
        # 完成了对新增治愈人数获得的字典
        self.data = self.__tmp_dict


class Build_Bar:
    data = None
    __length = 20
    __keys = list()
    data_list = list()
    # 只显示前50天
    __x_list = list()
    __y_list = list()
    def loads_data(self,filename):
        # 每次进入函数需要将data_list初始化
        with open(filename,"r",encoding="UTF-8") as f:
            self.data = json.load(f)
            self.__keys = list(self.data.keys())
        #     问题在该函数部分
        index = 0
        while index < len(self.__keys):
            tmp = list()
            key = self.__keys[index]
            tmp.append(key)
            tmp.append(self.data[key])
            self.data_list.append(tmp)
            index += 1
        self.data_list.sort(key=lambda element : element[1],reverse=True)
        self.__get_axis()
        self.data_list = list()


    def __get_axis(self):
        for i in self.data_list:
            # 日期是key
            self.__x_list.append(i[0])
            self.__y_list.append(i[1])


    def build_bar(self,filename):
        __bar = Bar()

        __bar.add_xaxis(self.__x_list[0:self.__length+1])
        __bar.add_yaxis(f"全球疫情{filename}人数",self.__y_list[0:self.__length+1],label_opts=LabelOpts(
            position="right"
        ))
        __bar.reversal_axis()
        __bar.render(f"datapath/全球疫情{filename}人数.html")
        # 存在问题，死亡人数将治愈的人数一起加进去了

def get_real_data(data: Data,filepath: str,filename: str):
    data.change_type(filepath)
    data.get_info()
    # 无问题
    data.build_json(filename)

def build_bar(data: Build_Bar,filename: str,index):
    data.loads_data(filename)
    if index == 0:
        title = "新增治愈"
    else:
        title = "新增死亡"
    data.build_bar(title)

if __name__ == '__main__':
    bar = Build_Bar()
    # 检查文件夹的存在性
    file = "datapath"
    if not os.path.exists(file):
        os.makedirs(file)

    filepath = "database/world_total_data.json"
    filename_2 = f"{file}/deadIncr.json"
    filename_1 = f"{file}/curedIncr.json"
    filename_list = [filename_1,filename_2]
    cured = Get_CuredIncr()
    dead = Get_DeadIncr()
    # 创建一个储存对象的列表
    file_list = [cured,dead]
    count = 0
    while count < len(filename_list):
        get_real_data(file_list[count],filepath,filename_list[count])
        build_bar(bar,filename_list[count],count)
        count += 1
