# 捕获异常
try:
    r = open("python.txt","r",encoding="UTF-8")
    # 出现错误，被except接收，但是r没有被close
except :
    print("出现异常，文件不存在，采用写方式打开")
    w = open("python.txt","w",encoding="UTF-8")
    # 此处w已经被close了
finally:
    print("无论有没有异常我都会关闭文件的打开")
    r.close()
# 捕获指定异常,不能接受多个异常
try:
    print(name)
except NameError as e:
    print(f"name变量名称未定义:{e}")
finally:
    print("无论有没有异常我执行")
# 捕获多个异常
try:
    # print(name)
    1/0
except (NameError,ZeroDivisionError) as e:
    print(f"出现了{e}")
# 捕获所有异常
try:
    # 1/0
    name = ' '
    print(name)
except Exception as e:
    print(f"出现了异常:{e}")
else :
    print("当前语句未出现任何异常")