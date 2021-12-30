'''内置函数'''
import random

x = list(range(11))
random.shuffle(x)  # 打乱列表中元素顺序
print(x)

print(all(x))  # False,0是False
print(all([1, 2, 3, 4, 5]))  # True

print(max(x), min(x), len(x), sum(x))
# 10 0 11 55

print(zip(x, [1] * 15), type(zip(x, [1] * 15)))
print(list(zip(x)))
# [(2,), (1,), (9,), (10,), (3,), (5,), (4,), (8,), (0,), (7,), (6,)]
print(tuple(zip(x)))
# ((2,), (1,), (9,), (10,), (3,), (5,), (4,), (8,), (0,), (7,), (6,))

print(set(zip(x)))
# {(6,), (2,), (5,), (8,), (4,), (1,), (7,), (10,), (0,), (3,), (9,)}

print(list(enumerate('abcd')))
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
