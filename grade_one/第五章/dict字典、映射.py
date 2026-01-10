# 定义字典

my_dict = {"dwx":100,"Hilary":250,"Arthur":'genius'}
my_dict_2 = {}
my_dict_3 = dict()
print(f"字典1{my_dict},字典2{my_dict_2},字典3{my_dict_3}")

# 基于key获取value,使用[]
score = my_dict["dwx"]
print(f"dwx的value为{score}")

# 字典的嵌套
# result_1 = {"语文":100,"数学":100,"英语":99}
# result_2 = {"语文":100,"数学":100,"英语":99}
# result_3 = {"语文":100,"数学":100,"英语":99}
# my_dict_4 = {"dwx":result_2,"Hilary":result_3,"Arthur":result_1}

my_dict_4 = {
    "dwx":{
        "语文":100,
        "数学":100,
        "英语":99
    },
    "Hilary":{
        "语文":100,
        "数学":100,
        "英语":99
    },
    "Arthur":{
        "语文":100,
        "数学":100,
        "英语":99
    },
}

print(my_dict_4)
score_1 = my_dict_4["Hilary"]["语文"]
print(score_1)