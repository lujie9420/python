# @TIME : 2020/4/24 17:05
# @Author : lj
# @file : .py

""""""
"""
e05806bba83c2a5ecf850c31ce21143b
"""
import requests




def Send_to_mess(apii,code,mobile):
    #单条发送的url地址
    url = 'https://sms.yunpian.com/v2/sms/single_send.json'
    text = f'【卢杰】您的验证码是{code}'

    res = requests.post(url,data={
        #传入名字不能乱写，必须是 apikey mobile text
        'apikey': apii,
        'mobile':mobile,
        'text': text,

    })
    result = res.json()
    return  result

if __name__ == '__main__':
    res = Send_to_mess('e05806bba83c2a5ecf850c31ce21143b','1234','18861855928')
    print(res)

