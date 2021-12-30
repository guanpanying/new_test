'''字典的添加修改和删除'''

a = {1: '1', 2: '2'}
print(a)

# 添加
a[3] = '3'
print(a)
# {1: '1', 2: '2', 3: '3'}

# 修改
a[1] = 'guan'
print(a)
# {1: 'guan', 2: '2', 3: '3'}

# 删除
print(a.pop(1))
print(a)
# guan
# {2: '2', 3: '3'}

print(a.popitem())
print(a)
# (3, '3')
# {2: '2'}
