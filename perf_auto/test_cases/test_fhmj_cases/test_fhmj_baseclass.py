from airtest.core.api import *
from utils import device_conn
import logging


class BaseClass(object):
    def __init__(self):
        self.DT_HZXL = Template(r"DT_HZXL.png")
        self.DT_FK13Y = Template(r"DT_FK13Y.png")
        self.quick_start = Template(r"quick_start.png")
        self.quick_start_jinbi = Template(r"quick_start_jinbi.png")
        self.DHL_ZB = Template(r"DHL_ZB.png")
        self.DHL_HD = Template(r"DHL_HD.png")
        self.DHL_CJ = Template(r"DHL_CJ.png")
        self.DHL_DB = Template(r"DHL_DB.png")
        self.HZXL_HZXL = Template(r"HZXL_HZXL.png")
        self.FK13Y_FK13Y = Template(r"FK13Y_FK13Y.png")
        self.FK8HZ_FK8HZ = Template(r"FK8HZ_FK8HZ.png")
        self.skip_guide = Template(r"skip_guide.png")
        self.duiju_hosts = Template(r"DUIJU_hosts.png")
        self.duiju_debug = []
        self.duiju_fxdh =  Template(r"duiju_fxdh.png")
        self.duiju_fxdh_bf = Template(r"duiju_fxdh_bf.png")
        self.fxdh_sqsm = Template(r"sqsmcs.png")
        self.duiju_again = Template(r"duiju_again.png")
        self.duiju_touxiang = [0.93,0.3]
        self.start_hosts = Template(r"start_hosts.png")
        self.jinbi = Template(r"jinbi.png")
        self.hongbao_gongxihuode = Template(r"hongbao_gongxihuode.png")
        self.hongbao_queding = Template(r"hongbao_queding.png")
        self.hongbao_buzaitishi = [0.46,0.902]
        self.shousheng_lingqu = Template(r"shousheng_lingqu.png")
        self.fanhuiyouxi = Template(r"fanhuiyouxi.png")
        self.fanhuiduiju = Template(r"fanhuiduiju.png")
        self.fanhuidating = Template(r"fanhuidating.png")
        self.rengyaolikai = Template(r"rengyaolikai.png")
        self.queshen = Template(r"queshen.png")
        self.guanbi = Template(r"guanbi.png")

    def enter_duiju(self,dating,moshi):
        touch(dating)
        touch(moshi)
        touch(self.quick_start)
        if exists(self.skip_guide):
            touch(self.skip_guide)
            print('关闭对局引导的提示')
        if exists(self.quick_start_jinbi):
            touch(self.quick_start_jinbi)
            print('关闭金币太多的提示')
        print('进入对局')

    def open_hosted(self):
        hosts = True
        while hosts:
            wait(self.duiju_hosts,timeout = 30)
            if exists(self.duiju_hosts):
                touch(self.duiju_hosts)
                touch(self.start_hosts)
                hosts = False
                print('开启托管模式')
            else:
                hosts = True

    def send_jinbi(self):
        w, h = device().get_current_resolution()  # 获取手机分辨率
        touxiang = True
        while touxiang:
            if exists(self.jinbi):
                touch(self.jinbi)
                touxiang = False
            else:
                touch([self.duiju_touxiang[0] * w, self.duiju_touxiang[1] * h])
        sleep(1)
        print('发送金币成功')

    def close_hongbao(self):
        w, h = device().get_current_resolution()  # 获取手机分辨率
        hongbao = True
        while hongbao:
            wait(self.hongbao_gongxihuode,timeout = 400)
            sleep(1)
            touch([self.hongbao_buzaitishi[0] * w, self.hongbao_buzaitishi[1] * h])
            touch(self.hongbao_queding)
            sleep(1)
            if exists(self.hongbao_gongxihuode):
                hongbao = True
                print('关闭红包失败，尝试再次获取红包')
            else:
                hongbao = False
                print('关闭红包成功，勾选不再提示')

    def end_shousheng(self):
        wait(self.shousheng_lingqu,timeout=400)
        if exists(self.shousheng_lingqu):
            touch(self.shousheng_lingqu)
            print('对局结束，领取首胜奖励')

    def end_again(self):
        wait(self.duiju_again, timeout=400)
        if exists(self.duiju_again):
            touch(self.duiju_again)
            print('对局结束，再来一局')

    def back_duiju(self):
        wait(self.duiju_again,timeout=400)
        if exists(self.fanhuiyouxi):
            touch (self.fanhuiyouxi)
        touch(self.fanhuiduiju)
        print('对局结束，返回对局')

    def back_dating(self):
        touch(self.fanhuidating)
        touch(self.rengyaolikai)
        print('对局结束，返回大厅')
        self.close_queshen()

    def close_queshen(self):
        if exists(self.queshen):
            touch(self.guanbi)
            print('关闭雀神弹窗')

if __name__ == '__main__':
    logging.getLogger("airtest").setLevel(logging.ERROR)
    device_conn.wifi_connect()
    bs = BaseClass()
    bs.enter_duiju(bs.DT_HZXL,bs.HZXL_HZXL)
    bs.open_hosted()
    for i in range(1,6):
        bs.send_jinbi()
    bs.close_hongbao()
    bs.end_shousheng()
    bs.end_again()
    bs.open_hosted()
    bs.back_duiju()
    bs.close_queshen()

