class Student:
    name = None
    age = None
    # 定义学生年级
    __grade = None

    # def __init__(self,name,age,grade):
    #     self.name = name
    #     self.age = age
    #     self.__grade = grade

    def basic_info(self):
        self.__get_student_grade()
        # 在类对象中使用私有成员方法
        print(f"当前学生信息:姓名{self.name},年龄{self.age},年级{self.__grade}")

    def __get_student_grade(self):
        self.__grade = self.age - 6
        # print(f"{self.name}的年级为{self.__grade}")
        # return self.__grade

stu = Student()
# 私有方法无法被类对象使用
# stu.__get_student_grade()(错误)
# 私有成员在外部无效
stu.name = "Tom"
stu.age = 20
stu.__grade = 9
# 若有效则打印9，若无效则打印14
stu.basic_info()
