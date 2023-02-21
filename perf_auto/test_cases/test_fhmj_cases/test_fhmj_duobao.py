from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco


def duobao(poco):
    CHOUYICI = poco(name="ui_btn_open_once")
    QUEDING = poco(name='ui_btn_confirm')
    ZAILAIYICI = poco(name='ui_btn_again')
    XUANYAO = poco(name="ui_btn_share")
    start_time = time.time()
    print('-----夺宝用例场景开始执行-----')
    poco("ui_hall_down_gongjulan_draw").click()
    if poco(text="夺宝").exists():
        print('夺宝标签成功获取')
    else:
        poco.click([0.459, 0.921])
        print('夺宝标签获取失败，改用坐标定位')
    print('夺宝界面进入成功，开始静置60s')
    sleep(60)
    print('静置结束')
    poco(name="ui_currencyBar_4").click()
    poco(name='ui_Slider').click()
    poco(name="ui_btn_buy").click()
    poco.click([0.5,0.85])
    print('-----完成抽奖币购买-----')
    if poco(name="btn_close").exists():
        poco("btn_close").click()
    for i in range(1,6):
        CHOUYICI.click()
        QUEDING.wait_for_appearance()
        if ZAILAIYICI.exists():
            QUEDING.click()
            print(f'-----完成第{i}次抽奖-----')
        elif XUANYAO.exists():
            QUEDING.click()
            QUEDING.click()
            print(f'-----完成第{i}次抽奖-----')
    poco(name="ui_btn_return").click()
    end_time = time.time()
    print(f'-----夺宝场景运行结束，共用时{end_time-start_time}秒-----')

if __name__ == '__main__':
    poco = UnityPoco()
    duobao(poco)