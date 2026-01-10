my_str = 'hello world'

# 下标索引
for i in range(len(my_str)):
    print(my_str[i])
print()
for i in range(-1,-len(my_str),-1):
    print(my_str[i])

# 字符串无法修改，只能怪得到一个新的字符串

# index方法
index = my_str.index('wor')
print(index)

# replace方法
new_str = my_str.replace("world","Python")
print(new_str)
print(my_str)

# split分隔字符串
result = my_str.split(" ")
print(result)

# 字符串的规整操作
my_str = '       hello world      '
print("字符串的规整操作:")
print(my_str.strip())

# 去除某个字符串
# 传入的字符串中，会将所有的字符串按照单个字符处理
my_str = 'oooooolllllhello worldlllllooooo'
print(f"字符串{my_str}被规整后得到：{my_str.strip("lo")}")

# 统计字符串count
count = my_str.count('l')
print(count)

# 统计字符串长度len()
length = len(my_str)
print(length)