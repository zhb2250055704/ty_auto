from airtest.core.api import *

def shangchengtiaozhuan(poco):
    print('------执行【商城界面跳转】用例，共跳转20次-------')
    start_time = time.time()
    i = 1
    for i in range(1,21):
        print(f'-------第{i}次跳转开始执行------')
        sleep(0.25)
        poco("ui_currencyBar_1").child("img_con").click()
        sleep(0.25)
        poco("ui_btn_back").click()
        sleep(0.25)
        print(f'-------第{i}次跳转执行结束------')
    end_time = time.time()
    print(f'-------完成【商城界面跳转】用例执行，共用时{end_time-start_time}秒----------')