from airtest.core.api import *

def jingzhi():
    start_time = time.time()
    print('-----开始静置2分钟------')
    sleep(120)
    end_time = time.time()
    print(f'------完成大厅界面静置，共用时{end_time-start_time}秒------')
