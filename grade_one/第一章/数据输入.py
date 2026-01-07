name = input("please input your name:")
if name == "Tom" or name == "tom" :
    print("hey Tom")
else :
    print("you are not Tom")
print("name : %s" % type(name))

# 均会获得字符串，因此需要符号类型转换