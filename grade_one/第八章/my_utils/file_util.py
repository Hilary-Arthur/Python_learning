def print_file_info(file_name):
    try :
        r = open(file_name, "r", encoding="UTF-8")
        index = r.readlines()
        for i in index:
            i= i.strip()
            print(i)
    except Exception as e:
        print(e)
    finally:
        if r:
            # 当文件没有内容的时候，关闭就会报错，因此在这里写一个if语句，判断文件指针是否为空
            print("文件关闭")
            r.close()

def append_to_file(file_name,data):
    a = open(file_name,"a",encoding="UTF-8")
    # 追加的位置是结束符，因此没有办法换行，所以先写入一个换行符
    a.write("\n")
    a.write(data)
    # close方法里自带flush
    a.close()
