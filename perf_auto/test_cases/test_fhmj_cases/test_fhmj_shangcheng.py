from airtest.core.api import *

# 商城
from poco.drivers.unity3d import UnityPoco


def shangcheng(poco):
    print('-----商城场景用例开始执行-----')
    start_time = time.time()
    poco("shop_spine").click()
    if poco(text='点券').exists():
        print('商城页面打开成功')
    else:
        poco.click([0.088, 0.888])
        print('商城页面打开成功')
    print('-----开始静置60s-----')
    sleep(60)
    print('-----静置完成-----')
    for i in range(1,6):
        poco(text='点券').click()
        poco(text='金币').click()
        print(f'-----完成第{i}次页签切换-----')
    for i in range(1,6):
        poco(text = '60').click()
        poco(name="ui_bottom_text").click()
        print(f'-----完成第{i}次金币购买-----')
        if poco(text='前往领取').exists():
            poco(name='btn_close').click()
    poco("ui_btn_back").click()
    end_time = time.time()
    print(f'-----商城用例场景结束，共用时{end_time-start_time}秒-----')

if __name__ == '__main__':
    poco = UnityPoco()
    shangcheng(poco)