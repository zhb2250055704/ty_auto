import os
from utils import device_conn
from test_cases.test_fhmj_cases import test_fhmj_xsyd
from poco.drivers.unity3d import UnityPoco
from airtest.core.api import *
from utils import fhmj_gm
import logging
logging.getLogger("airtest").setLevel(logging.ERROR)

'''
初始化模块说明：
1、连接手机，开启无线调试模式
1、请在插线模式，安装好（富豪麻将待测包体，切服工具）的情况下运行下运行此程序：
    1. 自动获取当前连接手机的IP地址，并进行保存
    2. 自动设置adb 端口为5555 
    3. 自动设置切服工具，启动进入游戏，完成登录新手引导等操作
PS: 若出现ADB保存，请把线拔了，再插上，运行此模块即可
'''

# 获取手机的IP，将wifi与电脑同一局域网下，使用有线模式连接
IP = device_conn.get_ip()
device_conn.wifi_connect()

# 图片对象封装
fuwiq01 = "images/fhmj_img/fuwuqi01.png"
debug02 = "images/fhmj_img/debug02.png"
gengxin03 = "images/fhmj_img/guanbi03.png"
denglutongyi = "images/fhmj_img/tongyi.png"
gouxuanxieyi = "images/fhmj_img/xieyi.png"
youkedenglu = "images/fhmj_img/youke.png"
# 富豪麻将APP包名：'com.maj3D.qmmj'
FHMJ_PACKAGE = 'com.maj3D.qmmj'
# 切服工具APP包名："com.example.com.example.changeurlnew"
QFGJ_PACKAGE = "com.example.com.example.changeurlnew"

# 唤醒设备
wake()
# 清除富豪麻将APP数据
clear_app(FHMJ_PACKAGE)
print(f'清除APP：{FHMJ_PACKAGE}成功')
start_app(QFGJ_PACKAGE)
print('启动切服工具成功')
touch(Template(fuwiq01))
print('1.切换仿真服务器成功')
sleep(1)
touch(Template(debug02))
print('2.切换DEBUG模式成功')
sleep(1)
touch(Template(gengxin03))
print('3.关闭APP更新成功')
stop_app(QFGJ_PACKAGE)
print('关闭切服工具')
# 前置登录操作
start_app(FHMJ_PACKAGE)
print(f'启动APP：{FHMJ_PACKAGE}成功')



wait(Template(denglutongyi), timeout=10)
touch(Template(denglutongyi))
touch(Template(gouxuanxieyi))
touch(Template(youkedenglu))
sleep(1)
poco = UnityPoco()
test_fhmj_xsyd.xsyd(poco)
id = fhmj_gm.huoquID(poco)
