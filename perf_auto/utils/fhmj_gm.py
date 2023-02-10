import requests    #使用Pycharm来抓取网页的时候，要导入requests模块
from urllib.parse import urlencode     #由于使用的是post请求，是通过request body传递参数，而body中的data参数是用urlencoded形式传过去的，用urlencode处理一下
# import json
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

def request():
    #获取账户ID
    poco("ui_top_left_user_image").click()
    id = poco("ui_number_id").attr('text')
    num_id = id[3::]
    print('你的账户ID：'+ num_id)
    poco("ui_close_btn_userinfo").click()

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

    data1 = {   #请求的data参数
        'userId':num_id,
        'itemId':'user:conch',
        'count':'1000000',
        'decoration':''
    }

    data2 = {
        'userId': num_id,
        'itemId': 'user:chip',
        'count': '10000000000000000',
        'decoration': ''
    }

    post_data1 = urlencode(data1)    #使用urlencode方法处理请求的data数据。因为请求头中的Content-Type使用的是x-www-form-urlencoded，所以需要处理。
    post_data2 = urlencode(data2)
    r = requests.post(url=url, data=post_data1, headers=header)   #向HTML网页提交POST请求的方法并赋值给对象
    R = requests.post(url=url,data=post_data2, headers=header)

    A = r.text
    B = '增减成功'
    if B in A:
        print('接口调用成功')
    else:
        print('接口调用失败')
    # print(r.text)  #返回响应内容的字符串形式
    # print(r.content)   #内容的二进制形式
    # print(r.url)   #返回响应HTML地址
    # print(r.status_code) #返回状态码（内容值为‘200’表示访问成功）

if __name__ == '__main__':
    request()


