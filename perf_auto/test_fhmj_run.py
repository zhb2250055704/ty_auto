from airtest.core.api import *
from utils import device_conn
from utils import perfdog
from test_cases.test_fhmj_cases import test_fhmj_shangcheng
from test_cases.test_fhmj_cases import test_fhmj_huodong
from test_cases.test_fhmj_cases import test_fhmj_jingzhi
from test_cases.test_fhmj_cases import test_fhmj_zhuangban
from test_cases.test_fhmj_cases import test_fhmj_duobao
from test_cases.test_fhmj_cases import test_fhmj_xlhz
from test_cases.test_fhmj_cases import test_fhmj_fkssy
from test_cases.test_fhmj_cases import test_fhmj_fk8hz
from test_cases.test_fhmj_cases import test_fhmj_fxdh
from test_cases.test_fhmj_cases import test_fhmj_cjjm
from test_cases.test_fhmj_cases import test_fhmj_8hzjmtz
from test_cases.test_fhmj_cases import test_fhmj_shangchengtiaozhuan
from test_cases.test_fhmj_cases import test_fhmj_xsyd
from utils import fhmj_gm


# log 过滤 ，只显示ERROR与print打印输出
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

# 前置工作
# 0. 设置ADB端口为5555 命令:adb tcpip 5555 ,IP为手机连接wifi的IP查看即可
# 1. 连接手机 有线模式使用方法 youxian_connect() 无线使用wifi_connect()
# device_conn.wifi_connect()


# 调试模式，使用有线模式便于调试
device_conn.youxian_connect()

# 2. 创建poco对象,不使用poco注销即可
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

# 3. 执行逻辑部分
# 3.1. 具体执行逻辑,使用其他逻辑请先导包
# 3.2. 调用perfdog进行打点操作


#新手引导
test_fhmj_xsyd.xsyd()
#发放点券
fhmj_gm.request()

# 测试用例
# 大厅界面：大厅界面静置2分钟
test_fhmj_jingzhi.jingzhi()
# 活动界面："1.持续滑动活动列表20秒 2.切换一轮活动页签共5次"
test_fhmj_shangcheng.shangcheng()
# 商城界面："1.在商城界面静置1min 2.连续切换页签10次 3.用点券购买60亿金币5次"
test_fhmj_huodong.huodong()
# 装扮界面："1.在装扮界面静置1min 2.连续切换页签10次"
test_fhmj_zhuangban.zhuangban()
# 夺宝界面："1.在夺宝界面静置1min 2.点击抽奖进行5次抽奖操作"
test_fhmj_duobao.duobao()
# 红中血流："1.进行2场完整对局 2.在对局中向对手发送金币表情5次"
test_fhmj_xlhz.hzxl()
# 疯狂十三幺："1.进行2场完整对局 2.在对局中向对手发送金币表情5次"
test_fhmj_fkssy.fkssy()
# 疯狂八红中 ："1.进行2场完整对局 2.在对局中向对手发送金币表情5次"
test_fhmj_fk8hz.fk8hz()
# 胡牌特效：连续点击播放胡牌特效一轮
test_fhmj_fxdh.bffxdh()
# 成就界面："1.在成就界面静置1min 2.连续切换全部成就页签5次 3.领取5次成就奖励"
test_fhmj_cjjm.chengjiujiemian()
# 八红中界面跳转："1.点击疯狂八红中 2.点击与所持金币对应的场次 3.进出场次20次"
test_fhmj_8hzjmtz.bahongzhongtiaozhuan()
# 商城界面跳转："1.点击商城 2.进入退出商城20次"
test_fhmj_shangchengtiaozhuan.shangchengtiaozhuan()

# 后置操作部分
# 1. 停止pefdog并上传数据
# 2. 退出perfdog账号
# perfdog.tingzhi()
# perfdog.jieshu()
