a_list = ['abc', '关', 'u11', '***']


def f(x):
    return x.isalnum()  # isalnum()字符串方法，测试是否为字母，汉字，数字，返回True


print(list(filter(f, a_list)))
print(list(filter(f, a_list)))

x = filter(f, a_list)
print(list(x))
print(list(x))
