import random
from faker.proxy import Faker

faker = Faker()
arr = [1,2,3,4,'aaa',True]

# 查找某元素下标,index方法只能查找元素的位置
aim = arr.index('aaa')
print(aim)

# 列表修改，按照特定下标
arr[aim] = 'hello'
print(arr[aim])

# 列表插入元素
arr.insert(aim+1,"world")
print(arr)

# 列表追加元素
arr_1 = [[faker.name(),faker.name()]]
arr.append(faker.name())
print(arr)

arr.extend(arr_1)
print(arr)

# 列表的删除
del arr[aim]
print(arr)

pop_letter = arr.pop(aim)
print(arr)
print(pop_letter)

# 移除列表元素的第一个匹配项
index_1 = random.randint(0,len(arr))
index_2 = random.randint(0,len(arr))
arr.insert(index_1,'one')
print(arr)
arr.insert(index_2,'one')
arr_2 = list()
# arr_2 使用append是直接将元素追加在列表后面，当arr随之清空，arr_2表现出来的也是空
arr_2.extend(arr)
print(arr)
arr.remove('one')
print(arr)

# 列表的清除
arr.clear()
print(arr)

# 统计列表元素的数量
print(arr_2)
key = 'one'
count = arr_2.count(key)
print(f"列表中{key}的数量为{count}")

# 统计列表中全部元素数
print(len(arr_2))