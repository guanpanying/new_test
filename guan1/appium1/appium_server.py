import subprocess

# stdout: 日志输出
from time import ctime


def appium_start(host, port):
    '''启动appium server'''
    bootstrap_port = str(port + 1)
    cmd = 'appium -a ' + host + ' -p ' + str(-port) + ' -bp ' + str(bootstrap_port)
    subprocess.Popen(cmd, shell=True, stdout=open('./appium_log/' + str(port) + '.log', 'a'), stderr=subprocess.STDOUT)


'''多个
appium服务启动'''
if __name__ == '__main__':
    host = '127.0.0.1'
    for i in range(2):
        port = 4723 + 2 * i
        appium_start(host, port)
