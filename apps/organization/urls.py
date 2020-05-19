# @TIME : 2020/4/25 22:48
# @Author : lj
# @file : .py

from django.urls import path ,re_path
from . import views
from django.views.decorators.csrf import csrf_exempt
# 应用命名空间
app_name = 'org'

urlpatterns = [
    # path("",views.index,name='index'),
    path("org/",views.OrgView.as_view(),name='org'),
]