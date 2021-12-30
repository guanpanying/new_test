'''列表元素的访问'''

a_list3 = ['a', 'b', 'c', 'c', 'd', 'e']
print(a_list3[1])
print(a_list3[-1])

'''列表常用方法'''
a_list3.append(5)
print(a_list3)
# ['a', 'b', 'c', 'd', 'e', 5]

a_list3.extend([4, 3, 2])
print(a_list3)
# ['a', 'b', 'c', 'd', 'e', 5, 4, 3, 2]

a_list3.insert(0, 1)
print(a_list3)  # [1, 'a', 'b', 'c', 'd', 'e', 5, 4, 3, 2]

a_list3.remove('e')
print(a_list3)  # [1, 'a', 'b', 'c', 'd', 5, 4, 3, 2]

a_list3.pop()
print(a_list3.pop())  # 3
print(a_list3)  # [1, 'a', 'b', 'c', 'd', 5, 4]

print(a_list3.count('c'))
print(a_list3.index('c'))

a = [9, 4, 3, 7]
a.sort()
print(a)
print(a[0])

a1 = [5, 3, 4, 5, 6]
print(a1.reverse())
a1.reverse()
print(a1)

a1.sort(reverse=True)
print(a1)
