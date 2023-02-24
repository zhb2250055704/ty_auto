import requests    #使用Pycharm来抓取网页的时候，要导入requests模块
from urllib.parse import urlencode     #由于使用的是post请求，是通过request body传递参数，而body中的data参数是用urlencoded形式传过去的，用urlencode处理一下



'''
获取ID方法 huoquID() 返回ID，在RUN方法里保存起来ID
增加电卷方法，gm_dianjuan(id,num) 在run方法里，传入ID和数量 进行发送
增加金币方法，gm_jinbi(id,num) 在run方法里，传入ID和数量 进行发送
'''

def huoquID(poco):
    #获取账户ID
    poco("ui_top_left_user_image").click()
    id = poco("ui_number_id").attr('text')
    num_id = id[3::]
    print('你的账户ID：'+ num_id)
    poco("ui_close_btn_userinfo").click()
    try:
        with open(r'config/config_id.txt','w+') as f:
            f.write(num_id)
    except Exception as e:
        print('id获取失败，请打开游戏，进入游戏大厅，再运行此模块')
    return num_id

def get_id():
    with open(r'config/config_id.txt', "r") as f:
        id = f.read()
    return id

def gm_dianjuan(id,num):
    url = 'http://81.70.14.160:8016/gtest/majiang/send_rewards'    #请求地址
    header = {   #请求头
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Content-Length':'63',
        'Content-Type':'application/x-www-form-urlencoded',
        'Host':'81.70.14.160:8016',
        'Origin':'http://81.70.14.160:8016',
        'Referer':'http://81.70.14.160:8016/gtest/majiang/send_rewards',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    dianjuan = {   #请求的data参数
        'userId':id,
        'itemId':'user:conch',
        'count':num,
        'decoration':''
    }
    post_data1 = urlencode(dianjuan)    #使用urlencode方法处理请求的data数据。因为请求头中的Content-Type使用的是x-www-form-urlencoded，所以需要处理。
    r = requests.post(url=url, data=post_data1, headers=header)   #向HTML网页提交POST请求的方法并赋值给对象
    A = r.text
    B = '增减成功'
    if B in A:
        print(f'成功为id:{id}增加点券:{num}')
    else:
        print('点券接口调用失败')
    # print(r.text)  #返回响应内容的字符串形式
    # print(r.content)   #内容的二进制形式
    # print(r.url)   #返回响应HTML地址
    # print(r.status_code) #返回状态码（内容值为‘200’表示访问成功）

def gm_jinbi(id,num):
    url = 'http://81.70.14.160:8016/gtest/majiang/send_rewards'    #请求地址
    header = {   #请求头
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Content-Length':'63',
        'Content-Type':'application/x-www-form-urlencoded',
        'Host':'81.70.14.160:8016',
        'Origin':'http://81.70.14.160:8016',
        'Referer':'http://81.70.14.160:8016/gtest/majiang/send_rewards',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    jinbi = {
        'userId': id,
        'itemId': 'user:chip',
        'count': num,
        'decoration': ''
    }
    post_data2 = urlencode(jinbi)
    r = requests.post(url=url,data=post_data2, headers=header)
    A = r.text
    B = '增减成功'
    if B in A:
        print(f'成功为id:{id}添加金币:{num}')
    else:
        print('金币接口调用失败')
    # print(r.text)  #返回响应内容的字符串形式
    # print(r.content)   #内容的二进制形式
    # print(r.url)   #返回响应HTML地址
    # print(r.status_code) #返回状态码（内容值为‘200’表示访问成功）

if __name__ == '__main__':
    # id = huoquID()
    id = 112583
    # gm_dianjuan(id,1000000)
    gm_jinbi(id,100000000000)

