# Python的Iterator对象表示的是一个数据流，
# Iterator对象可以被next()函数调用并不断返回下一个数据，
# 直到没有数据时抛出StopIteration错误。
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

# 可迭代对象：Iterable
# 可以使用isinstance()判断一个对象是否是Iterable对象
from collections import Iterable
isinstance([], Iterable)
# 首先获得Iterator对象:
