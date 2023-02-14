from airtest.core.api import *

def zhuangban(poco):
    print('-----装扮场景开始运行-----')
    poco("ui_hall_down_gongjulan_zhuangban").click()
    print('-----开始静置60s-----')
    sleep(60)
    print('-----静置结束-----')
    for i in range(1, 3):
        poco("ui_tab_layout").child("AdornmentTab")[0].child("Image").click()
        poco("ui_tab_layout").child("AdornmentTab")[1].child("Image").click()
        poco("ui_tab_layout").child("AdornmentTab")[2].child("Image").click()
        poco("ui_tab_layout").child("AdornmentTab")[3].child("Image").click()
        poco("ui_tab_layout").child("AdornmentTab")[4].child("Image").click()
        poco("ui_tab_layout").child("AdornmentTab")[5].child("Image").click()
    print(f'-----完成第{i}次页签切换')
    poco("ui_btn_back").click()
    print('-----装扮场景运行结束-----')

if __name__ == '__main__':
    zhuangban()