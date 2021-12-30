'''列表推导式'''

'''列表推导式可以使用非常简洁的方式对列表或其他可迭代对象的元素
进行遍历、过滤或再次计算，快速生成满足特定需求的新列表'''
x = []
for i in range(30):
    x.append(i)
print(x)

y = [i for i in range(2)]
print(y)

freshfruit = ['banana ', ' loganberry ', ' passion fruit']
new_ff = [i.strip() for i in freshfruit]
print(new_ff)

a = [[1, 2, 3], [4, 5, 6], [7, 9]]
new_a = [j for i in a for j in i]
print(new_a)

import os

print(os.getcwd())
# /Users/guanpy/Desktop/guan1/python当前路径

print(list(filename for filename in os.listdir(os.getcwd())))
# ['a1.py', 'list3.py', '__init__.py', 'list2.py', 'list5.py', 'test_import.py', 'list1.py', 'list4.py', 'name属性.py', 'aa', 'neizhihanshu_filter.py']
# 当前路径下的文件及文件夹,不包含子文件夹中的内容

print(list(filename for filename in os.listdir() if filename.endswith('.py')))
['a1.py', 'list3.py', '__init__.py', 'list2.py', 'list5.py', 'test_import.py', 'list1.py', 'list4.py', 'name属性.py',
 'neizhihanshu_filter.py']
# endswith()测试字符串是否以指定的字符串结束
