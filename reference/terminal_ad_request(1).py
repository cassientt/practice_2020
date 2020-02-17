#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 17:03
# @Author  : hfb
# @Site    : 
# @File    : terminal_ad_request.py
# @Software: PyCharm
import hashlib
import pprint
import time
import uuid

import requests

#host = 'http://127.0.0.1:12200'
# host = 'https://crm-office-test.imlaidian.com'
host = 'https://ad.imlaidian.com'
# host = 'http://192.168.10.180'
# host = 'http://127.0.0.1:12200'

url = host + '/terminalAd-api/ad/query/v2'

# 设置代理 方便抓包
proxies = {
    # "http": "http://127.0.0.1:8888"
}


def get_terminal_ad_v2(terminal, imei='', android_id='', mac='', ip='', connection_type='4G', operator_type='UNICOM'):
    """获取广告
    """
    # 请求参数
    param_dic = {'terminal': terminal, 'timestamp': int(round(time.time() * 1000)), 'nonce': 'fdksajfjdi',
                 'version': '2.0', 'requestId': str(uuid.uuid4()).replace('-', ''), 'imei': imei,
                 'androidId': android_id, 'mac': mac, 'ip': ip, 'connectionType': connection_type,
                 'operatorType': operator_type}
    # 计算签名
    # 排序后的参数值列表
    value_list = [str(param_dic[key]) for key in sorted(param_dic.keys())]
    value_list.append('f7921313-3593-448e-a748-8a15294907f7')
    sign_str = ','.join(value_list)
    # 计算md5值并添加到请求参数中
    md5 = hashlib.md5()
    md5.update(sign_str.encode('UTF-8'))
    param_dic['sign'] = md5.hexdigest()
    # 发送请求
    print('请求广告参数：')
    pprint.pprint(param_dic)
    start_time = int(round(time.time() * 1000))
    res = requests.post(url, param_dic, proxies=proxies)
    end_time = int(round(time.time() * 1000))
    print('status_code:', res.status_code)
    result_ad = res.json()
    print('请求到的广告数据：')
    print(res.text)
    pprint.pprint(result_ad)
    print('耗时：' + str(end_time - start_time))
    return result_ad


def get_terminal_ad(terminal):
    """获取广告
    """
    # 请求参数
    param_dic = {'terminal': terminal, 'timestamp': int(round(time.time() * 1000)), 'nonce': 'fdksajfjdi',
                 'version': '1.2'}
    # 计算签名
    # 排序后的参数值列表
    value_list = [str(param_dic[key]) for key in sorted(param_dic.keys())]
    value_list.append('f7921313-3593-448e-a748-8a15294907f7')
    sign_str = ','.join(value_list)
    # 计算md5值并添加到请求参数中
    md5 = hashlib.md5()
    md5.update(sign_str.encode('UTF-8'))
    param_dic['sign'] = md5.hexdigest()
    # 发送请求
    print('请求广告参数：')
    pprint.pprint(param_dic)
    start_time = int(round(time.time() * 1000))
    res = requests.post(host + '/terminalAd-api/ad/query/v2', param_dic, proxies=proxies)
    print(res.status_code)
    end_time = int(round(time.time() * 1000))
    result_ad = res.json()
    print('请求到的广告数据：')
    print(res.text)
    pprint.pprint(result_ad)
    print('耗时：' + str(end_time - start_time))
    return result_ad


# get_terminal_ad_v2('000020001660', '', '4d6928d5cd9805de', '00:ff:00:49:52:55', '8.8.8.8')

# get_terminal_ad('000050001989')
get_terminal_ad('000050001590')
