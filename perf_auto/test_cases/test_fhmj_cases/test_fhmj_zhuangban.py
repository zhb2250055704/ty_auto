from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco


def zhuangban(poco):
    print('-----装扮场景用例开始执行-----')
    start_time = time.time()
    poco("ui_hall_down_gongjulan_zhuangban").click()
    if poco(text = '套装').exists():
        print('装扮页面打开成功')
    else:
        poco.click([0.168, 0.919])
        print('装扮页面打开成功')
    print('-----开始静置60s-----')
    sleep(60)
    print('-----静置结束-----')
    for i in range(1, 3):
        poco(text = '套装').click()
        poco(text = '桌饰').click()
        poco(text = '特效').click()
        poco(text = '头像框').click()
        poco(text = '语音').click()
        poco(text = '表情').click()
        print(f'-----完成第{i}次页签切换')
    poco("ui_btn_back").click()
    end_time = time.time()
    print(f'-----装扮场景运行结束，共用时{end_time-start_time}秒-----')

if __name__ == '__main__':
    poco = UnityPoco()
    zhuangban(poco)