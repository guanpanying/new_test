import threading
import time


def a():
    print('a')
    time.sleep(5)
    print(time.asctime())


def b():
    print('b')
    time.sleep(3)
    print(time.asctime())


def c():
    print('c')
    time.sleep(6)
    print(time.asctime())


def test_thread():
    l1 = [threading.Thread(target=b), threading.Thread(target=c), threading.Thread(target=c)]
    [i.start() for i in l1]
    [i.join() for i in l1]
