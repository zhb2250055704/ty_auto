from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco

def huodong(poco):
    print('------活动场景用例开始执行------')
    start_time = time.time()
    poco(name='ui_hall_down_gongjulan_huodong').click()
    if poco(text='每日任务').exists():
        print('活动页面打开成功')
    else:
        poco.click([0.311, 0.924])
        print('使用坐标定位，活动页面打开，点击进入')
    for i in range(1,21):
        poco.swipe([0.25,0.8],[0.25,0.45],duration=0.2)
        poco.swipe([0.25,0.45],[0.25,0.8],duration=0.2)
        print(f'-----第{i}次拖拽结束-----')
    for i in range(1,4):
        poco(text='机甲风暴').click()
        poco(text="番型收集").click()
        poco(text="杠上杠新玩法").click()
        poco(text="疯狂十三幺").click()
        poco(text="每日任务").click()
        poco.swipe([0.25,0.8],[0.25,0.45],duration=0.2)
        poco(text="麻将无双杯").click()
        poco(text="川麻雀神杯").click()
        poco.swipe([0.25,0.45],[0.25,0.8],duration=0.2)
        print(f'-----第{i}轮循环结束')
    poco("ui_close").click()
    end_time = time.time()
    print(f'-----活动场景用例执行结束，共用时{end_time-start_time}秒-----')

if __name__ == '__main__':
    poco = UnityPoco()
    huodong(poco)