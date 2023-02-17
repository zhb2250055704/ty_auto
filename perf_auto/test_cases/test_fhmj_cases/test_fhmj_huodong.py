from airtest.core.api import *

#活动
def huodong(poco):
    print('------活动场景用例开始执行------')
    start_time = time.time()
    poco(name='ui_hall_down_gongjulan_huodong').click()
    if poco(text='每日任务').exists():
        print('活动页面打开成功')
    else:
        poco.click([0.318259031, 0.924202144])
        print('使用坐标定位，活动页面打开，点击进入')
    for i in range(1,21):
        poco(text='每日任务').swipe([0, -0.2])
        poco(text='每日任务').swipe([0, 0.2])
        print(f'-----第{i}次拖拽结束-----')
        # poco(text='每日任务').drag_to(poco(text="杠上杠新玩法"))
        # poco(text = '杠上杠新玩法').drag_to(poco(text="每日任务"))
#         swipe(Template(r"../perf_auto/images/fhmj_img/tuodong1.png", record_pos=(-0.322, 0.012), resolution=(2400, 1080)), vector=[0.0062, -0.358])
#         swipe(Template(r"../perf_auto/images/fhmj_img/tuodong2.png", record_pos=(-0.316, 0.015), resolution=(2400, 1080)), vector=[0.0004, 0.329])
    for i in range(1,4):
        poco(text='机甲风暴').click()
        poco(text="番型收集").click()
        poco(text="杠上杠新玩法").click()
        poco(text="疯狂十三幺").click()
        poco(text="每日任务").click()
        poco(text='每日任务').swipe([0, -0.2])
        poco(text="麻将无双杯").click()
        # poco(text = '麻将无双杯').drag_to(poco(text="番型收集"))
#         swipe(Template(r"../perf_auto/images/fhmj_img/tuodong3.png", record_pos=(-0.317, 0.0), resolution=(2400, 1080)), vector=[-0.0058, -0.3408])
        poco(text="川麻雀神杯").click()
        # poco(text="麻将话费").click()
        poco(text='每日任务').swipe([0, 0.2])
        # poco(text = '每日任务').drag_to(poco(text="麻将无双杯"))
        print(f'-----第{i}轮循环结束')
#         swipe(Template(r"../perf_auto/images/fhmj_img/tuodong2.png", record_pos=(-0.262, 0.012), resolution=(2400, 1080)), vector=[0.0084, 0.2987])
    poco("ui_close").click()
    end_time = time.time()
    print(f'-----活动场景用例执行结束，共用时{end_time-start_time}秒-----')

if __name__ == '__main__':
    huodong()