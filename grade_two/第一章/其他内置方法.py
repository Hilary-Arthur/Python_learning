class Student:
    name = None
    age = None
    tel = None
    address = None
    def __init__(self,name,age,tel,address):
        self.name = name
        self.age = age
        self.address = address
        self.tel = tel
    # __str__魔术方法
    def __str__(self):
        return f"Student类对象，name={self.name},age={self.age},address={self.address},tel={self.tel}"
    # __lt__小于符号比较方法
    def __lt__(self, other):
        return self.age < other.age
    # __le__小于等于符号的比较方法
    def __le__(self, other):
        return self.age <= other.age
    # __eq__符号比较
    def __eq__(self, other):
        return self.age == other.age

student = Student("周杰伦",45,"111111111","台湾省")
print(student)
# print(str(student))
# __lt__小于符号的魔术方法
student_1 = Student("dwx",20,"111111","四川")
print(student_1 < student)
print(student_1 > student)
# __le__
student_2 = Student("dwx",20,"111111","四川")
print(student_2 >= student_1)
print(student_2 < student_1)
# __eq__
print(student_1 == student_1)
print(student == student_1)
