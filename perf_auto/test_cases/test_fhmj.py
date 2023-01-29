from airtest.core.api import *


from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

# 商城
def shangcheng():
    poco("shop_spine").click()
    sleep(60)
    for i in range(1,5):
        poco("ui_tab_layout").child("MJStoreTab")[0].child("Image (1)").click()
        poco("ui_tab_layout").child("MJStoreTab")[1].child("Image (1)").click()
        #poco("ui_tab_layout").child("MJStoreTab")[2].child("Image (1)").click()
    for i in range(1,6):
        poco("ui_ScrollViewContent").child("MJStoreItemCell")[1].child("ui_btn_ok").click()
        poco("ui_bottom_text").click()
    poco("ui_btn_back").click()