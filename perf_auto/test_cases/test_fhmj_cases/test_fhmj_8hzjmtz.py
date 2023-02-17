from airtest.core.api import *

def bahongzhongtiaozhuan(poco):
    print('------执行【八红中界面跳转】用例，共跳转20次-------')
    start_time = time.time()
    for i in range(1, 21):
        print(f'-------第{i}次跳转开始执行------')
        #         点击疯狂十三幺
        if i == 1:
            if poco(name="HallBtnxueliu_fk13y").exists():
                poco(name="HallBtnxueliu_fk13y").click()
            if poco(text='疯狂8红中').exists():
                poco(text='疯狂8红中').click()
        if poco(name='ui_text_quick_start').exists():
            poco(name='ui_text_quick_start').click()
        #         如果存在新手引导
        if poco(name='ui_btn_skip').exists():
            poco(name='ui_btn_skip').click()
#             金币太多判断
        if poco(text='您的金币数量太多啦，建议进入更高场次！').exists():
            poco(name='ui_center_text').click()
        #          判断是否在对局
        if poco(name="ui_btn_2").exists():
            poco(name="ui_btn_2").click()
#         对局中结束，开启再来一次
        poco(name='ui_table_out').wait_for_appearance()
        poco(name='ui_table_out').click()
        poco(name="ui_btn_1").click()
#         雀神出现
        if poco(name='btn_go').exists():
            poco(name='btn_close').click()
        print(f'-------第{i}次跳转执行结束------')
    end_time = time.time()
    print(f'------【八红中跳转界面】执行结束，共用时{end_time-start_time}秒-------')
