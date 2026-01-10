# 位置参数
def person_info(name,age,gender):
    print(f"您的名字是{name},年龄为{age},性别为{gender}")

person_info('Tom',18,'男')

# 关键字参数
person_info(name='Tom',age=18,gender='男')
person_info(age=19,name="Anny",gender='woman')

# 关键字参数和位置参数结合
person_info("Hilary",age=20,gender="女")

# 缺省参数
def person_info_1(name,age,gender="男"):
    print(f"{name}的年龄为{age},他是{gender}")

person_info_1("Tom",12)
person_info_1("Anny",18,"女")

# 不定长传参
# 位置传递
def person_info_2(*args):
    print(f"args的类型为{type(args)}")
    print(args)

person_info_2("Tom",18,"woman")
# 关键字传递
def person_info_3(**kwargs):
    print(f"args的类型为{type(kwargs)}")
    print(kwargs)

person_info_3(name="Tom",age=18,gender="男",id=100)