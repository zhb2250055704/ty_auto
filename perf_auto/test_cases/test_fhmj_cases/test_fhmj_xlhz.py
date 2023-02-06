from airtest.core.api import *


from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()



def hzxl():
    poco("HallBtnxueliu_hz_bxp").click()
    poco("twolevel_effpref_04").wait_for_appearance()
    poco(name = 'Image (1)').click()
#     poco("ui_tab_bg").offspring("ui_tab_layout").child("TwoLevelTab")[0].child("Image (1)").click()
    poco("jiantou_mask").click()
    #规则介绍
    if poco("RulesView").child("Image").exists():
        poco("ui_btn_close").click()
    #对局循环
    for i in range(1,4):
        poco(texture="table_top_fanxing").wait_for_appearance()
        poco("ui_img_yellow").click()
        poco("ui_img_menu_flod").click()
        poco(texture="nc_tableentry_title").click()
#         poco("ui_waitOpengift_login").wait_for_appearance(timeout=400)
        poco("close").wait_for_appearance(timeout=500)
        poco("close").click()
        if i == 1:
            poco("ui_btnBuy").wait(10)
            poco("ui_btnBuy").click()
            poco("ui_button_again").click()
        elif i == 2:
            poco("ui_button_again").wait_for_appearance()
            poco("ui_button_again").click()
            sleep(3)
            if poco("ui_center_text").exists():
                poco("ui_center_text").click()
        elif i == 3:
            if poco(name = 'ui_btn_detail').exists():
                poco(name = 'ui_btn_detail').click()
            poco(name = 'ui_button_back').click()
            poco(name = 'ui_table_out').click()
            poco(name = "ui_btn_1").click()