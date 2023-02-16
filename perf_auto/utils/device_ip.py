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
    return None

def get_ip ():
    result1 = exec_cmd('adb shell ip addr show wlan0')
    ip = get_device_ip(result1)
    print(f'当前连接的设备ID为：{ip}')
    return ip

if __name__ == '__main__':
    ip = get_ip()
    print(ip)