class Student:
    name = None
    age = None

    def test_1(self):
        print(f"test_1:{self.name},{self.age}")
    def test_2(self,msg):
        print(f"test_2:{msg}")
stu = Student()
stu.name = "dwx"
stu.age = 20
stu.test_1()
stu.test_2("hello world")