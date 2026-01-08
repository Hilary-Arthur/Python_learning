import random

from faker import Faker
a = list()
b = []

print(a)
print(b)

faker = Faker()
name_list = [faker.name(),666,bool(1)]
print(name_list)
print(type(name_list))
# 下标索引取出元素
print(name_list[0])
for i in range(-1,-len(name_list)-1,-1):
    print(name_list[i])
print(type(name_list[0]))
# 列表嵌套，将字符串看做一个列表
for i in range(len(name_list)):
    if i == 0 :
        for j in name_list[i]:
            print(j)
    else :
        break

L = [[faker.name(),faker.name()],random.randint(1,100)]
print(L)
print(L[0][1])
print(len(L))