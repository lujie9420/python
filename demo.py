# 2019年12月7号 开始python


class inttuple(tuple):
    # __slots__ = (iter)

    def __new__(cls, iter):
        f = [i for i in iter if isinstance(i, int) and i > 0]
        print(f)
        """调用父类tuple的new方法"""
        return super().__new__(cls, f) #产生的结果就是输出元组数据（）

#
# lis = inttuple([2, -2,3, ['w', 'e'], 4])
# lis.qq = 'ju'
# print(lis.qq)
# ty = ([3,45,2])
# ty.x = '3'
# print(ty.x)

"""

"""

"""可管理的对象属性"""
"""
形式上是属性访问
实际上调用的是方法
"""

# class grander():
#     def __init__(self,age):
#         self.age = age
#
#     def get__age(self):
#         return self.age
#
#     def set__age(self, age):
#         if not isinstance(age, int):
#             raise TabError('Type Error')
#         self.age = age
#
#     R = property(get__age, set__age)
#
#
# res = grander(12)
# res.R = '20'
# print(res.R)
from functools import total_ordering
import abc
import math


@total_ordering
class A(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def area(self):
        pass


    def __lt__(self, other):
        return self.area() < other.area()
#
    def __eq__(self, other):
        return self.area() == other.area()


class cirle(A):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * math.pi

#
#
class reck(A):
    def __init__(self, t, h):
        self.t = t
        self.h = h

    def area(self):
        return self.t * self.h


    # def __str__(self):
    #     return '(%s,%s)'%(self.t,self.h)


# a = cirle(1)
# b = reck(2, 4)
# print(b <= a)

# import os
# path1 = 'join'
# print(os.path.join('E:\python\项目\面向对象.dir',path1))
# print(os.path.exists('E:\python\项目\面向对象.dir'))

# io = [1,2,45,5,34,53,12,2,4]
# io.sort()
#
# print(io)
# import time
# print(time.time())

