'''
# 打点方法：进行一次perfdog打点
# 使用前，请先导包，并运行perfdog连接
# 路径不能有中文

使用说明：
1. 打开perfdog，修改路径，perfdog_exe perfdog_r
方法：open_exe()
2. 操控perfdog进行打点
方法：dadian()
3. 停止perdog测试
方法：tingzhi()
4. 退出账号结束perfdog
方法：jieshu()
5. 关闭perdog进程，强制退出
方法：close_exe()

'''
import subprocess
import time
import lackey
import os
from lackey import Button, Match


perdog_exe = r'C:\Users\lh\Desktop\PerfDog(v8.0.221052)\PerfDog.exe'
perdog_r = r'C:\Users\lh\Desktop\PerfDog(v8.0.221052)'

def open_exe():
    subprocess.Popen(perdog_exe,cwd=perdog_r)
    print('启动成功')

def dadian():
    lackey.click('utils/photo/dadian.png')
    print('打点成功')

def kaishi():
    lackey.click('utils/photo/kaishi.png')
    print('开始测试')
def jieshu():
    lackey.click('utils/photo/jieshu.png')
    print('性能测试结束,账号已退出')

def tingzhi():
    lackey.click('utils/photo/tingzhi.png')
    # 等待停止上传
    time.sleep(30)
    lackey.click('utils/photo/shangchuan.png')
    # 等待数据上传
    time.sleep(30)
    print('性能测试已完成，停止测试')

def close_exe():
    subprocess.Popen("taskkill /IM " + "PerfDog.exe" + " -F")
    print("perodog, 程序已关闭")



if __name__ == '__main__':
    print('==========perdog 测试开始==========')
    # open_exe()
    # dadian()
    # jieshu()
    # close_exe()
    # kaishi()
    screen = lackey.Screen()
    click_png = lackey.Pattern('photo/dadian.png')
    screen.click(click_png)
    print('==========perdog 测试结束==========')
