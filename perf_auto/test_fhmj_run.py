import logging
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
from utils import fhmj_gm
from poco.drivers.unity3d import UnityPoco
# 过滤logo
logging.getLogger("airtest").setLevel(logging.ERROR)

'''
PS: 请先运行init模块，启动初始化模块，自动执行以下步骤
    1.获取手机的IP地址
    2.跳过新手引导
    3.获取账号ID
1.连接手机：
    连接方式 有线：device_conn.youxian_connect()
    无线方式 无线：device_conn.wifi_connect() 开启无线调试模式
2.GM工具的调用：
    获取ID方法 huoquID() 返回ID，在RUN方法里保存起来ID
    增加点券方法，gm_dianjuan(id,num) 在run方法里，传入ID和数量 进行发送
    增加金币方法，gm_jinbi(id,num) 在run方法里，传入ID和数量 进行发送
3. 测试用例代码块：
    执行GM工具具体逻辑
    执行性能自动化用例场景
    执行perfdog相关操作
'''
device_conn.wifi_connect()
poco = UnityPoco()
id = fhmj_gm.get_id()

fhmj_gm.gm_dianjuan(id,100000)
# 大厅界面：大厅界面静置2分钟
# perfdog.kaishi()
# perfdog.dadian()
test_fhmj_jingzhi.jingzhi()

# perfdog.dadian()
# 活动界面："1.持续滑动活动列表20秒 2.切换一轮活动页签共5次"
test_fhmj_shangcheng.shangcheng(poco)

# perfdog.dadian()
# 商城界面："1.在商城界面静置1min 2.连续切换页签10次 3.用点券购买60亿金币5次"
test_fhmj_huodong.huodong(poco)

# perfdog.dadian()
# 装扮界面："1.在装扮界面静置1min 2.连续切换页签10次"
test_fhmj_zhuangban.zhuangban(poco)

# perfdog.dadian()
# 夺宝界面："1.在夺宝界面静置1min 2.点击抽奖进行5次抽奖操作"
test_fhmj_duobao.duobao(poco)

# perfdog.dadian()
# 红中血流："1.进行2场完整对局 2.在对局中向对手发送金币表情5次"
test_fhmj_xlhz.hzxl(poco)

# perfdog.dadian()
# 疯狂十三幺："1.进行2场完整对局 2.在对局中向对手发送金币表情5次"
test_fhmj_fkssy.fkssy(poco)

# perfdog.dadian()
# 疯狂八红中 ："1.进行2场完整对局 2.在对局中向对手发送金币表情5次"
fhmj_gm.gm_jinbi(id,10000000000000000)
test_fhmj_fk8hz.fk8hz(poco)

# perfdog.dadian()
# 胡牌特效：连续点击播放胡牌特效一轮
test_fhmj_fxdh.bffxdh(poco)

# perfdog.dadian()
# 成就界面："1.在成就界面静置1min 2.连续切换全部成就页签5次 3.领取5次成就奖励"
test_fhmj_cjjm.chengjiujiemian(poco)

# perfdog.dadian()
# 八红中界面跳转："1.点击疯狂八红中 2.点击与所持金币对应的场次 3.进出场次20次"
test_fhmj_8hzjmtz.bahongzhongtiaozhuan(poco)

# perfdog.dadian()
# 商城界面跳转："1.点击商城 2.进入退出商城20次"
test_fhmj_shangchengtiaozhuan.shangchengtiaozhuan(poco)
# perfdog.dadian()

# 后置操作部分
# 1. 停止pefdog并上传数据
# 2. 退出perfdog账号
# perfdog.tingzhi()
# perfdog.jieshu()

