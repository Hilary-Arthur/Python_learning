# 更新元素，新增元素
my_dict = {"d":111,"a":222,"c":333,"b":444}
print("新增元素:")
my_dict["e"] = 777

print(my_dict)
print("更新元素:")
my_dict["d"] = 666

print(my_dict)
# 删除元素
value = my_dict.pop("d")
print(f"移除d元素{value},剩余字典{my_dict}")
# 清空元素
my_dict.clear()
print(f"字典被清空{my_dict}")
# 获取全部的key
my_dict_1 = {"d":111,"a":222,"c":333,"b":444}
keys = my_dict_1.keys()
print(keys)

# 遍历字典
# 通过获取的key来遍历
for i in keys:
    print(f"key值{i}对应的value值为{my_dict_1[i]}")

# 对字典直接进行for循环，每一次循环都直接得到key
for i in my_dict_1:
    print(f"{i},{my_dict_1[i]}")

# 统计元素数量
num = len(my_dict_1)
print(num)

# 练习
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
    }
}

print("全体员工当前信息如下:")
for i in customer:
    print(i,customer[i])

print("全体员工级别为1的员工完成升职加薪操作，操作后:")
for i in customer:
    if customer[i]["级别"] == 1:
        customer[i]["级别"] += 1
        customer[i]["工资"] += 1000
    print(i,customer[i])
