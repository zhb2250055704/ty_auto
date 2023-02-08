from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

import os
def bffxdh():
    # 在疯狂8红中对局结束后，直接播放番型动画
    print('======开始执行播放番型动画用例=======')
    poco(text='>').click()
    poco(name='18').click()
    poco(name='ui_btn_autofxplay').click()
    start_time = time.time()
    print('开始播放番型动画')
    wait(Template(r"images/fhmj_img/sqsmcs.png"), timeout=1000)
    print('ok已找到最后一个动画：十全十美')
    end_time = time.time()
    print(f'======播放番型动画用例已完成，共用时{end_time-start_time}秒=========')
    print('')
    # 后置操作：返回界面
    poco(name='ui_table_out').click()
    poco(name="ui_btn_1").click()
    print('已返回大厅')
    if poco(name='btn_go').exists():
        poco("btn_close").click()
        print(f'关闭雀神弹窗')


def test111():
    cwd = os.getcwd()
    print(cwd)
    wait(Template(r"images/fhmj_img/sqsmcs.png"), timeout=1000)

if __name__ == '__main__':
    cwd = os.getcwd()
    print(cwd)
    a = time.time()
    sleep(1)
    b = time.time()
    print(b-a)
    # bffxdh()