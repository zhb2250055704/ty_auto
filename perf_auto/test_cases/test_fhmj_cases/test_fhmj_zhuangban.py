from airtest.core.api import *


from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()


def zhuangban():
    print('-----装扮场景开始运行-----')
    poco("ui_hall_down_gongjulan_zhuangban").click()
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
    print('-----装扮场景运行结束-----')

if __name__ == '__main__':
    zhuangban()