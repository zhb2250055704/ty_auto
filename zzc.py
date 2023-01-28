# -*- encoding=utf8 -*-
__author__ = "HB"

from airtest.core.api import *
import dog
#auto_setup(__file__)


#auto_setup(__file__,logdir=True,devices=["android://172.16.30.70:5555"])
device_1 = connect_device('android:///172.16.30.70:5555?cap_method=javacap&touch_method=adb')

from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()


def test():
    #大厅静置
    #sleep(120)
    #lackey.click('photo/dadian.png')
    #活动
    poco("ui_hall_down_gongjulan_huodong").click()
    for i in range(0,20):
        swipe(Template(r"tpl1672741240120.png", record_pos=(-0.322, 0.012), resolution=(2400, 1080)), vector=[0.0062, -0.358])
        swipe(Template(r"tpl1672741359731.png", record_pos=(-0.316, 0.015), resolution=(2400, 1080)), vector=[0.0004, 0.329])
    for i in range(0,3):
        poco(text="番型收集").click()
        poco(text="杠上杠新玩法").click()
        poco(text="疯狂十三幺").click()
        poco(text="每日任务").click()
        poco(text="麻将无双杯").click()
        swipe(Template(r"tpl1672740734338.png", record_pos=(-0.317, 0.0), resolution=(2400, 1080)), vector=[-0.0058, -0.3408])
        poco(text="川麻雀神杯").click()
        poco(text="麻将话费").click()
        swipe(Template(r"tpl1672739430079.png", record_pos=(-0.262, 0.012), resolution=(2400, 1080)), vector=[0.0084, 0.2987])
    poco("ui_close").click()
    dog.perfdog()
    #lackey.click('photo/dadian.png')
    #商城
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
    #装扮
    poco("ui_hall_down_gongjulan_zhuangban").click()
    sleep(60)
    for i in range(1,3):
        poco("ui_tab_layout").child("AdornmentTab")[0].child("Image").click()
        poco("ui_tab_layout").child("AdornmentTab")[1].child("Image").cliack()
        poco("ui_tab_layout").child("AdornmentTab")[2].child("Image").click()
        poco("ui_tab_layout").child("AdornmentTab")[3].child("Image").click()
        poco("ui_tab_layout").child("AdornmentTab")[4].child("Image").click()
        poco("ui_tab_layout").child("AdornmentTab")[5].child("Image").click()
    poco("ui_btn_back").click()
    #夺宝
    poco("ui_hall_down_gongjulan_draw").click()
    poco(text="夺宝").wait_for_appearance()
    poco("ui_currencyBar_4").child("img_con").click()
    for i in range(1,5):
        poco("ui_btn_add1").click()
    poco("ui_btn_buy").click()
    poco("ui_bottom_text").click()
    for i in range(1,6):
        poco("ui_btn_open_once").click()
        if poco("ui_btn_share").exists():
            poco("ui_btn_confirm").click()
            poco("ui_btn_confirm").click()
            poco("ui_btn_open_once").click()
        else:
            poco("ui_btn_again").exists()
            poco("ui_btn_confirm").click()
            poco("ui_btn_open_once").click()
    poco("ui_btn_return").click()


test()











