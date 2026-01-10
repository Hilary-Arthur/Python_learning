import random
from pickle import TRUE, FALSE

from grade_one.第五章.集合 import my_list

customer = {
    "王力鸿":{
        "部门":"科技部",
        "工资":3000,
        "级别":1
    },
    "周杰轮":{
            "部门":"市场部",
            "工资":5000,
            "级别":2
    },
    "林俊节":{
            "部门":"市场部",
            "工资":7000,
            "级别":3
    },
    "张学油":{
            "部门":"科技部",
            "工资":4000,
            "级别":1
    },
    "刘德滑":{
            "部门":"市场部",
            "工资":6000,
            "级别":2
    },
}

max_data = max(customer)
min_data = min(customer)
print(f"最大元素为{max_data},最小元素为{min_data}")

change_list = list(customer)
print(change_list)
change_tuple = tuple(customer)
print(change_tuple)
change_str = str(customer)
print(change_str)
change_set = set(customer)
print(change_set)

my_list = list()
for i in range(10):
    my_list.append(random.randint(0,i*i))

# reverse为反向排序，翻转操作
print(f"{my_list}排序后的结果是:{sorted(my_list, reverse = True)}")
print(f"{customer}排序后的结果是:\n{sorted(customer)}")
