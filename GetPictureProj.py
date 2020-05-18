# @TIME : 2020/5/16 12:47
# @Author : lj
# @file : .py
import re
import requests

from lxml import etree
import csv


# "objURL":"http://attach.bbs.miui.com/forum/201310/19/235356fyjkkugokokczyo0.jpg" 图片网址
# http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fr=&sf=1&fmq=1567133149621_R&pv=&ic=0&nc=1&z=0&hd=0&latest=0&copyright=0&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E5%A3%81%E7%BA%B8 网页网址

# url = "https://movie.douban.com/"
# urls = 'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fr=&sf=1&fmq=1567133149621_R&pv=&ic=0&nc=1&z=0&hd=0&latest=0&copyright=0&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E5%A3%81%E7%BA%B8'
# urls = 'http://image.baidu.com/search/flip?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=88'


# res = requests.get(urls,headers=headers)
# ret = res.text
# # 去匹配获取网页图片的url地址，返回的是一个列表[含有几十个url地址]
# pic_url = re.findall('"objURL":"(.*?)"',ret)
#
#
#
# # 循环去获取每一个图片的url地址，并且去写入文件中；
# for i in pic_url:
#         # 获取图片的名字,替换
#         name = i[-10:]
#         sname = re.sub('/','',name)
#         # print(sname)
#         # 查询获取图片以一下结尾的url地址，并作出判断若没有则加上.jpg结尾
#         addname = re.search('(\.jpg|\.png|\.jpeg|\.gif)$',sname)
#         if addname == None:
#                 sname += '.jpg'
#         try:
#             with open('img/'+ name, 'wb') as f:
#                 t = requests.get(i)
#                 f.write(t.content)
#                 print('success')
#         except Exception as e:
#                 print(e)


# 爬取电影名称 详情url 评分 引言 并且保存到csv文件中

# 返回网页源码 字符串
def geturldetial(num):
    Durl = f'https://movie.douban.com/top250?start={num}&filter='
    headers = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        # 'user-agent': 'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19'
    }

    response = requests.get(Durl, headers=headers)
    response.encoding = 'utf-8'
    return response.text


# 传入网页源码 转为element对象 并使用xpath去获得电影详情信息
# xpath返回的是列表，将每个信息创建成字典，在追加到列表中返回
def getEveryItem(sourse):
    # 1，可以将html/xml字符串转化为element对象
    # 2，可以element这个对象可以为字符串或者二进制类型的数据
    html_element = etree.HTML(sourse)
    movieItemlist = html_element.xpath('//div[@class="info"]')
    # 定义空的列表
    movielist = []

    for eachmovie in movieItemlist:

        #                 创建一个字典 像列表中存储数据[{},{}]
        movieDict = {}
        title = eachmovie.xpath('div[@class="hd"]/a/span[@class="title"]/text()')
        othertitle = eachmovie.xpath('div[@class="hd"]/a/span[@class="other"]/text()')
        link = eachmovie.xpath('div[@class="hd"]/a/@href')[0]
        star = eachmovie.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()')[0]
        quote = eachmovie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()')

        if quote:
            quote = quote[0]
        else:
            quote = ''

        movieDict['title'] = ''.join(title + othertitle)
        movieDict['url'] = link
        movieDict['star'] = star
        movieDict['quote'] = quote

        movielist.append(movieDict)
    return movielist


# 写入scv文件
def writedata(movielist):
    try:
        with open('douban.csv', 'w', encoding='utf-8', newline='') as f:
            w = csv.DictWriter(f, fieldnames=['title', 'star', 'quote', 'url'])
            # 写表头
            w.writeheader()

            for each in movielist:
                # 写入每行
                w.writerow(each)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    movelist = []
    # 返回列表写入文件
    for xx in range(10):
        num = xx * 25
        res = geturldetial(num)
        movelist += (getEveryItem(res))
        writedata(movelist)
