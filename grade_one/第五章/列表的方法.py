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
print(arr)
arr.remove('one')
print(arr)
# 列表的清除