import os

b = os.popen('adb devices').read()
print(b, type(b))
# print(list(b))
'''List of devices attached
emulator-5554	device
emulator-5556	device

<class 'str'>

['L', 'i', 's', 't', ' ', 'o', 'f', ' ', 'd', 'e', 'v', 'i', 'c', 'e', 's', ' ', 'a', 't', 't', 'a', 'c', 'h', 'e', 'd', '\n', 'e', 'm', 'u', 'l', 'a', 't', 'o', 'r', '-', '5', '5', '5', '4', '\t', 'd', 'e', 'v', 'i', 'c', 
'e', '\n', 'e', 'm', 'u', 'l', 'a', 't', 'o', 'r', '-', '5', '5', '5', '6', '\t', 'd', 'e', 'v', 'i', 'c', 'e', '\n', '\n']'''

b1 = os.system('adb devices')
print(b1, type(b1))
'''List of devices attached
emulator-5554	device
emulator-5556	device

0 <class 'int'>'''

# res=os.popen('netstat -an |grep 4723').read()
# print(res)

# import subprocess
# for i in range(2):
#     port=4723+2*i
#     sport=port+1
#     subprocess.Popen(f'appium -a 127.0.0.1 -p {port} -bp {sport}',
#                                  shell=True, stdout=open('./appium_log/' + str(port) + '.log', 'a'),
#                                  stderr=subprocess.STDOUT)
#
# import yaml
#
# aa=yaml.safe_load()

import allure
