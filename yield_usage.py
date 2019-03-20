# 简单输出斐波那契數列前 N 个数
def fab(max):
    n, a, b = 0, 0, 1
    while n<max:
        print(b)
        a, b = b, a+b
        n = n+1
# fab(5)

# 直接在 fab 函数中用 print 打印数字会导致该函数可复用性较差，
# 因为 fab 函数返回 None，其他函数无法获得该函数生成的数列。
# 要提高 fab 函数的可复用性，最好不要直接打印出数列，而是返回一个 List

def fab1(max):
    n, a, b = 0, 0, 1
    L = []
    while n< max:
        L.append(b)
        a, b = b, a+b
        n = n+1
    return L

# for n in fab1(5):
#     print(n)

# 该函数在运行中占用的内存会随着参数 max 的增大而增大，
# 如果要控制内存占用，最好不要用 List
# 来保存中间结果，而是通过 iterable 对象来迭代

class fab2(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1
    def __iter__(self):
        return self
    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b =self.b, self.a+self.b
            return r
        raise StopIteration

# for n in fab2(5):
#     print(n)
# 使用 class 改写的这个版本，代码远远没有第一版的 fab 函数来得简洁。
# 如果我们想要保持第一版 fab 函数的简洁性，
# 同时又要获得 iterable 的效果，yield 就派上用场了：

def fab3(max):
    n, a, b =0, 0, 1
    while n<max:
        yield b
        #print(b)
        a,b =b, a+b
        n = n+1

for n in fab3(5):
    print(n)