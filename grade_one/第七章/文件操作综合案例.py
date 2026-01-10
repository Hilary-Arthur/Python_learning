fr = open("python.txt","r",encoding="UTF-8")
fw = open("python.txt.bak","w",encoding="UTF-8")

for i in fr:
    i = i.strip()
    if i.split(" ")[1] != "world":
        # 字符串不能内部改变，而是得到一个新的字符串
        i = i.replace(i.split(" ")[1],"world")
    fw.write(i)
    fw.write("\n")

print("文件备份写入完毕")
fr.close()
fw.close()