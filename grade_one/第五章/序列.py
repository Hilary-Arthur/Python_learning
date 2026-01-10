from faker.proxy import Faker

faker = Faker()
a = [1,2,3,4,5,6,7,faker.name(),"hello world"]

# 切片操作
b = a[2:10:3]
print(b)
c = (faker.name(),faker.name(),1,2,3,4,4,5,6,6,7,7,8,8,'a','b','c')
print(c[:])
d = 'abcdefghijklmn'
print(d[::-1])
print(d[3:1:-1])

# 练习
origin = "月薪过万,员序程马黑,nohtyP学"

index = origin.index(',')
index_1 = index + 5

result = origin[index_1:index:-1]
print(result)

aim = origin.split(",")
print(aim)
result_1 = aim[1][::-1]
print(result)