# 基础数据类型注解
import json
import random

var_1: int = 10
var_2: str = "chengdu"
var_3: bool = True
# 类对象类型注解
class Student:
    pass

stu: Student = Student()

def func():
    return False
# 基础容器注解
my_list : list = [1,2,3]
my_tuple : tuple = (1,2,3)
my_dict : dict = {"name":"Tom","age":18}

# 容器类型详细注解
my_list_1 : list[int] = [1,2,3]
# 虽然值的类型与注解不同，但是不会报错
my_tuple_1 : tuple[int,str,bool] = (1,"a",True)
# 在注释中进行类型注解
var_4 = random.randint(1,10)    # type: int
var_5 = json.loads('{"name":"Tom"}')    # type: dict[str,str]
var_6 = func() # type: bool