from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()


def bahongzhongtiaozhuan():
    print('------执行【八红中界面跳转】用例，共跳转20次-------')
    for i in range(1, 21):
        print(f'-------第{i}次跳转开始执行------')
        #         点击疯狂十三幺
        poco(name="HallBtnxueliu_fk13y").click()
        poco(name='ui_text_off').click()
        poco(name='ui_text_quick_start').click()
        #         如果存在新手引导
        if poco(name='ui_btn_skip').exists():
            poco(name='ui_btn_skip').click()
        #          判断是否在对局
        if i != 1:
            poco(name="ui_btn_2").click()
        else:
            time.sleep(10)
        #         在对局中退出
        poco(name='ui_table_out').wait(timeout=2).click()
        poco(name="ui_btn_1").click()

        print(f'-------第{i}次跳转执行结束------')
