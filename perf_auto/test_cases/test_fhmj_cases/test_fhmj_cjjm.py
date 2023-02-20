from airtest.core.api import *

def chengjiujiemian(poco):
    print('--------成就界面测试用例开始执行--------')
#     点击进入成就界面
    print('------开始进入成就界面------')
    poco(name='ui_hall_down_gongjulan_chengjiu').click()
    if poco(name = 'chengjidacheng_bj').exists():
        poco(name='chengjidacheng_bj').click()
        print('成就标签未获取到，改用坐标定位点击')
    else:
        poco.click([0.459, 0.921])
        poco(name = 'chengjidacheng_bj').click()
        print('使用坐标定位，获取到成就标签，点击进入')
    print('--------进入成就界面完成---------')
#     静止1min
    print('开始静止1分钟')
    for i in range(1,61):
        print(f'倒计时{61-i}s')
        sleep(1)
    print('1分钟已静止完成')
    print('----------开始执行切换页签5次操作---------')
    for i in range(1,6):
        print(f'成就循环操作第{i}次开始')
        poco(text="日积月累").click()
        poco(text="决胜千里").click()
        poco(text="群英荟萃").click()
        poco(text="如火如荼").click()
        poco(text="如火如荼").swipe([0.0181, -0.2555])
        poco(text="麻将成就").click()
        poco(text="南征北战").click()
        poco(text="胜利在望").click()
        poco(text="胡天胡地").click()
        poco(text="国士无双").click()
        poco(text="杠上开花").click()
        poco(text="杠上开花").swipe([0.003, -0.2324])
        poco(text="雀神之路").click()
        poco(text="挑战成就").click()
        poco(text="知难而进").click()
        poco(text="一叶知秋").click()
        poco(text="生涯成就").click()
        print(f'成就循环操作第{i}次结束')
        print('----------结束执行切换页签5次操作---------')
    print('开始执行领取5次成就奖励')
    poco(text="日积月累").click()
    for i in range(1,6):
        print(f'领取第{i}次成就')
        poco.click([0.7595399, 0.4017317])
        poco(text='点击任意空白区域关闭').click()
    print('结束执行领取5次成就奖励')
    print('=======开始返回大厅============')
    poco(name = 'ui_close').click()
    poco(name = 'ui_button_back').click()
    print('========返回完成=======')
    print('============结束执行成就场景============')

if __name__ == '__main__':
    chengjiujiemian()