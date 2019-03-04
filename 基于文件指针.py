#基于文件指针
file = open("gitlab_acess.log","r")
lines = file.readlines()
num = 1
while True:
    control = input(">>>")
    if control == "N":
        print("++++-第%s页开始+++")
        start = (num-1)*5
        end = num*5
        for line in lines[start:end]:
             print(line)
        print("++++-第%s页结束+++")
        num += 1
    elif control =="E":
        break
    elif control =="U":
        num -= 1
        print("++++-第%s页开始+++")