PO封装

1、page包 存放封装每一个page
page包--app.py   app相关的操作，app启动，关闭，重启
page包--base.py 基本方法 初始化driver,封闭find方法，封闭log日志，滚动查找
log.conf
page包可以多个，按模块区分，比如登录模块，联系人模块
testcase包 存放测试用例


2、有三层：base层，PO层，用例层
+utils其他功能封装，改进原生框架的不足
+Data数据驱动

3、return self ，用于类的链式调用

4、app需不需要继承basepage

5、 faker
from faker import Faker
pip install faker

fake=faker('zh_CN')
fake.name()
fake.address()
fake.text()
fake.phone_number()

6、appium --session-override 

7、driver复用

8 日志



#############多设备复用
9、mac udid='emulator-5554' port='4723' pytest test_a.py
  window  set udid='emulator-5554'
           set port='4723'
            pytest test_a.py

10、用例中 
import sys
sys.path.append('../../..')

11 多设备执行，appiumserver 配置代码，port
 
12 遍历出设备自己执行