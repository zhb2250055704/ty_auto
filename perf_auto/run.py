from airtest.core.api import *
from utils import device_conn
from utils import perfdog
from test_cases import test_fhmj
# 前置工作
# 0. 设置ADB端口为5555 命令:adb tcpip 5555 ,IP为手机连接wifi的IP查看即可
# 1. 连接手机 有线模式使用方法 youxian_connect() 无线使用wifi_connect()
device_conn.wifi_connect()

# 2. 创建poco对象,不使用poco注销即可
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

# 执行逻辑部分
# 1. 具体执行逻辑,使用其他逻辑请先导包
# 2. 调用perfdog进行打点操作
test_fhmj.shangcheng()


# 后置操作部分
# 1. 停止pefdog并上传数据
# 2. 退出perfdog账号
# perfdog.tingzhi()
# perfdog.jieshu()
