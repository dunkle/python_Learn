#输入参数加*为可变参数，传入函数时也可以为可变参数
def mySum(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
        return sum

mlist = [3, 4, 5, 6]
print(mySum(*mlist))


#传入字典参数**
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
