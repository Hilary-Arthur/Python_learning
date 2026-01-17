class Student:
    name = None
    age = None
    address = None
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

i = 0
stu_list = list()
while i < 10:
    print(f"当前录入第{i+1}位学生的信息，总共需要录入10位学生信息")
    name = input("请输入学生姓名")
    age = int(input("请输入学生年龄"))
    address = input("请输入学生地址")
    stu = Student(name,age,address)
    stu_list.append(stu)
    print(f"学生{i+1}信息录入完成,信息为:[学生姓名:{stu.name},年龄:{stu.age},地址:{address}]")
    i += 1