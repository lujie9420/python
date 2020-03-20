# @TIME : 2019/12/24 21:24
# @Author : lj
# @file : .py
'''
定义类
'''
'''
构造方法（初始化）
def __init__(self):

特殊意义：创建对象的同时，通过对象执行这样的一个方法叫做构造方法

'''
# class fb(object):
#     #属性
#     def __init__(self): #初始化
#         self.age =self
#         self .gender = self
#         self.adder=self
#
#     #行为
#     def fc(self):
#         print(self .age,self .gender,self.adder)
# lujie = fb()
# lujie.age=18
# lujie.gender = 'male'
# lujie.adder ='无锡'
# lujie.fc()
# huang = fb()
# huang.adder ='苏州'
# huang.fc()

'''
def __str__(self)
1.用return 关键字来返回
2.只能是字符串，如果非str  str()
'''

'''
私有属性，不想要别人访问
但是类的内部可以调用私有属性
'''
# class fb(object):
#     def __init__(self):
#         self .name = 'liu'
#         self .__age = 18  #加下划线外部不可访问,私有属性
#     def get_odd(self):
#         print(self.__age)
#     def set_odd(self,age):
#         self .__age = age
# fc = fb()
# print(fc.name)
#
# fc.get_odd()
# fc.set_odd('22')
# fc.get_odd()

'''
成员
'''
'''
property
# '''
# class fc:
#     def __init__(self):
#         self.name = 'lu'
#     def fb(self):
#         self .name = 'jie'
#         print(self.name)
#
# w = fc()
# w.fb()
# res = w.name
# print(res)
'''
继承
可以重写的同时并且继承父类的方法  super.fb(self) 或者类名调用
'''
# class ob(object):
#     def fb(self):
#         print( 'd')
# class ob1 (ob):
#     def fb1(self):
#         print('python')
#     def fb(self):
#         # super(ob1,self).fb()  #或者下面方法
#         ob.fb(self)
#         print('c')
# a = ob1()
# a.fb()
# a.fb1(
# print(ob1.__mro__)

'''
反射
'''
# def fc():
#     res = input('请输入一个网页名：').strip()
#     modules,func=res.split('/')
#     o = __import__(modules)
#     # print(o)
#     if hasattr(o,func):
#         t = getattr(o,func)
#         t()
#     else:
#         print ('404')
# fc()
'''
主动抛出异常

'''
# try:
#
#     raise Exception('主动')
# except Exception as e:
#     print(e)
'''
自定义异常
'''
# class lu(Exception):
#     def __init__(self,mag):
#         self.info = mag
#
#     def fb(self): #或者 __str__
#         return self.info
# # err = lu('错误报告')
# # err.fb()
# # print(err)
#
# try:
#     raise lu('cuowu')
# except lu as err:
#     print(err)
'''
断言的例子如下 （类似于if条件判断语句）
'''

# try:
#     int(2)
#     print('lujie')
#     assert int('w')
#     print('haung')
# except Exception as e:
#     print(e)

'''
# 模块
# '''
# import new
# new.fb()
# import os
# # print(os.path.exists('deom.py'))
#
# # lu = 'today\\happy'
# # if not os.path.exists(lu):
# #     os.makedirs(lu)
# # os.removedir ('today\\happy')
#

import random

# print(random.random(1,10)) #随机取整【1,10）
# print(random.randint(1,10)) #随机取整[1,10]
# li = [1,2,3,4]#可变
# random.shuffle(li)  #洗牌 对Li 本身进行操作 ，只能传列表
# print(li)
# print(random.sample(li,2))
# print(random.randrange(1,10,2))

'''
字母加数字随机组合验证码 5个
'''
# def fc():
# #     li=''
# #     for i in range(5):
# #         a = str(random.randrange(10))
# #         b = chr(random.randrange(65,91)) #65-90 对应的字母是 A-Z
# #         num = random.choice([a,b])
# #         li +=num
# #     print(li)
# # fc()
# li = ''
# a = str(random.randrange(10))
# b = chr(random.randrange(65, 91))  # 65-90 对应的字母是 A-Z
# num =  random.choice([a,b])
# # li += num
# # print(li)
# # import re
# s='python'
# res = re.findall('[a-d]','abcd')
# print(res)
# '''
# \转义字符
# \和元字符搭配-->去除特殊功能(\.) -->转为普通字符
# 相反 普通字符加上\ 就会实现特殊功能
# '''
#
# print(re.findall('\d{2}','1234'))
# print(re.findall('\d+','1234'))
# print(re.findall('\d*','aa1234'))
# # print(re.findall('\w*','aa1234'))
# '''
# re.search() 返回的是一个对象，末尾需要加group() 来获取结果
# 只会匹配一个 就不会往下找
# '''
# print(re.search('py','python').group())
#
# '''
# re.match() 只在字符串开始匹，返回也是对象 需要用group()调用
# '''
# print(re.match('as','asdf').group())
#
# '''
# re.split() 拆分 （重点）
# '''
# print(re.split('p','1python'))
#
# '''
# re.sub() 替换 相当于replace (用正则的规则去替换）
# '''
# print(re.sub('w.+d','lujie','hello world'))

# '''
# re.compile()
# 1.转为正则对象
# 2.可重复使用一个规则
# '''
# obi = re.compile('com')
# print(re.findall('com','sicom'))
# print(re.findall('com','cicomse'))
#
# from lujie import fb1
# fb1.fb()
# from lujie import *
# fb1.fb()
# f = open('456.txt','w')
# b = open('123.txt','r')
# print(b.readlines())
# f.writelines(['lu\n','jie'])
# f.write('e')
# print(f.tell())
# with open('456.txt','r') as f:
#     print(f.read())

'''
实现不同类的相同接口
'''
from math import pi

import abc

class shape(metaclass= abc.ABCMeta):
    @abc.abstractmethod
    def area(self):
        pass
class A(shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * pi


class B(shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


class C(shape ):
    def __init__(self,ta,bb,h):
        self.ta = ta
        self.bb = bb
        self.h = h

    def area(self):
        return (self.ta + self.bb) * self.h / 2


Ae = A(2)
Be = B(3, 4)
Ce = C(2,3,4)


def both_two(class_name):
    lis = ['area']
    for i in lis:
        f = getattr(class_name, i,None)
        if f:
            return f()


# lt = [Ae, Be,Ce]
# result = list(map(both_two, lt))
# print(result)

import socket
'''
1.创建套接字
family = AF_INET ， 协议族 ipv4
type = SOCK_STREAM 套接字类型 UDP
'''
#发送数据
def send_data(s):
    data = input('请输入要发送的数据：')
    # ip = input('请输入要发送的ip:')
    # port = int(input('请输入要发送的端口：'))
    s.sendto(data.encode('gbk'),('localhost',778))
#接收数据
def recv_data(s):
    recv = s.recvfrom(1024)
    #接收数据的是一个元组
    recv_data = recv[0]
    recv_ip = recv[1]
    print('打印的数据是：',recv_data.decode('gbk'))
    print('打印的ip和端口是：',recv_ip)


def main():
    #创建一个udp套接字
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定端口
    s.bind(('',778))
    while True:
        send_data(s)
        recv_data(s)
   #


    #关闭套接字

# if __name__ == '__main__':
    # main()

'''
闭包以及装饰器
'''
def fb(num):
    print('i am fb')
    def fb1(num1):
        print('i am fb1')
        nums = num()
        return nums + num1
    return fb1
@fb
def fb2():
    # print(3)
    return 4

print(fb2(3))



