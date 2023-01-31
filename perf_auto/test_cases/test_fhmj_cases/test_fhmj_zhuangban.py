from airtest.core.api import *


from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()


def zhuangban():
    poco("ui_hall_down_gongjulan_zhuangban").click()
    sleep(60)
    for i in range(1, 3):
        poco("ui_tab_layout").child("AdornmentTab")[0].child("Image").click()
        poco("ui_tab_layout").child("AdornmentTab")[1].child("Image").click()
        poco("ui_tab_layout").child("AdornmentTab")[2].child("Image").click()
        poco("ui_tab_layout").child("AdornmentTab")[3].child("Image").click()
        poco("ui_tab_layout").child("AdornmentTab")[4].child("Image").click()
        poco("ui_tab_layout").child("AdornmentTab")[5].child("Image").click()
    poco("ui_btn_back").click()