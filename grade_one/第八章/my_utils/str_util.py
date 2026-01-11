def str_reverse(s):
    # 接收传入字符串，并且反转返回
    return s[::-1]

def substr(s,x,y):
    # 对字符串按照下表x和y，对字符串进行切片
    return s[x:y]

if __name__ == '__main__':
    str_reverse("Python")
    substr("Python",2,4)