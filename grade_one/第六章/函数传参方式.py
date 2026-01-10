# 位置参数
def person_info(name,age,gender):
    print(f"您的名字是{name},年龄为{age},性别为{gender}")

person_info('Tom',18,'男')

# 关键字参数
person_info(name='Tom',age=18,gender='男')