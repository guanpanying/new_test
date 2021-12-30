a = {1, 2}
a1 = set(range(5))
print(a)
print(a1)
# {1, 2}
# {0, 1, 2, 3, 4}

del a
# print(a)
# NameError: name 'a' is not defined


'''增加'''
a1.add('guan')
print(a1)
# {0, 1, 2, 3, 4, 'guan'}

a1.update({'g', 'p', 'y'})
print(a1)
# {0, 1, 2, 3, 4, 'guan', 'p', 'g', 'y'}

'''删除'''
print(a1.pop())
print(a1)
# 0
# {1, 2, 3, 4, 'g', 'guan', 'p', 'y'}

a1.remove('guan')  # 没有会抛异常
print(a1)
# {1, 2, 3, 4, 'y', 'p', 'g'}

a1.discard('g')  # 不抛异常
print(a1)
# {1, 2, 3, 4, 'y', 'p'}
