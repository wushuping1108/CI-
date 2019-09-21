import requests


# 登录接口
lgn_url = 'http://localhost/index.php?ctl=user&act=dologin'

# 登录数据
lgn_data = {
    'email': 'testhaha2',
    'user_pwd': 'QUhGV0p2WnBhdExZVlVDaFdHak5Wc1JuRE9md0hlTEFsbklvY0tRU01hQU51ZnhNZFYlMjV1NjVCOSUyNXU3RUY0c2YxMjM0NTYlMjV1OEY2RiUyNXU0RUY2',
    'ajax': 1,
}

lgn_result = requests.post(url=lgn_url, data = lgn_data)
lgn_cookies = lgn_result.cookies['PHPSESSID']


# 线下支付
prepay_url = 'http://localhost/member.php?ctl=uc_money&act=incharge_done'
prepay_data = {
    'check_ol_bl_pay': 'on',
    'money': '1234567',
    'pingzheng': '',
    'memo': '777771',
    'payment': '5',
    'bank_id': '0',
}



cookies = {
    'PHPSESSID':'{}'.format(lgn_cookies)
}

prepay_result = requests.post(url=prepay_url,data=prepay_data,cookies=cookies)


if '立即支付' in prepay_result.text:
    print('线下充值支付成功')