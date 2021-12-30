a = dict(name='1', guan='2')
print(a)

b = {1: '1', 2: '2'}
print(b)

c = dict(aa=1, bb=2)
print(c)

a1 = dict.fromkeys(['name', 'age', 'sex'])
print(a1)

'''获取元素'''
# print(a1['address'])  #KeyError: 'address'

print(a1.get('address'))  # None

print(a1.get('address', 'not exists'))  # not exists

'''
'''

print(len(a1))  # 3
print(max(a1))  # sex
print('-' * 30)

aDict = {'age': 39, 'score': [98, 99], 'name': 'Guan', 'sex': 'female'}
for i in aDict:
    print(i)
# age
# score
# name
# sex

for i in aDict.items():
    print(i)

# ('age', 39)
# ('score', [98, 99])
# ('name', 'Guan')
# ('sex', 'female')

for i in aDict.values():
    print(i)
#
# 39
# [98, 99]
# Guan
# female
