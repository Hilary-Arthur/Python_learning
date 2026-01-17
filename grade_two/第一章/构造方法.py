

class Student:
    name = None
    age = None
    tel = None
    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
        print(f"Student类创建了一个对象")

stu = Student("dwx",20,"1999999999")
print(f"{stu.name}+{stu.age}+{stu.tel}")