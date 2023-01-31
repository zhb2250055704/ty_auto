from airtest.core.api import *


from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

def duobao():
    poco("ui_hall_down_gongjulan_draw").click()
    poco(text="夺宝").wait_for_appearance()
    poco("ui_currencyBar_4").child("img_con").click()
    for i in range(1,5):
        poco("ui_btn_add1").click()
    poco("ui_btn_buy").click()
    poco("ui_bottom_text").click()
    for i in range(1,6):
        poco("ui_btn_open_once").click()
        sleep(5)
        if poco("ui_btn_share").exists():
            poco("ui_btn_confirm").click()
            poco("ui_btn_confirm").click()
        else:
            poco("ui_btn_again").exists()
            poco("ui_btn_confirm").click()
    poco("ui_btn_return").click()