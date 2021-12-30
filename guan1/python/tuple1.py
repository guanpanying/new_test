'''生成器对象'''

g = ((i + 2) ** 2 for i in range(10))
print(g)  # <generator object <genexpr> at 0x7fecd8053900>

print(tuple(g))  # (4, 9, 16, 25, 36, 49, 64, 81, 100, 121)

print(list(g))  # [] 生成器已遍历结束

g = ((i + 2) ** 2 for i in range(10))
print(g.__next__())
print(next(g))

for i in g:
    print(i, end=' ')

g1 = map(str, range(20))
print('4' in g1)
print('8' in g1)
print('4' in g1)
print('5' in g1)
