from airtest.core.api import *
from test_fhmj_baseclass import BaseClass
from utils import device_conn
import logging

class test_fhmj_case(BaseClass):
    def __init__(self):
        BaseClass.__init__(self)
    def test_hzxl(self):
        self.enter_duiju(self.DT_HZXL, self.HZXL_HZXL)
        self.open_hosted()
        for i in range(1, 6):
            self.send_jinbi()
        self.close_hongbao()
        self.end_shousheng()
        self.end_again()
        self.open_hosted()
        self.back_duiju()
        self.back_dating()
    def test_fk13y(self):
        self.enter_duiju(self.DT_HZXL, self.FK13Y_FK13Y)
        self.open_hosted()
        for i in range(1, 6):
            self.send_jinbi()
        self.end_again()
        self.open_hosted()
        self.back_duiju()
        self.back_dating()
    def test_fk8hz(self):
        self.enter_duiju(self.DT_HZXL, self.FK8HZ_FK8HZ)
        self.open_hosted()
        for i in range(1, 6):
            self.send_jinbi()
        self.end_again()
        self.open_hosted()
        self.back_duiju()
    def test_fhdx(self):
        touch(self.duiju_debug)
        touch(self.duiju_fxdh)
        touch(self.duiju_fxdh_bf)
        wait(self.fxdh_sqsm, timeout=1000)
        self.back_dating()




if __name__ == '__main__':
    logging.getLogger("airtest").setLevel(logging.ERROR)
    device_conn.wifi_connect()
    case = test_fhmj_case()
    # case.test_fk8hz()
    case.test_fhdx()


