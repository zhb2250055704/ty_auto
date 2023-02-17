from airtest.core.api import *

# 商城
from poco.drivers.unity3d import UnityPoco


def shangcheng(poco):
    print('-----商城场景用例开始执行-----')
    start_time = time.time()
    if poco("shop_spine").exists():
        print('商城页面打开成功')
    else:
        poco.click([0.0984375, 0.925265968])
        print('商城页面打开成功')
    print('-----开始静置60s-----')
    sleep(60)
    print('-----静置完成-----')
    for i in range(1,6):
        poco("ui_tab_layout").child("MJStoreTab")[0].child("Image (1)").click()
        poco("ui_tab_layout").child("MJStoreTab")[1].child("Image (1)").click()
        #poco("ui_tab_layout").child("MJStoreTab")[2].child("Image (1)").click()
        print(f'-----完成第{i}次页签切换-----')
    for i in range(1,6):
        poco("ui_ScrollViewContent").child("MJStoreItemCell")[1].child("ui_btn_ok").click()
        poco(name="ui_bottom_text").click()
        print(f'-----完成第{i}次金币购买-----')
        if poco(name="Image (2)").exists():
            poco("btn_close").click()
    poco("ui_btn_back").click()
    end_time = time.time()
    print(f'-----商城用例场景结束，共用时{end_time-start_time}秒-----')

if __name__ == '__main__':
    poco = UnityPoco()
    shangcheng(poco)