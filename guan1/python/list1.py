'''列表的创建与删除'''

a_list1 = []
a_list2 = list()
a_list3 = ['a', 'b', 'c', 'd', 'e']

print(a_list1, a_list2, a_list3)
# [] [] ['a', 'b', 'c', 'd', 'e']

del a_list2, a_list1
# 删除列表
print(a_list2, a_list3)
# NameError: name 'a_list2' is not defined


# 可使用list()将元组，range对象,字符串，字典，集合等可迭代对象转换为列表
print(list((3, 5, 7, 9)))  # 元组转为列表

print(list(range(1, 10, 2)))

print(list('hello world'))
# ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

print(list({'a': 1, 'b': 2}))
# ['a', 'b']

print(list({'a': 1, 'b': 2}.keys()))
['a', 'b']

print(list({'a': 1, 'b': 2}.values()))
[1, 2]

print(list({'a': 1, 'b': 2}.items()))
# [('a', 1), ('b', 2)]
