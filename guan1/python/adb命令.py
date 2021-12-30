import os

# os.system('adb devices')

f = os.popen('adb devices')
# print(f.read())
print('-' * 30)
# print(type(f))
a = f.readlines()
print(a)
for i in a:
    print(i)
