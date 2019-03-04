file = open("file_/gitlab_access.log", "r")
access_log = file.read()
#print(access_log)
result={}
lines = access_log.splitlines()
for line in lines:
    ip = line.split(" ", 1)[0]  # print str.split(' ', 1 ); # 以空格为分隔符，分隔成两个
    if ip[0].isdigit():
        if ip in result:
            result[ip] += 1
        else:
            result[ip] = 1
#print(result)
list1=sorted(result.items(), key=lambda item: item[1], reverse=True)
print(list1)
print("访问次数最多的ip地址为:{},访问次数为:{}".format(list1[0][0], list1[0][1]))
file.close()


#lambda 匿名函数
# def say_hello():
#     pass
# print(type(say_hello()))
# print(type(lambda x:x))
#
# lambda 参数：表达式 #作用返回表达式结果
# lambda 匿名函数：没有名称的函数
# hello = lambda x,y:x+y
# 调用lambda 需要用变量调出
#
# def hello(x, y):
#     return x+y