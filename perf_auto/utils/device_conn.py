from airtest.core.api import *
import os
# 如果adb collection报错：Using or importing the ABCs from 'collections'.......，开启下面两行代码
# from collections.abc import Iterable
# print(isinstance('abc', Iterable))
import os
import re

'''
使用方法：使用get_ip()获得当前安卓手机的IP地址
'''

def exec_cmd(cmd):
    cmd = os.popen(cmd)
    cmd_result = cmd.read()
    cmd.close()
    return cmd_result

def get_device_ip(content):
    math_obj = re.search(r'inet\s(\d+\.\d+\.\d+\.\d+).*?wlan0', content)
    if math_obj and math_obj.group(1):
        return math_obj.group(1)

def huoqu_ip ():
    result1 = exec_cmd('adb shell ip addr show wlan0')
    ip = get_device_ip(result1)
    print(f'当前连接的设备ID为：{ip}')
    return ip

def get_ip():
    try:
        IP = huoqu_ip()
        with open(r'config/config_ip.txt','w+') as f:
            f.write(IP)
        os.system("adb tcpip 5555")
        return IP
    except Exception as e:
        print(f'请拔线重连后，再运行此模块,ADB报错为：{e}')
        print('执行重启ADB操作')
        os.system('adb kill-server')
        os.system('adb reconnect')
        print('尝试再次获取IP')
        IP = huoqu_ip()
        return IP

# 有线模式连接当前手机
def youxian_connect():
    auto_setup(__file__)

# 无线模式连接
def wifi_connect():
    with open(r'config/config_ip.txt', "r") as f:
        ip = f.read()
    # 手机与电脑处于同一wifi，查看手机WIFI的IP
    tcpip = ip + ':5555'
    device_1 = connect_device('android:///'+tcpip+'?cap_method=javacap&touch_method=adb')
    print("无线模式连接成功,IP为"+ip)

if __name__ == '__main__':
    wifi_connect()
