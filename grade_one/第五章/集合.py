from faker.proxy import Faker

faker = Faker()
a = set()
b = {1,2,faker.name(),3,4,5,6,6,"hello world",7,2,1,23,5,6,7,8,9,10}

print(f"集合a{a},集合b{b},集合的类型为{type(b)}")

# 集合的相关操作
my_set = {"Python","Java","C/C++","Html","JavaScript"}

my_set.add("Go")
print(my_set)
my_set.add("Python")
print(f"集合不能添加重复元素{my_set}")

# 移除元素
my_set.remove("Python")
print(my_set)

# 随机取出一个元素
data = my_set.pop()
print(f"集合取出的元素为{data},取出后集合为{my_set}")

# 清空集合
my_set.clear()
print(f"集合被清空{my_set}")

# 集合的差集
my_set = {"Python","Java","C/C++","Html","JavaScript"}
my_set_1 = {"Python","Java","C/C++"}
print(f"集合1{my_set}与集合2{my_set_1}的差集为{my_set.difference(my_set_1)}")

# 消除集合的差集
my_set.difference_update(my_set_1)
print(f"消除集合1和集合2的差集，得到的集合1的结果为{my_set},集合2不发生改变{my_set}")

# 集合的合并
set_1 = {"Python","Java","C/C++"}
my_set.add("Go")
set_2 = my_set
set_3 = set_1.union(set_2)
print(f"集合1{set_1}和集合2{set_2}合并的结果集合3为{set_3}")

# 统计集合的元素数
num = len(set_3)
print(f"集合3的长度为{num}")

# 集合的遍历
print(f"集合3为:{set_3}")
for i in set_3:
    print(i)

# 练习
'''
    my_list = ['黑马程序员','传智播客','黑马程序员','传智播客','Itcast','Itcast','best']
    定义一个空集合
    for循环遍历列表
    将遍历得到的元素添加到集合
    去重后的集合对象打印输出
'''
my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'Itcast', 'Itcast', 'best']
my_set = set()
for i in my_list:
    my_set.add(i)

print(my_set)
