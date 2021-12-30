'''列表中使用运算符+，*，in '''

x = [1, 2, 3]
x = x + [4]
print(x)  # [1, 2, 3, 4]

print(x * 3)  # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

print(3 in x)  # True

'''关系运算符比较两个列表大小'''
print([1, 2, 4] > [1, 2, 3, 5])  # True 逐个比较列表中对应位置元素，直到某个元素能够比较出大小

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # True
print(id(x))  # True
print(id(y))  # 140362350923328
print(x is y)  # False

a = 1
b = 1
print(id(a))
print(id(b))
print(a == b)
print(a is b)
# 4441864896
# 4441864896
# True
# True
