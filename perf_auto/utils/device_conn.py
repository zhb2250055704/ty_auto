from airtest.core.api import *
import os
# 如果adb collection报错：Using or importing the ABCs from 'collections'.......，开启下面两行代码
# from collections.abc import Iterable
# print(isinstance('abc', Iterable))

'''
分为有线模式与无线模式

使用有线模式,连接上手机即可

使用无线模式,需保证与电脑wifi相同,且修改adb端口为5555

adb tcpip 5555
'''

# 有线模式连接当前手机
def youxian_connect():
    auto_setup(__file__)

# 无线模式连接
def wifi_connect():
    # 手机与电脑处于同一wifi，查看手机WIFI的IP
    ip = input('请输入手机的wifiIP,格式为:XXX:XXX:XXX:XXX')
    tcpip = ip + ':5555'
    device_1 = connect_device('android:///'+tcpip+'?cap_method=javacap&touch_method=adb')
    print("无线模式连接成功,IP为"+ip)

if __name__ == '__main__':
    wifi_connect()
