from airtest.core.api import *

def duobao(poco):
    start_time = time.time()
    print('-----夺宝用例场景开始执行-----')
    if poco("ui_hall_down_gongjulan_draw").exists():
        poco("ui_hall_down_gongjulan_draw").click()
        print('夺宝标签成功获取')
    else:
        poco.click([0.459, 0.921])
        print('夺宝标签获取失败，改用坐标定位')
    poco(text="夺宝").wait_for_appearance()
    poco("ui_currencyBar_4").child("img_con").click()
    for i in range(1,5):
        poco("ui_btn_add1").click()
    poco("ui_btn_buy").click()
    poco("ui_bottom_text").click()
    print('-----完成抽奖币购买-----')
    if poco(name="Image (2)").exists():
        poco("btn_close").click()
    for i in range(1,6):
        poco("ui_btn_open_once").click()
        sleep(5)
        if poco("ui_btn_share").exists():
            poco("ui_btn_confirm").click()
            poco("ui_btn_confirm").click()
            print(f'-----完成第{i}次抽奖-----')
        else:
            poco("ui_btn_again").exists()
            poco("ui_btn_confirm").click()
            print(f'-----完成第{i}次抽奖-----')
    poco("ui_btn_return").click()
    end_time = time.time()
    print(f'-----夺宝场景运行结束，共用时{end_time-start_time}秒-----')

if __name__ == '__main__':
    duobao()