# @TIME : 2020/4/29 8:53
# @Author : lj
# @file : .py

import requests
import urllib.request,urllib.parse
import random

# https://tieba.baidu.com/f?kw=%E7%AE%80%E4%B9%A6&ie=utf-8&pn=200  简书
# https://tieba.baidu.com/f?kw=%E7%AE%80%E4%B9%A6&ie=utf-8&pn=0  (n-1)*50


Header_list = ['user-agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
               'user-agent: Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19'
                ]

class Request_demo(object):

    def __init__(self):
        self.s = requests
        self.name = input('请输入要爬取的内容名称：')
        self.start = int(input('请输入起始页：'))
        self.end = int(input('请输入结束页：'))

    def get_message(self):
        #随机取一个USER-Agent用户代理
        heards = random.choice(Header_list)
        #将输入的查询条件进行转码
        kw = {'kw': self.name}
        Inputname = urllib.parse.urlencode(kw)
        #进入循环爬取从起始到结束的网址
        for i in range(self.start,self.end +1):
            #固定网址，搜索名称 符号 页数
            Root_url = ' https://tieba.baidu.com/f?'
            Name = Inputname
            Sym = '&pn='
            Pn = (i-1)*50
            #获得完整网址
            Res_url = Root_url + Name + Sym + str(Pn)
            result = self.s.get(Res_url, heards)
            # print(Res_url)
            # 将html写入本地
            filename = f'第{i}页.html'
            with open(filename, 'wb') as f:
                f.write(result.content)
                print(f'正在爬取{i}.html')


if __name__ == '__main__':
    res = Request_demo()
    R = res.get_message()



