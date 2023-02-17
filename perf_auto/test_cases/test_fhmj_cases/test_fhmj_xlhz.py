from airtest.core.api import *


def hzxl(poco):
    print('-----血流红中用例场景开始执行-----')
    start_time = time.time()
    poco("HallBtnxueliu_hz_bxp").click()
    poco("twolevel_effpref_04").wait_for_appearance()
    poco(name = 'Image (1)').click()
#     poco("ui_tab_bg").offspring("ui_tab_layout").child("TwoLevelTab")[0].child("Image (1)").click()
    poco(name = "ui_text_quick_start").click()
    #规则介绍
    if poco("RulesView").child("Image").exists():
        poco("ui_btn_close").click()
    print(f'关闭规则介绍')
    #对局循环
    for i in range(1,3):
        poco(texture="table_top_fanxing").wait_for_appearance()
        poco("ui_img_yellow").click()
        print(f'换牌成功')
        if poco(name = "ui_img_menu_flod").exists():
            poco(name = "ui_img_menu_flod").click()
            poco(name="ui_table_zidonghupai_text").click()
            print(f'托管成功')
        else:
            poco(name = "ui_img_menu_unflod").click()
            poco(name="ui_table_zidonghupai_text").click()
            print(f'托管成功')
#      poco("ui_waitOpengift_login").wait_for_appearance(timeout=400)
        if i == 1:
            for x in range(1,6):
                poco(name = "table_people_1").click()
                sleep(1)
                poco.click([0.5778258, 0.5478659])
                sleep(2)
                print(f'第{x}次金币表情发送成功')
                if poco("close").exists():
                    break
            poco("close").wait_for_appearance(timeout=500)
            poco("Checkmark").click()
            print(f'勾选不在提示')
            poco(text = "确 定").click()
            print(f'关闭红包成功')
            poco("ui_btnBuy").wait(3).click()
#             poco("ui_btnBuy").click()
            poco("ui_button_again").click()
            print(f'第{i}次循环完成')
#         elif i == 2:
#             poco("ui_button_again").wait_for_appearance()
#             poco("ui_button_again").click()
#             sleep(3)
#             if poco("ui_center_text").exists():
#                 poco("ui_center_text").click()
#             print(f'第二次循环完成')
        elif i == 2:
            poco(name = 'ui_button_again').wait_for_appearance(timeout=500)
            if poco(name = 'ui_btn_detail').exists():
                poco(name = 'ui_btn_detail').click()
            poco(name = 'ui_button_back').click()
            poco(name = 'ui_table_out').click()
            poco(name = "ui_btn_1").click()
            print(f'第{i}次循环完成')
    if poco(name='btn_go').exists():
        poco("btn_close").click()
        print(f'关闭雀神弹窗')
    end_time = time.time()
    print(f'-----血流红中场景结束，共用时{end_time-start_time}秒-----')