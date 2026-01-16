# 设计类
class Student:
    name = None
    gender = None
    nation = None
    native_place = None
    age = None

# 创建对象
stu_1 = Student()
stu_1.name = "dwx"
stu_1.age = 20
stu_1.gender = "女"
stu_1.nation = "中国"
stu_1.native_place = "四川省"
# 获取对象中记录的信息
print(stu_1.name)
