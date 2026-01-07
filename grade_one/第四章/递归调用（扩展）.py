def add_self(data,num):
    num += data
    data -= 1
    if data < 0:
        return num
    return add_self(data,num)



ori = 0
print(add_self(100,ori))