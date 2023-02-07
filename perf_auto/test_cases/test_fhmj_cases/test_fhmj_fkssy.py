from airtest.core.api import *


from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

def fkssy():
    poco(name = "HallBtnxueliu_fk13y").click()
    poco(name = 'anniu_zi1').click()
    print(f'---快速开始---')
    if poco("RulesView").child("Image").exists():
         poco("ui_btn_close").click()
         print(f'---关闭规则弹窗---')
    else:
        print(f'---无规则弹窗---')
    for i in range(1,3):
        poco(texture="table_top_fanxing").wait_for_appearance()
        #poco("ui_img_yellow").click()
#         poco("ui_img_menu_flod").click()
        for x in range(1,6):
            poco(name = "table_people_1").click()
            poco.click([0.5778258, 0.5478659])
#             poco("ui_child").child("MagicEmojiItem")[4].child("ui_bg").click()
        if poco(name = "ui_img_menu_flod").exists():
            poco(name = "ui_img_menu_flod").click()
            poco(name="ui_table_zidonghupai_text").click()
            print(f'---托管成功---')
        else:
            poco(name = "ui_img_menu_unflod").click()
            poco(name="ui_table_zidonghupai_text").click()
            print(f'---托管成功---')
#         poco("ui_waitOpengift_login").wait_for_appearance(timeout=400)
#         poco("close").wait(timeout=300)
#         print(f'---关闭红包---')
        poco(name = "title0").wait_for_appearance
        poco("ui_press").wait_for_appearance(timeout=500)
        if poco("title").exists():
            poco(name = "ui_btn_continue").click()
        poco("ui_button_again").wait_for_appearance()
        if i == 1:
            poco("ui_button_again").click()
            print(f'第一次循环完成')
        elif i == 2:
            if poco(name = 'ui_btn_detail').exists():
                poco(name = 'ui_btn_detail').click()
            poco(name = 'ui_button_back').click()
            poco(name = 'ui_table_out').click()
            poco(name = "ui_btn_1").click()
            print(f'第二次循环完成')
    if poco(name="Image (2)").exists():
        poco("btn_close").click()
        print(f'关闭雀神弹窗')