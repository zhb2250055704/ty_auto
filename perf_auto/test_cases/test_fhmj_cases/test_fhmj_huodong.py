from airtest.core.api import *
#导入图片文件
from perf_auto.images import fhmj_img
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

#活动
def huodong():
    poco("ui_hall_down_gongjulan_huodong").click()
    for i in range(0,20):
        swipe(Template(r"../perf_auto/images/fhmj_img/tuodong1.png", record_pos=(-0.322, 0.012), resolution=(2400, 1080)), vector=[0.0062, -0.358])
        swipe(Template(r"../perf_auto/images/fhmj_img/tuodong2.png", record_pos=(-0.316, 0.015), resolution=(2400, 1080)), vector=[0.0004, 0.329])
    for i in range(0,3):
        poco(text="番型收集").click()
        poco(text="杠上杠新玩法").click()
        poco(text="疯狂十三幺").click()
        poco(text="每日任务").click()
        poco(text="麻将无双杯").click()
        swipe(Template(r"../perf_auto/images/fhmj_img/tuodong3.png", record_pos=(-0.317, 0.0), resolution=(2400, 1080)), vector=[-0.0058, -0.3408])
        #poco(text="川麻雀神杯").click()
        poco(text="麻将话费").click()
        swipe(Template(r"../perf_auto/images/fhmj_img/tuodong2.png", record_pos=(-0.262, 0.012), resolution=(2400, 1080)), vector=[0.0084, 0.2987])
    poco("ui_close").click()