from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

def fk8hz():
    print('====开始执行疯狂⑧红中用例======')
    start_time = time.time()
    poco("HallBtnxueliu_hz_bxp").click()
    poco("twolevel_effpref_04").wait_for_appearance()
    poco(text = '疯狂8红中').click()
    poco(name = "ui_text_quick_start").click()
    #         如果存在新手引导
    if poco(name='ui_btn_skip').exists():
        poco(name='ui_btn_skip').click()
        print(f'关闭规则介绍')
    # 金币太多判断
    if poco(text='您的金币数量太多啦，建议进入更高场次！').exists():
        poco(name='ui_center_text').click()
    # 对局循环
    for i in range(1,3):
        poco(name='table_people_1').wait_for_appearance()
        if poco(name = "ui_img_menu_flod").exists():
            poco(name = "ui_img_menu_flod").click()
            poco(name="ui_table_zidonghupai_text").click()
            print(f'托管成功')
        else:
            poco(name = "ui_img_menu_unflod").click()
            poco(name="ui_table_zidonghupai_text").click()
            print(f'托管成功')
        # 发表情
        for x in range(1,6):
            poco(name='table_people_1').click()
            poco.click([0.5778258, 0.5478659])
            print(f'第{i}轮对局，第{x}次发金币表情成功')
            sleep(1)
        if i == 1:
            poco("ui_button_again").wait_for_appearance(500)
            poco("ui_button_again").click()
            sleep(3)
            if poco("ui_center_text").exists():
                poco("ui_center_text").click()
            print(f'第{i}次循环完成')
        elif i == 2:
            poco("ui_button_again").wait_for_appearance(500)
            if poco(name='ui_btn_detail').exists():
                poco(name='ui_btn_detail').click()
            poco(name='ui_button_back').click()
            print(f'第{i}次循环完成，对局结束，停留在牌桌，等待播放番型动画')
    end_time = time.time()
    print(f'=====疯狂⑧红中用例执行完成，用时{end_time-start_time}秒=========')