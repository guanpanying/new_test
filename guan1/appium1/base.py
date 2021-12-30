import os
import socket
import subprocess
import threading
import time

from appium import webdriver


class Base:
    def __init__(self):
        self.ue_a = ('emulator-5554', 4723)
        self.ue_b = ('emulator-5556', 4725)
        self.__start_appium_server()
        # self.connect_devices()

        # devices_list=[threading.Thread(target=self.connect_devices,args=(ue_a,)),
        #          threading.Thread(target=self.connect_devices,args=(ue_b,))]
        #
        # [con_device.start() for con_device in devices_list]
        # [con_device.join() for con_device in devices_list]

    def connect_devices(self, client, port, user):

        self.desired_caps = {
            'platformName': 'android',
            'udid': client,
            'deviceName': client,
            'noReset': True,
            'appPackage': 'com.android.chrome',
            'appActivity': 'com.google.android.apps.chrome.Main'

        }
        user = webdriver.Remote('http://127.0.0.1:' + str(port) + '/wd/hub', self.desired_caps)

    def __start_appium_server(self):
        b = os.popen('adb devices').read()
        # print(b.count('device'))
        device_num = b.count('device') - 1
        for i in range(device_num):
            self.port = 4723 + 2 * i
            self.bootstrap_port = 4723 + 2 * i + 1
            if self._check_port(self.port):
                time.sleep(1.5)

                subprocess.Popen(f'appium -a 127.0.0.1 -p {self.port} -bp {self.bootstrap_port}',
                                 shell=True, stdout=open('./appium_log/' + str(self.port) + '.log', 'a'),
                                 stderr=subprocess.STDOUT)
            else:
                self._release_port(self.port)
                time.sleep(1.5)
                subprocess.Popen(f'appium -a 127.0.0.1 -p {self.port} -bp {self.bootstrap_port}',
                                 shell=True, stdout=open('./appium_log/' + str(self.port) + '.log', 'a'),
                                 stderr=subprocess.STDOUT)

    def _check_port(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '127.0.0.1'

        try:
            s.connect((host, port))
            s.shutdown(2)  # 表示将来禁止读和写
        except OSError as msg:
            print('port %s is available!' % port)
            print(msg)
            return True
        else:
            print('port %s already be in use!' % port)
            return False

    def _release_port(self, port):
        cmd_find = 'lsof -i:%s' % port
        result = os.popen(cmd_find).read()
        print(result)

        if str(port) and 'LISTEN' in result:
            i = result.index('guanpy')
            pid = result[i - 6:i - 1]
            print('pid', pid)

            cmd_kill = 'kill %s' % pid
            print(cmd_kill)
            os.popen(cmd_kill)
        else:
            print('port %s is available' % port)
