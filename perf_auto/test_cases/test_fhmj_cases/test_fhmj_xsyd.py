from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()


def xsyd():
    # a = input('真实姓名：')
    # b = input('身份证号码：')
    # poco(text="真实姓名").wait_for_appearance()
    # poco("ui_name_input").click()
    # poco("ui_name_input").set_text(a)
    # poco("ui_shenfenz_input").set_text(b)
    # poco("ui_currencyBar_3").click()
    # poco("ui_node_btns").click()
    # poco("title").wait(3).click()
    # if poco("title").exists():
    #     poco("title").click()
    #     print('实名认证成功')
    # else:
    #     print('实名认证失败')
    poco("ui_btn_skip").click()
    poco(name = "ui_icon").click()

if __name__ == '__main__':
    xsyd()
