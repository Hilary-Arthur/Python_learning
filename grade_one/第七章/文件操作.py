# 打开文件
# w = open('python.txt','w',encoding='UTF-8')
# r = open('python.txt','r',encoding='UTF-8')
# a = open('python.txt','a',encoding='UTF-8')

# read()方法
# content = r.read(5)
# r指针已经读取到第四个元素0,1,2,3
# readlines()方法，读取全部内容
# content_1 = r.readlines()
# print(f"读取长度为3的内容为{content},按行读取的列表为{content_1}，类型为{type(content_1)}")
# readline()方法：一次读取一行内容
# content_2 = r.readline()
# print(f"第一行{content_2}")

# for循环读取文件行
# for line in r:
#     print(f"该行数据为{line}")

# 文件的关闭，停掉文件的占用
# r.close()
# a.close()

# with open语法
# 练习
hello_times = 0
with open("python.txt","r") as f:
    content = f.readlines()
    for i in content:
        hello_times += i.count("hello")
print(content)
print(f"文件中hello出现的次数为{hello_times}")

def read_file():
    with open("python.txt","r") as r:
        content = r.readlines()
        print(content)

# 文件的写入
with open("python.txt","w") as w:
    w.write("hello world\n")
    w.flush()
    read_file()

# 文件的追加a
with open("python.txt","a") as a:
    a.write("hello Python\n")
    a.flush()
    read_file()